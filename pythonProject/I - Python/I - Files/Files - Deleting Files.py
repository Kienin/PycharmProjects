# DELETING FILES
import os

path = '/II - Miscellaneous\\TEXT.txt'

try:                                 # To make sure program doesn't crash when trying to delete a file that doesnt exist
    os.remove(path)
except FileNotFoundError:
    print("That file was not found")

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