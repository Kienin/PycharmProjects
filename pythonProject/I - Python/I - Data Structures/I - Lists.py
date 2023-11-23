# LIST = used to store multiple items in a single variable
#        lists items are ordered, changeable, can have duplicates, can be any data types

food = ["pizza", "hamburger", "hotdog", "spaghetti"]
print(food)
print(food[1])                                      # elements can be called out using index (starting from 0) in brackets

food[3] = "sushi"
print(food)
print(food[3])

for x in food:
    print(x)

print("--------------------------------")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
    # Functions for list:
food.append("chips")                                # .append adds another element to the list
print(food)
thislist[1:3] = ["blackcurrant", "watermelon"]      # [1:3] replaces values on index 1 and 2
print(thislist)
food.remove("hotdog")                               # .remove removes a certain element
print(food)
food.pop()                                          # .pop removes the last element on the list
print(food)
food.insert(0, "hotdog")             # .insert inserts an element into a specified index in the list
print(food)
food.sort()                                         # .sort sorts the list alphabetically
print(food)
food.clear()                                        # .clear removes all elements in a list
print(food)

print("--------------------------------")

        # List Trick:
        # Removing duplicates letters (a) in a list while maintaining order
old = ['a', 'b', 'c', 'a', 'd', 'a']

new = []
for item in old:
    if item not in new:
        new.append(item)
print(new)

# or
new = list(dict.fromkeys(old).keys())
print(new)

print("--------------------------------")





# 2D LISTS = a list of lists

drinks = ["Boba", "Soda", "Coffee"]
dinner = ["Pizza", "Hamburger", "Hotdog"]
desert = ["Ice crea", "Cake"]

food = [drinks, dinner, desert]
print(food[0][0])                                    # first [] is for list, second [] is for elements in the list

print("--------------------------------")

# range indexing lists
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# extending lists:
this_list = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
this_list.extend(tropical)
print(this_list)
# can add any array type:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

print("--------------------------------")

# Remove List Items:
this_list = ["apple", "banana", "cherry"]
this_list.remove("banana")
print(this_list)

# only removes the first occurance:
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# pop() removes the specified index or the last index if no index is specified
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# clear() empties the list:
list = ["apple", "banana", "cherry"]
list.clear()
print(list)

print("--------------------------------")



# Looping Through List:
# using len()
list = ["apple", "banana", "cherry"]
for i in range(len(list)):
  print(list[i])

this_list = ["apple", "banana", "cherry"]
for x in this_list:
  print(x)

print("")



# While loop:
print("While Loop:")
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

print("")

# List Comprehension:
print("List Comprehension:")
List = ["apple", "banana", "cherry"]
[print(x) for x in List]

print("")

# Copying Lists:
thislist = ["chicken", "rice", "fries"]
mylist = thislist.copy()                                          # .copy() copies list
print(mylist)

print("")

# Joining Lists:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["y", "x", "z"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)                                               # append() adds items in list 2 to list 1
print(list1)

list1 = ["q", "r", "s"]
list2 = [1, 2, 3]

list1.extend(list2)                                             # extend() extends list1 with items from list2
print(list1)

# LIST METHODS:
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# It is also possible to use the list() constructor when creating a new list.
list = list(("apple", "banana", "cherry")) # note the double round-brackets
print(list)
