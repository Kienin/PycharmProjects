# Run these mini-programs
# simple - open
f = open("demofile.txt", "r")
print(f.read())
f.close()



print("===============")
# why doesn't the last two print commands don't work? b/c of the pointer
f = open("demofile.txt", "r")
print(f.read())
print(f.name)               # prints file name
print(f.mode)               # prints mode type
print(f.readline())         # readline() reads one line, at the pointer
print(f.read())             # read() reads the entire file, from the pointer
f.close()



print("===============")
# how to set the pointer at the beginning = use seek
f = open("demofile.txt", "r")
print(f.read())
print(f.name)               # prints file name
print(f.mode)               # prints mode type
f.seek(0)
print(f.readline())         # readline() reads one line, at the pointer
print(f.read())             # read() reads the entire file, from the pointer
f.close()



print("===============")
# write some with append and regular write
f = open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()
f = open("demofile.txt", "r")
print(f.read())
f.close()



print("===============")
# how to write a new line, a regurn carriage return?
# write some with append and regular write
f = open("demofile.txt", "a")
f.write("\r")
f.write("This is on a new line")
f.close()
f = open("demofile.txt", "r")
print(f.read())
f.close()



print("===============")
# how write over the file - entirely
# write some with append and regular write
f = open("demofile.txt", "w")
f.write("where is this written?")
f.write("\r")
f.close()
f = open("demofile.txt", "r")
print(f.read())
f.close()



print("===============")
# How to prepend or write/insert at particular location?
f = open("demofile.txt", "w")
f.write("where is this written?")
f.write("\r")
f.close()
f = open("demofile.txt", "r")
print(f.read())
f.close()