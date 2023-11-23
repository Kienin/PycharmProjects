from tkinter import *
import time
from Class_Ball import *



window = Tk()

# constant:
WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

# class
volleyball = Ball(canvas, 0, 0, 100, 1, 1, "white")
tennis_ball = Ball(canvas, 0, 0, 35, 4, 3, "yellow")
basketball = Ball(canvas, 0, 0, 85, 2, 3, "#800020")


while True:
    volleyball.move()
    tennis_ball.move()
    basketball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()