from tkinter import *
from PIL import Image, ImageTk

# Create root window
root = Tk()

# Open image and resize it
image = Image.open('../../Miscellaneous/green_icon.png')
resized = image.resize((100, 100))

# Create PhotoImage from resized image
photo_image = ImageTk.PhotoImage(resized)

# Create label and set image
label = Label(root, image=photo_image)
label.pack()

root.mainloop()