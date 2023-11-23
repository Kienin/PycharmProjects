# An iterator is an object that contains a countable number of values.

# iter() method  is used to get an iterator:
my_tuple = ("apple", "banana", "cherry")
myit = iter(my_tuple)

print(next(myit))
print(next(myit))
print(next(myit))

print()
my_str = "banana"
myit = iter(my_str)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

print("\n-----------------------------------------")
print("__iter__() and __next__() functions:")
# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

# As you have learned in the I - Python Classes/Objects chapter, all classes have a function called __init__(),
# which allows you to do some initializing when the object is being created.

# The __iter__() method acts similar, you can do operations but must always return the iterator object itself.

# The __next__() method also allows you to do operations, and must return the next item in the sequence.

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


print("\n-----------------------------------------")
print("StopIteration Statement:")

# To prevent the iteration from going on forever, we can use the StopIteration statement.
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

