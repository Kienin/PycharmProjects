from tkinter import *
from tkinter import filedialog

# define open file:
def open_file():
    file_path = filedialog.askopenfilename(initialdir="C:\\Users\\kevin\\PycharmProjects\\pythonProject\\II - Miscellaneous\\Test File.txt",
                                           title= "Open File",
                                           filetypes= ("Test File","*.txt"))

    file = open(file_path, 'r')                                                 # 'r' == read
    print(file.read())
    file.close()

window = Tk()

button = Button(window,
                text= "Open",
                command= open_file,
                )
button.pack()


window.mainloop()