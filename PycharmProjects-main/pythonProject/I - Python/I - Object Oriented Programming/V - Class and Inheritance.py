# INHERITANCE = classes can inherit attributes or methods from another class

class Animal:
    # Attributes:
    alive = True

    # Methods:
    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")

# Separate classes from different animals:
class Rabbit(Animal):                             # Rabbit class will have acess to Animal class' attributes and methods
    def run(self):
        print("This rabbit is running")
class Fish(Animal):                             # Fish class will have acess to Animal class' attributes and methods
    def swim(self):
        print("This rabbit is swimming")
class Hawk(Animal):                             # Hawk class will have acess to Animal class' attributes and methods
    def fly(self):
        print("This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()
hawk.fly()

print("--------------------------------")





# MULTI-LEVEL INHERITANCE = when a derived (child) class inherits another derived (child) class

    # 3 level hierachy of classes (family tree)
class Organism:                                                             # Parent class
    alive = True

class Animal(Organism):                                     # Child class that has inherited ORGANISM
    def eat(self):
        print("This animal is eating")

class Dog(Animal):                                          # Child class that has inherited ANIMAL
    def bark(self):
        print("This dog is barking")

dog = Dog()                                                 # Dog has attributes and methods of both Animal and Organism
print(dog.alive)
dog.eat()
dog.bark()

print("--------------------------------")






# MULTIPLE INHERITANCE = when a child class is derived from more than one parent class
class Prey:
    def flee(self):
        print("This animal flees")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey,Predator):                                  # Fish inherits both Prey and Predator classes
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()                                                 # Fish can flee and hunt
fish.hunt()

print("--------------------------------")






# METHOD OVERRIDING = ability to allow a child class a specific implementation of a method that's already provided
class Animal:
    def eat(self):
        print("This animal eats")
class Rabbit(Animal):

    # def eat(self) IN RABBIT class overrides def eat(self) IN ANIMAL class
    def eat(self):
        print("This rabbit is eating a carrot")                # a more specific method ("This rabbit") for rabbit class

rabbit = Rabbit()
rabbit.eat()

print("--------------------------------")






# METHOD CHAINING = call multiple methods sequentially; each call perfroms an action on the same object and returns self
class Car:
    def turn_on(self):
        print("You start the engine")
        return self                                                              # return self to allow method chaining

    def drive(self):
        print("You are driving this car")
        return self                                                              # return self to allow method chaining

    def brake(self):
        print("You are braking")
        return self                                                              # return self to allow method chaining

    def turn_off(self):
        print("You turn off the engine")
        return self                                                              # return self to allow method chaining

car = Car()                                                                      # car = Car() turns car into object Car
car.turn_on().drive()                                                            # sequentially turn on then drives car
car.brake().turn_off()
(car.turn_on()
 .drive()
 .brake()
 .turn_off())

print("--------------------------------")





# SUPER() = function used to give access to the methods of a parent class
#           returns a temporary object of a parent class when used.
class Rectangle:
    def __init__(self, length, width):                       # __init__ lets the class initialize the object's attributes
        self.length = length
        self.width = width
class Square(Rectangle):
    def __init__(self, length, width):                       # __init__ lets the class initialize the object's attributes
        super().__init__(length, width)                       # super() gives access from rectangle class

    def area(self):
        return self.length * self.width
class Cube(Rectangle):
    def __init__(self, length, width, height):
       super().__init__(length, width)
       self.height = height

    def volume(self):
        return self.length * self.width * self.height

square = Square(3, 3)
cube = Cube(3,3,3)

print("The area of the square is:", square.area())
print("The volume of the cube is:", cube.volume())

print("--------------------------------")






# ABSTRACT CLASSES = a class which containts one or more abstract methods.
#                    prevents a user from creating an object of that class (i.e. an idea)
#                    compels users to override abstract methods in a child class
# ABSTRACT METHOD = a method that has declaration but does not have an implementation

from abc import ABC, abstractmethod                           # import abstractmethod from abstract class
class Vehicle(ABC):                                           # Vehicle will inherit from ABC class
    @abstractmethod                                           # @abstractmethod is decorator
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car")
    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")
    def stop(self):
            print("This motorcycle is stopped")

#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()

print("--------------------------------")
