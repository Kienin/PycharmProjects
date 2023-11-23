# LIST COMPREHENSION = a way to create a new list with less syntax; can mimic certain lambda function and easier to read
# list = [expression for item in iterable]
# list = [expression if/else for item in iterable]

square = []
for i in range(1,11):
    square.append(i*i)
print(square)

square = [i*i for i in range(1,11)]                  # same code as above but fewer lines
print(square)

print("")
#---------------------------------------
# list = [expression for item in iterable if conditional]

students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
passed_students = list(filter(lambda x: x >= 60, students))                      # lambda func for passing students
print(passed_students)

student_passed = [i for i in students if i >= 60]                                # same code as above
print(student_passed)

student_passed = [i if i >= 60 else "Failed" for i in students]                  # if/else (failing grade is "Failed")
print(student_passed)

print("--------------------------------")

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list

# New_list = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

new_list = [x for x in fruits if "a" in x]

print(new_list)

print("--------------------------------")

# Iterable: can be any object
list = [x for x in range(10)]
print(list)

new_list = [x for x in range(10) if x < 5]
print(new_list)


# You can manipulate expressions in list comprehensions:
new_list = [x.upper() for x in fruits]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = ['hello' for x in fruits]
print(new_list)

# can also contain conditions:
List = [x if x != "banana" else "orange" for x in fruits]
# "Return the item if it is not banana, if it is banana return orange".

print(List)