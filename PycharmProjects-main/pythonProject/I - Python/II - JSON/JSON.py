# JSON is a syntax for storing and exchanging data written in Javascript object notation
# Good for creating API

import json

# JSON Types: strings, numbers, Booleans, null, Arrays, Objects

# If you have JSON string, you can parse it using json.loads()
print("Parsing JSON:")
# example JSON:
x = '{"name":"Kevin", "age":"18", "city":"Bolingrbook"}'

# parse x:
y = json.loads(x)
print(y)
print(f"Name is: {(y['name'])}")


# If you have a Python object, you can convert it into JSON string by using json.dumps()
print("\nConverting Python String to JSON string:")
# example python object(dicionary):
x = {
    "name": "Jasmine",
    "age": "18",
    "gender": "female"
}

# convert into JSON:
y = json.dumps(x)
print(y)

print("\nConverting Python Objects into JSON:\nThese are the Javascript equivalent of Python objects")
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

'''
Python	    JSON
dict	    Object
list	    Array
tuple	    Array
str	        String
int	        Number
float	    Number
True	    true
False	    false
None	    null
'''

print("\nConverting Python Objects in one variable into JSON:")
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

# Indenting json.dumps()
print("\nIndexing json.dumps():")
print(json.dumps(x, indent=4))
print(json.dumps(x, indent=4, separators=(". ", " = ")))
print("\nSorting json.dumps():")
print(json.dumps(x, indent=4, sort_keys=True))