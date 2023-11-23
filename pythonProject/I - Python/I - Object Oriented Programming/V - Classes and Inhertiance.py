# INHERITANCE: allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

# Student class will inherit attributes and methods of Person class
class Student(Person):
  pass

student1 = Student("Kevin", "Dacanay")
student1.printname()

print()
# __init__() function overrides inheritance:
class Student(Person):
  def __init__(self, fname, lname):
      self.fname = fname
      self.lname = lname


print()
# super() function will make the child class inherit all the methods and properties from its parent
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()

