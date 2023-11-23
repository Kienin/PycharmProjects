# open() function takes in 2 parameters; filename and mode
# different methods(modes) for opening a file:
#       "r" - Read   - Default value. Opens a file for reading, error if the file does not exist
#       "a" - Append - Opens a file for appending, creates the file if it does not exist
#       "w" - Write  - Opens a file for writing, creates the file if it does not exist
#       "x" - Create - Creates the specified file, returns an error if the file exists

# In addition, you can specify if the file should be handled as binary or text mode:
# "t" - Text   - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)


f = open("demofile.txt", "r")

# If file is in a different location:
# f = open("D:\\myfiles\welcome.txt", "r")

print(f.read())

# Read():
print("\nRead up to index 5:")
print(f.read(5))

# read 1 line:
print("\nRead one line:")
print(f.readline())

# Looping through the text:
print("\nLooping:")
for i in f:
    print(i)

# Closing file:
print("\nClosing File:")
print(f.readline())
f.close()