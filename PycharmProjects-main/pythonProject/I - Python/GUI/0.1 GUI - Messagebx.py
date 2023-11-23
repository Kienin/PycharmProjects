from tkinter import *
from tkinter import messagebox

# define Click
def click():
    '''
    messagebox.showinfo(title="This is an info message box",
                        message= "Hello user!")
#----------------------------------------------------------------------------------------
    messagebox.showwarning(title="Warning!",
                           message="You have a virus")
#----------------------------------------------------------------------------------------

    messagebox.showerror(title="ERROR",
                         message="Something went wrong")
#----------------------------------------------------------------------------------------

    if messagebox.askokcancel(title="ask ok cancel",
                           message="Do you want to do the thing?"):
        print("You did a thing")
    else:
        print("You canceled a thing")
#----------------------------------------------------------------------------------------

    if messagebox.askretrycancel(title="ask try cancel",
                                 message="Do you want to retry the thing?"):
        print("You retried a thing")
    else:
        print("You canceled a thing")
#----------------------------------------------------------------------------------------

    if messagebox.askyesno(title="Ask Yes or No",
                        message="Do you like me?"):
        print("I like you too")
    else:
        print("Why do you not like me :(")
#----------------------------------------------------------------------------------------

    answer = messagebox.askquestion(title="Ask question",
                           message="Do you like me still?")
    if(answer== 'yes'):
        print("I still like you too!")
    else:
        print("Why not :(")
    '''
    answer = (messagebox.askyesnocancel(title="yes no cancel",
                              message="Do you like going out with me?"))
                              #  icon= 'warning' or 'info' or 'error'
    if (answer==TRUE):
        print("I like going out with you too!")
    elif (answer==FALSE):
        print("Wow... I like going out with you though")
    else:
        print("Why do you not wanna answer???")


window = Tk()

button = Button(window,
                command= click,
                text= "click me",
                )
button.pack()

window.mainloop()