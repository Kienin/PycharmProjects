# Creating Classes:

class Dog:                                                               # class is a code template for creating objects
                                                                         # class Dog: is the __main__ module
    def __init__(self, name, age):                                       # __init__ instantiates when object is created
        self.name = name
        self.age = age

# def x(self) are methods:
    def bark(self):
        print("barking")

    def sit(self):
        print("sitting")

    def sleep(self):
        return "sleeping"

    def eat(self, treats):
        return f"eating {treats} treats"

    def get_name(self):
        return self.name                                 # return self.name to get the name of instantiated dog class

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

dog = Dog("Bubba", 1)                                       # Dog(name) is when __init__ is initiated and name is passed in

print(type(dog))
print()

# calling a method on an instance of the class Dog
print("Dog name is", dog.name)
dog.bark()
dog.sit()
print(dog.sleep())
print(dog.eat(2))


print()
# create another instance of the class Dog:
dog_2 = Dog("Tutoy", 2)

print("Second dog's name is", dog_2.name)

# get_name():
print()
print("Using get_name function:")
print("The name of the first dog is", dog.get_name())

# get_age():
print()
print("Using get_age function:")
print("The ages of the dogs are", dog.get_age(), "and", dog_2.get_age())

# set_age():
print()
print("Changing dog age using set_age function:")
print(f"{dog_2.name}'s age is {dog_2.age}.")

dog_2.set_age(69)
print(f"We are now changing {dog_2.name}'s age to {dog_2.get_age()}")