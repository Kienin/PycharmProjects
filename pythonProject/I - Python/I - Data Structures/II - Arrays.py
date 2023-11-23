# ARRAYS:  used to store multiple values in one single variable:

cars = ["Ford", "Volvo", "BMW"]

# Accessing elements in an array:
x = cars[0]
print(x)

# Modify elements in an array:
cars[0] = "Toyota"
print(cars[0])

# LEN() method returns the length of an array (the number of elements in an array).
print("\nLength or array:")
x = len(cars)
print(x)

# Looping through an array:
print("\nFor loop in array:")
for x in cars:
  print(x)

# APPEND() method adds elements in to an array
print("\nAdding elements in array:")
cars.append("Jeep")
print(cars)

# POP() method removes elements in index x in an array
print("\nPopping elements in array")
cars.pop(3)
print(cars)

# REMOVE() method removes a specific element in an array
print("\nRemoving elements in array:")
cars.remove("Volvo")
print(cars)

"""
ARRAY METHODS:
append()	Adds an element at the end of the list
clear() 	Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index() 	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
"""
