from tkinter import *
from PIL import Image, ImageTk

# define functions:
def move_up(event):
    canvas.move(amongus,0,-10)
def move_left(event):
    canvas.move(amongus,-10,0)
    print("You are moving left")
def move_down(event):
    canvas.move(amongus,0,+10)
    print("You are moving down")
def move_right(event):
    canvas.move(amongus,+10,0)
    print("You are moving right")


window = Tk()

canvas = Canvas(window, width=500, height=500)
canvas.pack()



# image set up:
image = Image.open('/II - Miscellaneous\\among_us.png')
resized = image.resize((65, 65))
#among_us = PhotoImage(file="C:\\Users\\kevin\\PycharmProjects\\pythonProject\\II - Miscellaneous\\among_us.png")
among_us = ImageTk.PhotoImage(resized)

amongus = canvas.create_image(0,0,image=among_us, anchor=NW)

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

window.mainloop()