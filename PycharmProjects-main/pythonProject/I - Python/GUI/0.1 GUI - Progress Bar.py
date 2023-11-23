from tkinter import *
from tkinter.ttk import *
import time

# define start
def start():
    GB = 100
    download = 0
    speed = 1
    while (download<GB):
        time.sleep(0.05)
        bar['value']+=(speed/GB)*100                                                # bar goes up by 10
        download+=speed
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download)+"/"+str(GB)+" GB completed")
        window.update_idletasks()                                                   # refreshes the window

window = Tk()

# define percent
percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=20, padx= 20)

percent_label = Label(window, textvariable=percent).pack()
task_label = Label(window, textvariable=text).pack()



button = Button(window, text="Download", command=start)
button.pack()

window.mainloop()
