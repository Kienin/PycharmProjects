# LIST = used to store multiple items in a single variable

food = ["pizza", "hamburger", "hotdog", "spaghetti"]
print(food)
print(food[1])                                      # elements can be called out using index (starting from 0) in brackets

food[3] = "sushi"
print(food)
print(food[3])

for x in food:
    print(x)

print("--------------------------------")

    # Functions for list:
food.append("chips")                                # .append adds another element to the list
print(food)
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





# TUPLES = a collection which is ordered and unchangeable used to group together related data

    # Student Record:
student = ("Kevin", 18, "male")

print(student.count("Kevin"))                         # .count counts how many times () shows
print(student.index("male"))                          # .index counts which index is () at

for i in  student:
    print(i)

if "Kevin" in student:
    print("Kevin is here")

print("--------------------------------")





# SET = collection which is unordered, unindexed. No duplicate values.

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






# DICTIONARIES = a changeable, unordered collection of unique key; value pairs.
            #  = Fast because they are HASHING, allows us to access a value quickly

Capitals = {"USA": "Washington DC",
            "Philippines": "Manila",
            "India": "New Deli",
            "China": "Beijing"}

print(Capitals["Philippines"])
print(Capitals.get("Germany"))      # Get Method: check and see if something is in dictionary- won't crash

print("--------------------------------")

    # Dictionary Methods:
print(Capitals.keys())                # .keys prints all keys but not values
print(Capitals.values())              # .values prints all values but not keys
print(Capitals.items())               # .items prints entire dictionary

for key,value in Capitals.items():    # prints out entire dictionary in pairs
    print(key, value)

Capitals.update({"Germany": "Berlin"})    # .update adds a new key value pair
for key,value in Capitals.items():
    print(key, value)

Capitals.update({"USA": "Illinois"})      # .update can also change an existing pair
for key,value in Capitals.items():
    print(key, value)

Capitals.pop("China")                     # .pop removes a pair
Capitals.clear()                          # .clear, clears the dictionary

print("--------------------------------")





# INDEX OPERATOR [] = gives access to a sequence's element (str,list,tuples)

name = "kevin Dacanay!"

if (name[0].islower()):                   # [].islower() checks if index 0 is lower case
    name = name.capitalize()
print(name)

first_name = name[:5].upper()            # indexing till index 5 to capitalize
print(first_name)

last_name = name[6:].lower()             # indexing starting at index 6 to lower case
print(last_name)

last_character = name[-1]                # negative indexing printing out the last character
print(last_character)

print("--------------------------------")
