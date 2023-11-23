# KEY EVENT = bind a key event and a function to a window

from tkinter import *

# define events:
def do_something(event):
    print("You did something")
def quit(even):
    print("You quit")
def display(event):
    print("You pressed: "+ event.keysym)
    label.config(text=event.keysym)

window = Tk()

window.bind("<Return>", do_something)                                                   # window.bind("<key>", function)
window.bind("<q>", quit)
window.bind("<Key>", display)

label = Label(window, font=("Comic Sans",100))
label.pack()


window.mainloop()