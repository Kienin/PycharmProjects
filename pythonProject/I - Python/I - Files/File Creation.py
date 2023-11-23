# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write  - will overwrite any existing content

f = open("demofile.txt", "a")
f.write("\nWriting this new line with f.write() function!")
f.close()

f = open("demofile.txt")
print(f.read())

f = open("demofile2.txt", "w")
f.write("I deleted the content")
f.close()

f = open("demofile2.txt")
print(f.read())


# Creating A New File:
# To create a new file in Python, use the open() method, with one of the following parameters:
# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write  - will create a file if the specified file does not exist
