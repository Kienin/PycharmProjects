from tkinter import *

# define functions:
def W():
    print("W is pressed")
def A():
    print("A is pressed")
def S():
    print("S is pressed")
def D():
    print("D is pressed")


window = Tk()

frame= Frame(window,bg="light blue",bd=5,relief=RAISED)
frame.place(x=0,y=0)

Button(frame, text= "W", font=("Consolas",15),width= 3, command=W).pack(side=TOP)
Button(frame, text= "A", font=("Consolas",15),width= 3, command=A).pack(side=LEFT)
Button(frame, text= "S", font=("Consolas",15),width= 3, command=S).pack(side=LEFT)
Button(frame, text= "D", font=("Consolas",15),width= 3, command=D).pack(side=LEFT)

window.mainloop()

