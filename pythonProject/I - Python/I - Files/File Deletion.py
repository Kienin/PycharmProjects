# To delete a file, you must import the OS module, and run its os.remove() function:
import os

os.remove("demofile.txt")

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("This file does not exist")


# Deleting Folders:
# os.rmdir("folder")
