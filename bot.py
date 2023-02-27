import win32com.client as comctl

class TwBot:
    def __init__(self, _window):
        self.window = _window
        self.wsh = comctl.Dispatch("WScript.Shell")
        self.is_consume_farm_list_running = False
        self._farm_loop_job = None
        self._farm_job = None
        self.plundered_villages = 0
        self.farm_loop_time = 60000 * 3 # measured in miliseconds
        self.number_of_villages_plunder = 1000
    
    def farm(self):
        self.prepare_farm_list()
        
    def farm_loop(self):
        self.farm()
        self._farm_loop_job = self.window.after(self.farm_loop_time, lambda : self.farm_loop())
    
    def prepare_farm_list(self):
        self.start()
        self.countdown()
        
    def start(self):
        self.is_consume_farm_list_running = True
        self.plundered_villages = 0
        
    def countdown(self, current_count = 0):
        if current_count < 5:
            print(f"INFO: Starting in {5 - current_count}...")
            current_count += 1
            self._farm_job = self.window.after(1000, lambda : self.countdown(current_count))
        else: 
            print(f"INFO: Starting in 0...")
            self.refresh_page() 

    def refresh_page(self):
        self.wsh.SendKeys("{F5}")
        self._farm_job = self.window.after(2000, self.open_farming_script)

    def open_farming_script(self):
        self.wsh.SendKeys("{8}")
        self._farm_job = self.window.after(2000, lambda : self.wsh.SendKeys("{9}"))
        self._farm_job = self.window.after(4000, self.consume_farm_list)
    
    def consume_farm_list(self):
        if self.plundered_villages >= self.number_of_villages_plunder:
            self.stop()
        elif self.is_consume_farm_list_running:
            self.wsh.SendKeys("{m}")
            self.plundered_villages += 1
            self._farm_job = self.window.after(225, lambda : self.consume_farm_list())
    
    def stop(self):
        if self._farm_job is not None:
            self.window.after_cancel(self._farm_job)
            self._farm_job = None
            self.is_consume_farm_list_running = False
            self.plundered_villages = 0
    
    def stop_loop(self):
        if self._farm_loop_job is not None:
            self.stop()
            self.window.after_cancel(self._farm_loop_job)
            self._farm_loop_job = None