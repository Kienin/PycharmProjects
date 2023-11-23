from tkinter import *
#---------------------------------------------------------------------------------------------------------------------
# define Submit Function:
def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))                                  # iterates how many times you selected
    print("You have ordered: ")

    for index in food:
        print(index)                                                            # prints out everything you order
# define Add Function:
def add():
    listbox.insert(listbox.size(), entry_box.get())
    listbox.config(height=listbox.size())                                       # to readjust box size after adding

#define Delete Function:
def delete():
    for index in reversed(listbox.curselection()):                              # allows for multiple deletion
        listbox.delete(index)
    listbox.config(height=listbox.size())                                       # to readjust box size after deleting
#---------------------------------------------------------------------------------------------------------------------
window = Tk()

listbox = Listbox(window,
                  bg= ("#f7ffde"),
                  font= ("constantia", 20),
                  width=15,
                  selectmode=MULTIPLE,                                          # allows multiple selection
                  )
listbox.pack()

listbox.insert(1, "Pizza")
listbox.insert(2, "Pasta")
listbox.insert(3, "Garlic Bread")
listbox.insert(4, "Soup")
listbox.insert(5, "Salad")

listbox.config(height=listbox.size())                              # height= listbox.size() changes height automatically

#---------------------------------------------------------------------------------------------------------------------
# ENTRY BOX
entry_box = Entry(window)
entry_box.pack()
#---------------------------------------------------------------------------------------------------------------------
# SUBMIT BUTTON
submit_button= Button(window,
                      text= "Submit",
                      command= submit)
submit_button.pack()
#---------------------------------------------------------------------------------------------------------------------
# ADD BUTTON
add_button= Button(window,
                      text= "Add",
                      command= add)
add_button.pack()
#---------------------------------------------------------------------------------------------------------------------
# DELETE BUTTON
delete_button= Button(window,
                      text= "Delete",
                      command= delete)
delete_button.pack()


window.mainloop()