# OPENING A FILE:
file = open("demofile.txt", "r")
print(file.read())
file.close()



print("===============")
# The last two commands won't work due to pointer
F = open("demofile.txt", "r")
print(F.read())
print(F.name)
print(F.mode)
print(F.readline())
print(F.read())
F.close()



print("===============")
# SET POINTER USING file.seek()
file = open("demofile.txt", "r")
print(file.read())
print(file.name)
print(file.mode)
file.seek(0)
print(file.readline())
print(file.read())
file.close()



print("===============")
# WRITE: write additional text on your file
f = open("demofile.txt", "a")
f.write("I - Computer Science Rocks!!! Hi Mr KIM!!!!!")
f.close()
f = open("demofile.txt", "r")
print(f.read())
f.close()



print("===============")
# Write on A NEW LINE using: \r
F = open("demofile.txt", "a")
F.write("\r")
F.write("This is on a new line using \\r")
F.close()
F = open("demofile.txt", "r")
print(F.read())
F.close()



print("===============")
# Writing over a file completely:
file = open("demofile.txt", "w")
file.write("Overwritten the file")
file.write("\\r")
file.close()
file = open("demofile.txt", "r")
print(file.read())
file.close()



print("===============")
# Write in a specific location on the file:
f = open("demofile.txt", "w")
f.write("Writing on a specific location")
f.write("\\r")
f.close()
f = open("demofile.txt", "r")
print(f.read())
f.close()
