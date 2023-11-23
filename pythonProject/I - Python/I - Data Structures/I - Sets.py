# SET = collection which is unordered, unindexed. No duplicate values.
#       Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

utensils = {"Spoon", "Fork", "Knife"}

for i in utensils:
    print(i)

utensils= {"Spoon", "Fork", "Knife", "Knife", "Knife"}
for i in utensils:
    print(i)

print("--------------------------------")

    # Methods of Sets
utensils.add("Napkin")                                      # .add adds an element to the set
print(utensils)
utensils.remove("Fork")                                     # .remove removes an element from the set
print(utensils)
utensils.clear()                                            # .clear clears the whole set
print(utensils)

utensils= {"Spoon", "Fork", "Knife", "Knife", "Knife"}
dishes = {"Bowl", "Plate", "Cup"}

utensils.update(dishes)                                     # .update() adds another set to a set
for i in utensils:
    print(i)

dinner_table = utensils.union(dishes)                       # .union() adds another set to a set in a variable


utensils= {"Spoon", "Fork", "Knife", "Knife", "Knife"}
dishes = {"Bowl", "Plate", "Cup", "Knife"}

print(utensils.difference(dishes))                          # .difference() checks for differences in sets
print(utensils.intersection(dishes))                        # .intersection() checks for similarities in sets

print("--------------------------------")
print("")



# SET = Sets are used to store multiple items in a single variable.
#       A set is a collection which is unordered, unchangeable*, and not indexed.
set = {"apple", "banana", "cherry"}
print(set)

# Duplicates are NOT ALLOWED:
this_set = {"apple", "banana", "cherry", "apple", "apple", "apple"}
print(this_set)



# The values True and 1 are considered the same value in sets, and are treated as duplicates:
thisSet = {"apple", "banana", "cherry", True, 1, 2}
print(thisSet)
# False and 0 is considered the same value:
thisSet = {"apple", "banana", "cherry", False, True, 0}
print(thisSet)

print("--------------------------------")
print("")




# Lenght of a Set:
print("Lenght of a Set:")
this_set = {"apple", "banana", "cherry"}
print(len(this_set))

# Looping Sets:
print("Looping through Set:")
set = {"apple", "banana", "cherry"}
for x in set:
  print(x)

print("")
set = {"apple", "banana", "cherry"}
print("banana" in set)
print("--------------------------------")
print("")



# Adding Set Items:
print("Adding Items in Set:")
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

print(fruits)
print("")

# Adding Sets in Sets:
print("Adding Sets in Set:")
this_set = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
this_set.update(tropical)

print(this_set)
print("")

# Adding Iterables in Set:
print("Adding Iterables in Set:")
set = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange", "pear", "durian"]
set.update(mylist)

print(set)
print("")

# Removing Set Items:
print("Removing Set Items:")
this_set = {"apple", "banana", "cherry"}
this_set.remove("banana")
print(this_set)

# discard() removes items in set:
print("Discard cherry")
set = {"apple", "banana", "cherry"}
set.discard("cherry")

print(set)
print("")

# pop() removes items randomly in set:
print("Pop randomly removes an item:")
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(f"{x} is the randomly removed item in the set")
print(thisset)
print("")

# clear() empties the set:
print("Clear empties the set")
set = {"apple", "banana", "cherry"}
set.clear()

print(f"Cleared set: {set}")
print("")

# del() deletes the set completely:
'''
this_set = {"apple", "banana", "cherry"}
del this_set
print(this_set)
'''
print("--------------------------------")
print("")




# Joining Sets: NOT INCLUDING DUPLICATES
# union() returns a new set containing all items from both sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(f"Union Set: {set3}")

print()
# update() method inserts all the items from one set into another:
set1 = {"x", "y", "z"}
set2 = {7, 8, 9}

set1.update(set2)
print(f"Update Set: {set1}")
print()

# intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)

print(f"Intersection Update: {x}")                      # will only print out 'apple' since it's present in sets x and y
print()
# intersection() method will return a new set, that only contains the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(f"Intersection: {z}")                             # will only print out 'apple' since it's present in sets x and y
print()

# symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)

print(f"Symmetric Difference Update: {x}")              # will print out items that are NOT in both sets
print()

# symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets
x = {"apple", "knife", "spoon"}
y = {"gun", "airsoft", "apple"}

z = x.symmetric_difference(y)

print(f"Symmetric Difference: {z}")                    # will print out items that are NOT in both sets
print()

# The values True and 1 are considered the same value in sets, and are treated as duplicates:
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}
z = x.symmetric_difference(y)

print(z)

print("--------------------------------")

# add()	                            Adds an element to the set
# clear()	                        Removes all the elements from the set
# copy()	                        Returns a copy of the set
# difference()	                    Returns a set containing the difference between two or more sets
# difference_update()	            Removes the items in this set that are also included in another, specified set
# discard()	                        Remove the specified item
# intersection()	                Returns a set, that is the intersection of two other sets
# intersection_update()	            Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	                    Returns whether two sets have a intersection or not
# issubset()	                    Returns whether another set contains this set or not
# issuperset()	                    Returns whether this set contains another set or not
# pop()	                            Removes an element from the set
# remove()	                        Removes the specified element
# symmetric_difference()	        Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	    inserts the symmetric differences from this set and another
# union()	                        Return a set containing the union of sets
# update()	                        Update the set with the union of this set and others

# It is also possible to use the set() constructor to make a set.
set = set(("apple", "banana", "cherry")) # note the double round-brackets
print(set)
