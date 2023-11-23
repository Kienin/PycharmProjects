from tkinter import *

# define functions:
def open_file():
    print("File has been opened")

def save_file():
    print("File has been saved")

def cut():
    print("Text has been cut")

def copy():
    print("Text has been copy")

def paste():
    print("Text has been pasted")


window = Tk()

'''
For images:

open_image = Photoimage(file="file.png")
save_image = Photoimage(file="save.png")
exit_image = Photoimage(file="exit.png")

-> (..., image= open_image, compound= "left")
'''

menu_bar = Menu(window)
window.config(menu= menu_bar)

file_menu = Menu(menu_bar, tearoff=0, font= ("Comic Sans", 11))
menu_bar.add_cascade(label="File", menu=file_menu)                                     # .add_cascade() drop down effect
file_menu.add_command(label= "Open", command=open_file)
file_menu.add_command(label= "Save", command=save_file)
file_menu.add_separator()                                                              # separates Save and Exit
file_menu.add_command(label= "Exit", command=quit)                                     # quit exit shortcut

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label= "Cut", command=cut)
edit_menu.add_command(label= "Copy", command=copy)
edit_menu.add_command(label= "Paste", command=paste)

window.mainloop()