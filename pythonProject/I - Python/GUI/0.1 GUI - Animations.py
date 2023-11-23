from tkinter import *
from PIL import Image, ImageTk
import time


# constant: value you don't plan on changing
WIDTH = 500
HEIGHT = 500
X_VELOCITY = 3
Y_VELOCITY = 2

window = Tk()

canvas = Canvas(window, width= WIDTH, height=HEIGHT)
canvas.pack()

# image set up:

# background: first since images overlap
space = Image.open('/II - Miscellaneous\\space_background.png')
space = space.resize((500, 500))
space = ImageTk.PhotoImage(space)
#space = PhotoImage(file="C:\\Users\\kevin\\PycharmProjects\\pythonProject\\II - Miscellaneous\\space_background.png")
my_background = canvas.create_image(0,0, image= space, anchor=NW)

# main image:
image = Image.open('/II - Miscellaneous\\among_us.png')
resized = image.resize((80, 80))
among_us = ImageTk.PhotoImage(resized)
my_image = canvas.create_image(0,0,image=among_us, anchor=NW)

image_width = among_us.width()
image_height = among_us.height()
while True:
    coordinates = canvas.coords(my_image)
    #print(coordinates)
    if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
        X_VELOCITY = -X_VELOCITY
    if (coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0):
        Y_VELOCITY = -Y_VELOCITY
    canvas.move(my_image, X_VELOCITY, Y_VELOCITY)
    window.update()
    time.sleep(0.01)

window.mainloop()