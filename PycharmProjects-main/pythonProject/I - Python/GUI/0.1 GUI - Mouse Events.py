from tkinter import *

# define function:
def do_something(event):
    print("Mouse coordinates: " + str(event.x) , str(event.y))
def release(event):
    print("You released the button")

window = Tk()

window.bind("<Button-1>", do_something)                                                      # button 1 = left button
window.bind("<Button-2>", do_something)                                                      # button 2 = scroll button
window.bind("<Button-3>", do_something)                                                      # button 3 = right button

window.bind("<ButtonRelease>", release)                                                # ButtonRelease = when you let go
window.bind("<Enter>", do_something)                                                   # Enter = enter the window
window.bind("<Leave>", do_something)                                                   # Leave = leave the window
window.bind("<Motion>", do_something)                                                  # Motion= where the mouse moved

window.mainloop()

# Activates a command when mouse hovers over a button:
'''
from tkinter import *
def hover(event):
    print("Button hovered")

window = Tk()

button = Button(window, text="hover over me")
button.bind("<Motion>", hover)
button.pack()
window.mainloop()
'''