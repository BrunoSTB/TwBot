import tkinter as tk
from bot import TwBot

window = tk.Tk()
twBot = TwBot(window) 
    
farm_button = tk.Button(text="Farm",
    width=30,
    height=2,
    bg="blue",
    activebackground="yellow",
    activeforeground="red",
    fg="yellow",
    command=twBot.farm)
farm_button.pack()

cancel_farm_button = tk.Button(text="Cancel Farm",
    width=30,
    height=2,
    bg="red",
    fg="yellow",
    command=twBot.stop)
cancel_farm_button.pack()

loop_farm_button = tk.Button(text="Farm Loop",
    width=30,
    height=2,
    bg="green",
    activebackground="yellow",
    activeforeground="red",
    fg="yellow",
    command=twBot.farm_loop)
loop_farm_button.pack()

cancel_farm_loop_button = tk.Button(text="Cancel Farm Loop",
    width=30,
    height=2,
    bg="red",
    fg="yellow",
    command=twBot.stop_loop)
cancel_farm_loop_button.pack()

twBot.define_buttons(farm_button, loop_farm_button)

window.mainloop()


