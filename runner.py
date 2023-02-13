import tkinter as tk
from bot import TwBot

window = tk.Tk()
twBot = TwBot(window) 
running = True

def start():
   global running
   running = True

def stop():
   global running
   running = False
    
def scavange(counter):
    if running:
        twBot.scavanger()
    if counter >= 7:
        stop()
    window.after(225, scavange)
    
farm_button = tk.Button(text="Farm",
    width=30,
    height=2,
    bg="blue",
    fg="yellow",
    command=lambda : {
        twBot.prepare_farm(),
        twBot.farm(0)
        })
farm_button.pack()

scavange_button = tk.Button(text="Scavange",
    width=30,
    height=2,
    bg="green",
    fg="yellow",
    command=lambda : {
        start(),
        twBot.prepare_scavange(),
        scavange(0)
        })
scavange_button.pack()

full_button = tk.Button(text="Full",
    width=30,
    height=2,
    bg="purple",
    fg="yellow",
    command=twBot.full)
full_button.pack()

cancel_button = tk.Button(text="Cancel",
    width=30,
    height=2,
    bg="red",
    fg="yellow",
    command=twBot.stop)
cancel_button.pack()

window.mainloop()


