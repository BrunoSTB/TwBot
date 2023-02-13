import win32com.client as comctl
import time

class TwBot:
    def __init__(self, window):
        self.stop_iteration = False
        self.wsh = comctl.Dispatch("WScript.Shell")
        self.running = True
        self.window = window
    
    def start(self):
       self.running = True
        
    def stop(self):
        self.running = False
    
    def prepare_farm(self):
        self.prepare()
        self.wsh.SendKeys("{8}")
        time.sleep(2)
        self.wsh.SendKeys("{9}")
        time.sleep(2)
    
    def farm(self, counter):
        if self.running:
            self.wsh.SendKeys("{m}")
        if counter >= 1000:
            self.stop()
        counter += 1
        self.window.after(225, lambda : self.farm(counter))
    
    def prepare_scavange(self):
        self.prepare()
    
    def scavanger(self):
        for j in range(4):
            self.wsh.SendKeys("{6}")
            time.sleep(1)
            self.wsh.SendKeys("{7}")
            time.sleep(2)
            self.wsh.SendKeys("{ENTER}", 0)
            time.sleep(2)
        self.wsh.SendKeys("{d}")
        time.sleep(5)
            
    def full(self):
        self.farm()
        time.sleep(5)
        self.scavanger()
        
    def cancel_action(self):
        if self.stop_iteration is False:
            self.stop_iteration = True
    
    def prepare(self):
        self.countdown()
        self.refresh_page()
        self.start()
        
    def countdown(self):
        for i in range(5):
            print(f"Starting in {5 - i}...")
            time.sleep(1)

    def refresh_page(self):
        self.wsh.SendKeys("{F5}")
        time.sleep(2)
    
        
