from tkinter import *

# define functions:
def drag_start(event):
    widget = event.widget                                                               # makes it all compatible
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)


window = Tk()

label = Label(window, bg="violet", width=10, height=5)
label.place(x=0,y=0)

label2 = Label(window, bg="red", width=10, height=5)
label2.place(x=100,y=100)

label.bind("<Button-1>",drag_start)                                                    # Button 1 = left button
label.bind("<B1-Motion>",drag_motion)                                                  # B1-Motion = when B1 is moving

label2.bind("<Button-1>",drag_start)
label2.bind("<B1-Motion>",drag_motion)

window.mainloop()