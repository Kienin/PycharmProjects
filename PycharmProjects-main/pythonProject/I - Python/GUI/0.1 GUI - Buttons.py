from tkinter import *
from PIL import Image, ImageTk

# to count how many times button is clicked:
count = 0

# for command=
def click():                                                                # prints if button is clicked
    global count
    count += 1
    print(count)
    print("You clicked the button!")

window = Tk()

# to insert image in window:
photo = PhotoImage(file='../../Miscellaneous/like_button.png')

# resize image:
image = Image.open('../../Miscellaneous/like_button.png')          # from PIL; to resize image in window
resize = image.resize((50,50))
photo = ImageTk.PhotoImage(resize)

button = Button(window,                                                     # Button(master==window)
                text="This is a button!",                                   # text= displays text
                command=click,                                              # command= call back
                font=("Times New Roman", 30),                               # font= changes font
                fg= "Purple",                                               # fg= foreground (text) color
                bg= "Black",                                                # bg= background color
                activebackground= "White",                                  # activebackground= color of bg when clicked
                activeforeground= "Purple",                                 # activeforeground= color of fg when clicked
                state= ACTIVE,                                              # state= activates/disables the button

                image= photo,
                compound= "top",
                )
button.pack()                                                               # button.pack() to display button

window.mainloop()