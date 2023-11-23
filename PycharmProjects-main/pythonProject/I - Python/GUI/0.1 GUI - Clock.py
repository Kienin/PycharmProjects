from tkinter import *
from time import *

# define functions:

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000, update)

window = Tk()
window.config(background="black")

time_label = Label(window, font=("CityLight Dots", 50), fg="green", bg="black")
time_label.pack()

day_label = Label(window, font=("Cursive", 20), fg="white", bg="black")
day_label.pack()

date_label = Label(window, font=("Cursive", 15), fg="white", bg="black")
date_label.pack()

update()

window.mainloop()

