import tkinter as tk
from bot import TwBot

window = tk.Tk()
stop_iteration = False
twBot = TwBot() 

farm_button = tk.Button(text="Farm",
    width=10,
    height=5,
    bg="blue",
    fg="yellow",
    command=twBot.farmer)
farm_button.pack()

scavange_button = tk.Button(text="Scavange",
    width=10,
    height=5,
    bg="green",
    fg="yellow",
    command=twBot.scavanger)
scavange_button.pack()

full_button = tk.Button(text="Full",
    width=10,
    height=5,
    bg="purple",
    fg="yellow",
    command=twBot.full)
full_button.pack()


window.mainloop()