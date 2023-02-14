import win32com.client as comctl
import time

class TwBot:
    def __init__(self, window):
        self.wsh = comctl.Dispatch("WScript.Shell")
        self.running = True
        self.window = window
        self.counter = 0
    
    def start(self):
        self.running = True
        self.counter = 0
        
    def stop(self):
        self.running = False
        self.counter = 0
    
    def farm(self):
        self.prepare_farm()
        self.consume_farm_list()
    
    def prepare_farm(self):
        self.prepare()
        self.wsh.SendKeys("{8}")
        time.sleep(2)
        self.wsh.SendKeys("{9}")
        time.sleep(2)
    
    def consume_farm_list(self):
        if self.counter >= 1000:
            self.stop()
        elif self.running:
            self.wsh.SendKeys("{m}")
            self.counter += 1
            self.window.after(225, lambda : self.consume_farm_list())
    
    def prepare_scavange(self):
        self.prepare()
    
    def scavanger(self):
        for i in range(7):
            for j in range(4):
                self.wsh.SendKeys("{6}")
                time.sleep(1)
                self.wsh.SendKeys("{7}")
                time.sleep(2)
                self.wsh.SendKeys("{ENTER}", 0)
                time.sleep(2)
            self.wsh.SendKeys("{d}")
            time.sleep(5)
            
    def prepare(self):
        self.start()
        self.countdown()
        self.refresh_page()
        
    def countdown(self):
        for i in range(5):
            print(f"Starting in {5 - i}...")
            time.sleep(1)

    def refresh_page(self):
        self.wsh.SendKeys("{F5}")
        time.sleep(2)
    
        
