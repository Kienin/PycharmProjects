from tkinter import *
import random

def counter():
    global count
    if 'count' not in globals():
        count = 0
    count += 3
    return count

def yes():
    new_window = Tk()
    new_window.geometry("500x100")
    label = Label(new_window, text= "GAYYYY", font=(('Arial'),50))
    label.pack()
    new_window.mainloop()

def hover(event):
    x_coord = random.randint(10, 480)
    y_coord = random.randint(10, 480)
    # changes the place of the No button randomly on the window:
    button.place(x=x_coord, y=y_coord)
    yes_increase()

def yes_increase():
        current_size = 25
        button_yes.config(font=("Comic Sans", (current_size+counter())))

window = Tk()
window.title("Serious Question")
window.geometry("500x500")

label = Label(window, text="Are you gay?", font=("Comic Sans", 25))
label.pack()

button_yes = Button(window, text="Yes", font=("Comic Sans", 19), command=yes)
button_yes.pack()

button = Button(window, text="No", font=("Comic Sans", 10))
button.bind("<Motion>", hover)
button.pack()

window.mainloop()
