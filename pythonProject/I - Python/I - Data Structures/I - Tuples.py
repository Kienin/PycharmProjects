# TUPLES = a collection which is ordered and unchangeable used to group together related data
#          Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

    # Student Record:
student = ("Kevin", 18, "male")

print(student.count("Kevin"))                         # .count counts how many times () shows
print(student.index("male"))                          # .index counts which index is () at

for i in  student:
    print(i)

if "Kevin" in student:
    print("Kevin is here")

print("------------------------------------")
print("")

# Tuple_Items
# Tuple_items are ordered, unchangeable, and allow duplicate values.

# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Allow Duplicates
# Since tuples are indexed, they can have items with the same value:
tuple = ("apple", "banana", "cherry", "apple", "cherry")
print(tuple)

# Create tuple with one item: comma is important
this_tuple = ("apple",)
print(type(this_tuple))

#NOT a tuple
this_tuple = ("apple")
print(type(this_tuple))

print("------------------------------------")
print("")






# Indexing Tuples:

tuple = ("apple", "banana", "cherry")
print(tuple[1])
print(tuple[-1])

tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple[2:5])                                          # range[beginning(inclusive):ending(exclusive):skips]
# This will return the items from position 2 to 5.
# Remember that the first item is position 0,
# and note that the item in position 5 is NOT included

print(tuple[:4])
# from beginning until fourth index (kiwi) which is not included

print(tuple[2:])
# from index 2 (banana) all the way to the end

# Negative Indexing:
this_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(this_tuple[-4:-1])

print("------------------------------------")
print("")
# Negative indexing means starting from the end of the tuple.
# This example returns the items from index -4 (included) to index -1 (excluded)
# Remember that the last item has the index -1,

# Checking if Item In Tuple:
this_tuple = ("apple", "banana", "cherry")
if "apple" in this_tuple:
  print("Yes, 'apple' is in the fruits tuple")


print("------------------------------------")
print("")








# Updating Tuple Values:
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#
# BUT You can add more tuples:1
this_tuple = ("apple", "banana", "cherry")
y = ("orange",)
this_tuple += y

print(this_tuple)

# Adding Multiple Tuples:
x = ("apple", "banana", "cherry")
y = ("orange", "kiwi")
a = ("pear",)
z = x + y + a

# Multiplying Tuples:
fruits = ("apple", "banana", "cherry")
my_tuple = fruits * 2

print(my_tuple)
print(z)

# Deleting Tuples
'''
fruits = ("apple", "banana", "cherry")
del fruits
print(fruits) #this will raise an error because the tuple no longer exists
'''
print("------------------------------------")
print("")








# Unpacking Tuples:
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(f"green is: {green}")
print(f"yellow is: {yellow}")
print(f"red is: {red}")

# If the number of variables is less than the number of values,
# you can add an * to the variable name and the values will be assigned to the variable as a list:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# If the asterisk is added to another variable name than the last,
# I - Python will assign values to the variable until the number of values left matches the number of variables left.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

print("------------------------------------")
print("")





# Looping Tuples:
# For Loop:
items = ("gun", "knife", "sword")
for i in range(len(items)):
  print(items[i])

print("")
# While Loop:
things = ("katana", "claymore", "kukri")
i = 0
while i < len(items):
  print(items[i])
  i = i + 1

# It is also possible to use the tuple() constructor to make a tuple.
tuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(tuple)
