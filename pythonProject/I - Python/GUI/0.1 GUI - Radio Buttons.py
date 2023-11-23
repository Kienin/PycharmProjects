# RADIO BUTTONS = similar to checkbox, but you can only select ONE from a group

from tkinter import *

food = ["Pizza", "Hamburger", "Hotdog"]

#
def order():
    if(x.get()==0):
        print("You ordered Pizza")
    elif(x.get()==1):
        print("You ordered Hamburger")
    elif(x.get()==2):
        print("You ordered Hotdog")
    else:
        print("Huh")
window = Tk()

# define x
x = IntVar()

for index in range(len(food)):                              # for loop will create how many buttons based on list length
    radiobutton = Radiobutton(window,
                              text= food[index],            # adds text at each index
                              variable= x,                  # groups radio buttons together
                              value= index,                 # gives value of each index on list
                              padx=20,
                              pady=20,
                              font= ("arial", 20),
                              indicatoron= 0,               # eliminates circle button
                              width= 25,
                              command= order)               # set command of radiobutton to function
    radiobutton.pack(anchor=W)                              # changes position of options

window.mainloop()
