from tkinter import *

def create_window():
#   new_window = Toplevel()               # Toplevel() = new window 'on top' of other windows; linked to a bottom window
    new_window = Tk()                     # Tk() = new independent window
    old_window.destroy()                  # will close out of 'old window'

old_window = Tk()

button = Button(old_window,
                text= "Create new window",
                command= create_window)
button.pack()

old_window.mainloop()