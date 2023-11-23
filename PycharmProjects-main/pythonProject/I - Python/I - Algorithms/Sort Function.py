# sort() method = used with lists[] and won't work with other iterables(),{}
# sort() function = used with iterables

students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs"]      # LIST
names = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs")         # TUPLE

print("----------------------------------")

students.sort()                                                     # sort in alphabetical order
for i in students:                                                  # in a for loop to print out names line by line
    print(i)
print("----------------------------------")

students.sort(reverse = True)                                       # sort in reverse alphabetical order
for i in students:
    print(i)
print("----------------------------------")

sorted_students = sorted(names)
for i in sorted_students:
    print(i)
print("----------------------------------")

sorted_students = sorted(names, reverse = True)
for i in sorted_students:
    print(i)
print("----------------------------------")


students = [("Squidward", "F", 60),         # LIST OF TUPLES
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr. Krabs", "C", 78)]

    # sort by grades
grade = lambda grades: grades[1]            # lambda function creates the second column/index in the list as a function
students.sort(key = grade)
for i in students:
    print(i)
print("----------------------------------")

    # sort by age
age = lambda ages: ages[2]                  # lambda function creates the second column/index in the list as a function
students.sort(key = age)
for i in students:
    print(i)
print("----------------------------------")

students = (("Squidward", "F", 60),         # TUPLE OF TUPLES
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr. Krabs", "C", 78))

age= lambda ages:ages[2]
sorted_students = sorted(students, key = age)
for i in sorted_students:
    print(i)

print("----------------------------------")
print("")

# Sort Function:
# sort the list based on how close n is to 50:
def myfunc(n):
  return abs(n - 50)                                            # (n - 50) checks for number closest to 50

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

print("")

# List sorts are case-sensitive:
this_list = ["banana", "Orange", "Kiwi", "cherry"]
this_list.sort(key = str.lower)                                # str.lower makes all variables lower case
print(this_list)

print("")
# Reverse sort:
list = ["banana", "Orange", "Kiwi", "cherry"]
list.reverse()
print(list)