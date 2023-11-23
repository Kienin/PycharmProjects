from tkinter import *
from PIL import Image, ImageTk

# define functions:
def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-10)                        # label.winfo_x/y = current location
    print("You are moving up")                                                  # label.winfo_y - 10 = movement
def move_left(event):
    label.place(x=label.winfo_x()-10, y=label.winfo_y())                        # label.winfo_x/y = current location
    print("You are moving left")
def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+10)                        # label.winfo_x/y = current location
    print("You are moving down")
def move_right(event):
    label.place(x=label.winfo_x()+10, y=label.winfo_y())                        # label.winfo_x/y = current location
    print("You are moving right")


window = Tk()
window.geometry("500x500")

# key binding:
window.bind("<w>", move_up)
window.bind("<a>", move_left)
window.bind("<s>", move_down)
window.bind("<d>", move_right)
# arrow keys:
window.bind("<Up>", move_up)
window.bind("<Left>", move_left)
window.bind("<Down>", move_down)
window.bind("<Right>", move_right)



# image set up:
image = Image.open('/II - Miscellaneous\\among_us.png')
resized = image.resize((65, 65))
#among_us = PhotoImage(file="C:\\Users\\kevin\\PycharmProjects\\pythonProject\\II - Miscellaneous\\among_us.png")
among_us = ImageTk.PhotoImage(resized)

label = Label(window, image=among_us)
label.place(x=10, y=10)

window.mainloop()