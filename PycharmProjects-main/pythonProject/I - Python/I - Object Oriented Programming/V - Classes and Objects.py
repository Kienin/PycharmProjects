# I - Python is an object-oriented programming language

# A Class is like an object constructor, or a "blueprint" for creating objects.

# create a Class using class keyword:
class MyClass:
  x = 5

# create Object in class
parent = MyClass()
print(parent.x)

print("__init__() function:")
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or
# other operations that are necessary to do when the object is being created:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

print()
print("__str__() Function:")
# The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

# The __str__() dunder method returns a reader-friendly string representation of a class object; Not the gibberish!
  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)
print()

# Object Methods:
print("Object Methods:")
# CLASS:
class Person:

  # ATTRIBUTE:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # METHOD:
  def myfunc(self):
    print("Hello my name is " + self.name)

# OBJECT:
p1 = Person("John", 36)
p1.myfunc()


# self parameter refers to the current instance of the class, and is used to access variables that belongs to the class
# self doesn't need to be named self; can be anything
class Person:
# self = mysillyobject
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

# self = abc
  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()


# Modifying Objects:
print("\nModifying Objects:")
p1.age = 40
print(p1.age)

# Deleting Objects:
print("\nDeleting Objects:")
del p1.age
#del p1
print(p1)