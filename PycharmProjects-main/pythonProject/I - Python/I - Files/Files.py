import os

# Checker if a file exist in our computer
# I - Python 3.11 in file location: "C:\Users\kevin\OneDrive\Desktop\I - Python 3.11 (64-bit).lnk"

path = "C:\\Users\\kevin\\OneDrive\\Desktop\\Python 3.11 (64-bit).lnk"              # needs \\ instead of \ for strings

if os.path.exists(path):                          # os.variable.exists(variable) checks if a location for a file exists
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
else:
    print("That location doesn't exist")

# Folder
path = "C:\\Users\\kevin\\OneDrive\\Desktop\\folder"              # needs \\ instead of \ for strings

if os.path.exists(path):                          # os.variable.exists(variable) checks if a location for a file exists
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):                     # os.path.isdir(variable) checks if variable is a directory
        print("That is a directory")
else:
    print("That location doesn't exist")

print("--------------------------------")





# READING FIlES
try:                                         # to prevent program from crashing if file not found
    with open("/II - Miscellaneous\\text.txt") as file:      # Directory used since it's on another directory.
        print(file.read())                                                                                     # if it was in I - Python directory, we just need the name of the file
except FileNotFoundError:
    print("That file was not found.")
print(file.closed)                           # using "with open() as file:" closes the file automatically after opening

print("--------------------------------")






# WRITING/APPEND FILES
text = "KEVIN!!!!\nThat's my name\nHello there!"                   # \n for line break; goes down one line
with open("../II - Miscellaneous/TEXT.txt", "w") as file:         # w = write
    file.write(text)                                               # file.write(variable) writes the variable in a file

text = "\nToday is 9/10/2023 and it's 6:04 PM"
with open("../II - Miscellaneous/TEXT.txt", "a") as file:         # a = append
    file.write(text)

print("--------------------------------")





# COPYING FILES

'''
Different types of copy functions in SHUTIL
1. copyfile() = copies contents of a file
2. copy()     = copyfile() + permission mode + destination can be a directory
3. copy2()    = copy() + copies metadata (file's creation and modification times)
'''
import shutil                                                      # shutil = allows for high-level operations on a file
                                                                   # 2 arguments = (src.dst)

shutil.copyfile("/II - Miscellaneous/copy.txt",
                "../II - Miscellaneous/copy1.txt")

print("--------------------------------")





# MOVING FILES

# Moving files from python folder to desktop:
import os

source = "MoveDesktop.txt"                                           # can be a file and directory
destination = "C:\\Users\\kevin\\OneDrive\\Desktop\\MoveDesktop.txt"

try:                                                                 # put in a try and except so program doesn't crash
    if os.path.exists(destination):                                  # if os.path.exists() checks if file exists already
        print("There is already a file there")
    else:
        os.replace(source, destination)                              # os.replace(src,dst) replaces the file
        print(source, "was moved")
except FileNotFoundError:
    print(source, "was not found.")

print("--------------------------------")




'''
# DELETING FILES

3 Basic Functions for Deleting Files:
#   os.remove(variable)         = delete a file
#   os.rmdir(variable)          = delete an empty directory
#   !!! shutil.rmtree(variable) = delete a directory containing files (shutil module)

import os

path = 'C:\\Users\\kevin\\PycharmProjects\\pythonProject\\II - Miscellaneous\\TEXT.txt'

try:                                # To make sure program doesn't crash when trying to delete a file that doesn't exist
    os.remove(path)
except FileNotFoundError:
    print("That file was not found")

print("--------------------------------")

    # Deleting empty folders:
import shutil

path = 'empty folder'

try:
    os.rmdir(path)
except FileNotFoundError:
    print(path, "is not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path, "was deleted")

print("--------------------------------")
'''