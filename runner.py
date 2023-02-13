import tkinter as tk
from bot import TwBot

window = tk.Tk()
twBot = TwBot(window) 
    
farm_button = tk.Button(text="Farm",
    width=30,
    height=2,
    bg="blue",
    fg="yellow",
    command=twBot.farm)
farm_button.pack()

scavange_button = tk.Button(text="Scavange",
    width=30,
    height=2,
    bg="green",
    fg="yellow",
    command=lambda : {
        twBot.prepare_scavange(),
        twBot.scavanger()
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


