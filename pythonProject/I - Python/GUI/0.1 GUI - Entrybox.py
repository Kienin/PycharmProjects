from tkinter import *

# ENTRY WIDGET = textbox that accepts a single line of user input

# Create a function for a submit button:
def submit():
    username = entry.get()                                            # entry.get gets the string from the entry window
    print("Hello "+username)
#   entry.config(state= DISABLED)                                     # state= DISABLED disables the entry box after
# Create a function for a delete button:
def delete():
    entry.delete(0, END)                                         # entry.delete(index 0, END) deletes all character
# Create a function for a backspace button:
def backspace():
    entry.delete(len(entry.get())-1, END)                             # len(entry.get())-1 deletes the last character


window = Tk()

entry = Entry(window,
              font= ("Comic Sans", 30),
              fg= "black",
              bg= "red",
              show= "*",)                                              # show= '*' replaces character inputs with *
# entry.insert(0, "Spongebob")
entry.pack(side= LEFT)                                                # side= changes the place of the entry window

# to create a submit button:
submit_button = Button(window,
                       text= "Submit",
                       command= submit)
submit_button.pack(side = RIGHT)                                       # side= changes the place of the entry button

# delete button:
delete_button = Button(window,
                       text= "Delete",
                       command= delete)
delete_button.pack(side = RIGHT)

# backspace button:
backspace_button = Button(window,
                       text= "Backspace",
                       command= backspace)
backspace_button.pack(side = RIGHT)

window.mainloop()