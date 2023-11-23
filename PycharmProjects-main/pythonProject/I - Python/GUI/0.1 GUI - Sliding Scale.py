from tkinter import *


def submit():
    print("The temperature is "+ str(scale.get()) +" degrees Celsius")

window = Tk()

# if you want to put in a hot image, do it here


scale = Scale(window, from_=0, to=100,                                                # from_=0, to=100 is the range
              length= 500,
              orient= HORIZONTAL,
              font= ("Consolas", 20),
              tickinterval= 10,                                                       # numeric indicators on the scale
              showvalue= 0,                                                           # hides current value on slider
              resolution= 5,                                                          # increment of the slider
              troughcolor= "light blue",
              fg= "crimson",
              bg= "black",
              )
scale.set(50)                                                                         # sets the slider at x position
# scale.set(((scale['from']-scale['to'])/2)+scale['to'])                              # always sets slider in the middle
scale.pack()

# if you want to put in a cold image, do it here

button = Button(window,
                text= "Submit",
                command= submit)
button.pack()

window.mainloop()