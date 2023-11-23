from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)                               # widget that manages a collection of windows and displays

tab1 = Frame(notebook)                                        # new frame for tab 1
tab2 = Frame(notebook)                                        # new frame for tab 2

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.pack(expand= True, fill= "both")                     # expands to fill any space not used, fill space on x,y

Label(tab1, text= "Hello! This is Tab 1", width=50, height=20).pack()
Label(tab2, text= "Hi! This is Tab 2", width=50, height=20).pack()



window.mainloop()