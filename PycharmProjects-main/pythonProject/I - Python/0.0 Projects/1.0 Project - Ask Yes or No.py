from tkinter import *
import random

def counter():
    global count
    if 'count' not in globals():
        count = 0
    count += 5
    return count

def yes():
    new_window = Tk()
    new_window.resizable(width=FALSE, height=FALSE)
    label = Label(new_window, text= "I love you too :)", font=(('Arial'),20))
    label.pack()
    new_window.mainloop()

def no_hover(event):
    x_coord = random.randint(15, 470)
    y_coord = random.randint(15, 470)
# changes the place of the No button randomly on the window:
    button_no.place(x=x_coord,y=y_coord)
    yes_increase()

def yes_increase():
    current_size = 25
    button_yes.config(font=("Comic Sans", (current_size + counter())))

window = Tk()
window.geometry("500x500")
window.title("Question")

label = Label(window, text="Do you love me?", font=("Comic Sans", 22))
label.pack()

button_yes = Button(window, text="Yes", font=("Comic Sans", 20), command=yes)
button_yes.pack()

button_no = Button(window, text="No", font=("Comic Sans", 15))
# when mouse is hovering over No button, no function is called:
button_no.bind("<Motion>", no_hover)

button_no.pack()


window.mainloop()