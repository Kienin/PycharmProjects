# DICTIONARIES = a changeable, ordered collection of unique key; value pairs.
#                Fast because they are HASHING, allows us to access a value quickly
#                Dictionary is a collection which is ordered** and changeable. No duplicate members.

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
print()

# Method	    Description
# clear()	    Removes all the elements from the dictionary
# copy()	    Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	        Returns the value of the specified key
# items()	    Returns a list containing a tuple for each key value pair
# keys()	    Returns a list containing the dictionary's keys
# pop()	        Removes the element with the specified key
# popitem() 	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key doesn't exist: insert the key with the specified value
# update()	    Updates the dictionary with the specified key-value pairs
# values()	    Returns a list of all the values in the dictionary

# It is also possible to use the dict() constructor to make a dictionary.
# dict = dict(name = "John", age = 36, country = "Norway")
# print(dict)

# Duplicates are NOT allowed
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2020,
  "year": 1964
}
print(dict)
print(f"The brand is: {dict['brand']}")

# Length of Dictionary:
print(f"The length of this dictionary is: {len(dict)}")

print("--------------------------------")
print()

# Accessing Dictionary Items:
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(f"The year for this car is: {dict['year']}")

# get() will give the same result:
print(dict.get("model"))
print(f"The model of this car is: {dict.get('model')}")

print("--------------------------------")
print()


# KEYS:
print("Adding Keys in Dictionary:")
print(dict.keys())

# Adding keys:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x)                    # before the change

car["color"] = "white"      # new key, value pair
print(x)                    # after the change
print()

# VALUES:
print("Adding Values in Dictionary:")
print(dict.values())

# Adding values:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()
print(x)                    # before the change

car["year"] = 2020
car["color"] = "red"
print(x)                    # after the change
print()

# ITEMS (key, value pair):
print(dict.items())
print()

# Checking if Key exists:
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in dict:
  print("Yes, 'model' is one of the keys in the dict dictionary")

print("--------------------------------")
print()


# Changing Dictionary Items:
print("Changing Items in Dictionary:")

dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
dict['year'] = 2023
print(dict)

# update() method will update the dictionary with the items from the given argument.
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
this_dict.update({"year": 2020})
print(this_dict)

dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict.update({"color": "red"})
print(dict)

print("--------------------------------")
print()


# Removing Dictionary Items:
print("Removing Items in Dictionary:")

# pop() method removes the item with the specified key name:
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
this_dict.pop("model")
print(this_dict)

# popitem() method removes the last inserted item
this_dict.popitem()
print(this_dict)

# del keyword removes the item with the specified key name OR the whole dictionary:
del this_dict["brand"]
print(f"Del: {this_dict}")

# del this_dict
# print(this_dict)

# clear() method empties the dictionary:
this_dict.clear()
print(f"Clear(): {this_dict}")

print("--------------------------------")
print()

# Looping Dictionaries:
print("Looping through Dictionaries:")
for x in dict:
  print(x)
print()

print("Keys():")

for x in dict.keys():
  print(x)

print()
print("Values():")
# values() method to return values of a dictionary:
for x in dict.values():
  print(x)

print()
print("Items():")
for x, y in dict.items():
  print(x,":", )

print("--------------------------------")
print()

# Copying Dictionaries:
print("Copying Dictionaries:")

# copy() method makes a copy of a dictionary
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = this_dict.copy()
print(mydict)

# it is also possible to create/copy another dictionary using dict() constructor
this_dict = {
   "brand": "Ford",
   "model": "Mustang",
   "year": 1964
 }
mydict = dict(this_dict)
print(mydict)


print("--------------------------------")
print()

# Nested Dictionaries:

family = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(f"Nested Dictionary: {family}")

# Or,we can add three dictionaries into a new dictionary:
child1 = {
  "name" : "Kevin",
  "year" : 2004
}
child2 = {
  "name" : "Kyle",
  "year" : 2001
}
child3 = {
  "name" : "Ken",
  "year" : 2015
}

my_family = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(f"Adding Dictionaries: {my_family}")

# Access Items in Nested Dictionaries:
print(f"Child1's name is: {my_family['child1']['name']}")
print(f"Child1's year is: {my_family['child1']['year']}")