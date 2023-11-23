# CANVAS = widget that is used to draw graphs, plots, images in a window

from tkinter import *

window = Tk()

canvas = Canvas(window, height=500, width=500, )
blue_line = canvas.create_line(0,0,500,500, fill="blue", width=5)                                        # create a line
red_line = canvas.create_line(0,500,500,0, fill="red", width=5)                                          # create a line
quadrilateral = canvas.create_rectangle(50,50,250,250)                                                   # create square
points = [250,0,500,500,0,500]
polygon = canvas.create_polygon(points, fill="yellow", outline="black", width=5)                        # create polygon
arc = canvas.create_arc(0,0,500,500, fill="purple", style= CHORD)
arc = canvas.create_arc(250,250,0,0,
                        fill="orange",
                        style= PIESLICE,                                                            # style= type of arc
                        start=90,                                                                   # start= orientation
                        extent=180)

canvas.pack()

window.mainloop()
