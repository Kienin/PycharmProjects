from tkinter import *
from tkinter import filedialog

# define save file
def save_file():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\kevin\\PycharmProjects\\pythonProject\\II - Miscellaneous",  # saves in II - Miscellaneous
                                    defaultextension=".txt",                        # saves the file as a text (.txt)
                                    filetypes=[                                     # gives options on file saving
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*")
                                    ])
    if file is None:                                                                # so you dont encounter exception
        return
    file_text = str(text.get(1.0, END))                                      # gets all the text in the file
#   file_text = input("Enter text:")                                                # Don't need a text area
    file.write(file_text)                                                           # writes all the file
    file.close()                                                                    # closes the file


window = Tk()

button = Button(window, text= "Save", command= save_file)
button.pack()
text = Text(window)
text.pack()

window.mainloop()