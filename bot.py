import win32com.client as comctl
import time

wsh = comctl.Dispatch("WScript.Shell")
class TwBot:
    def __init__(self):
        self.stop_iteration = False
        
    # Google Chrome window title
    def farmer(self):
        wsh.AppActivate("br117.tribalwars.com.br/")
        countdown()
        refresh_page()

        wsh.SendKeys("{8}")
        time.sleep(2)
        wsh.SendKeys("{9}")
        time.sleep(2)
        
        for i in range(500):
            wsh.SendKeys("{m}")
            time.sleep(0.22)
    
    def scavanger(self):
        countdown()
        refresh_page()

        for i in range(7):
            for j in range(4):
                wsh.SendKeys("{6}")
                time.sleep(1)
                wsh.SendKeys("{7}")
                time.sleep(2)
                wsh.SendKeys("{ENTER}", 0)
                time.sleep(2)
            wsh.SendKeys("{d}")
            time.sleep(3)
            
    def full(self):
        self.farmer()
        time.sleep(5)
        self.scavanger()

            
def countdown():
    for i in range(5):
        print(f"Starting in {5 - i}...")
        time.sleep(1)

def refresh_page():
    wsh.SendKeys("{F5}")
    time.sleep(2)
    
        
