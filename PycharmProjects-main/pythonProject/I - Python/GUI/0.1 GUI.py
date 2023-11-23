# GUI = graphical user interface

"""
GUI tutorials:
    https://wiki.tcl-lang.org/page/winfo%28%29
    https://www.tutorialspoint.com/python/python_gui_programming.htm
"""
# widgets = GUI elements: buttons, text boxes, labels, images
# windows = serves as a container to hold widgets

from tkinter import *
from PIL import Image, ImageTk

window = Tk()                                                     # instantiate an instance of a window

window.geometry("700x700")                                        # size of window
window.title("Kevin's First GUI")                                 # change title of window

# create photo image to change GUI icon
icon = PhotoImage(file='../../Miscellaneous/green_icon.png')           # change icon on GUI
window.iconphoto(True, icon)
window.config(background="purple")                                # change background color (word/hex)

# LABEL = an area widget that holds text and/or an image within a window

# photo image:

image = Image.open('../../Miscellaneous/among_us.png')          # from PIL; to resize image in window
resize = image.resize((100,100))
photo = ImageTk.PhotoImage(resize)

label = Label(window,
              text= "Hi Jasmine!",
              font= ('Times New Roman', 40, "bold"),               # font= changes font of label
              fg= "violet",                                        # fg= changes color of label
              bg= "black",                                         # bg= changes color of background of label
              relief= SUNKEN,                                      # relief= changes border size
              bd= 20,                                              # bd= changes border width
              padx= 20,                                            # padx= changes x-axis padding between the text and border
              pady= 20,                                            # pady= changes y-axis padding between the text and border
              image= photo,                                        # image= inserts image in window
              compound= 'bottom')                                  # compound= changes image placement

label.pack()                                                       # sets label on middle top
label.place(x=200, y=200)                                         # sets label on given coordinates

window.mainloop()                                                  # place window on screen; listen for events






