from tkinter import *
from PIL import Image, ImageTk

def display():
    if(x.get()==1):
        print("User agrees")
    else:
        print("User disagrees")

window = Tk()

# define variable x
x = IntVar()

# image insert:
photo = PhotoImage(file='../../Miscellaneous/python_logo.png')

# photo image resize:
image = Image.open('../../Miscellaneous/python_logo.png')                                           # from PIL; to resize image in window
resize = image.resize((45,45))
photo = ImageTk.PhotoImage(resize)

check_box = Checkbutton(window,
                        text= "Check if you agree",
                        variable= x,
                        onvalue= 1,
                        offvalue= 0,
                        command= display,
                        font= ("comic sans", 20),
                        fg= "black",
                        bg= "white",
                        activeforeground= "black",
                        activebackground= "white",
                        padx= 25,
                        pady= 10,
                        image= photo,
                        compound= "right")

check_box.pack()

window.mainloop()