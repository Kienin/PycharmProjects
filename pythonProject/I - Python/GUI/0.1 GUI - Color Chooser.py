from tkinter import *
from tkinter import colorchooser

# define button click function:
def click():
    color = colorchooser.askcolor()
    print(color)
    color_HEX = color[1]                                          # color[1] gets the element in index 1 (the HEX value)
    print("This color in Hexadecimal is:", color_HEX)
    window.config(bg=color_HEX)                                   # will change background color

# shorter code:
#   window.config(bg=colorchooser.askcolor())

window = Tk()
window.geometry("500x500")


button = Button(window,
                text="click me",
                command= click)
button.pack()

window.mainloop()