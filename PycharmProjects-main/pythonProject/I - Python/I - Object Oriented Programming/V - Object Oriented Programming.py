# OBJECT = an instance of a class; representations of an object by assigning attributes and methods
# CLASS = in order to create an object, class is needed.
# CLASS can function as a blueprint that will describe what attributes or methods an object will have

from OOP_Car import Car

# create an object with attributes:
car_1 = Car("Honda", "Accord", "2007", "Gray")
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()
car_1.stop()

car_2 = Car("Ford", "Mustang", "1960", "Black")
print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_2.drive()
car_2.stop()

print("--------------------------------")





# CLASS VARIABLES:
car_1 = Car("Honda", "Accord", "2007", "Gray")
car_2 = Car("Ford", "Mustang", "1960", "Black")
car_3 = Car("Harley-Davidson", "Fat Boy", "2023", "Jet Black")

car_3.wheels = 2
# Car.wheels = 2                                                                 will affect all instances of car class
# print(Car.wheels)                                                              will output 2
print(car_1.wheels)
print(car_2.wheels)
print(car_3.wheels)

print("--------------------------------")






# OBJECTS AS ARGUMENTS:
class Car:
    color = None
class Motorcycle:
    color = None
def change_color(vehicle, color):
    vehicle.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()


change_color(car_1, "red")
change_color(car_2, "white")
change_color(car_3, "blue")
change_color(bike_1, "black")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)

print("--------------------------------")






# DUCK TYPING = concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present

class Duck:
    def walk(self):
        print("This duck is walking")
    def talk(self):
        print("This duck is quacking")

class Chicken:
    def walk(self):
        print("This chicken is walking")
    def talk(self):
        print("This chicken is clucking")

class Person:
    def catch(self, duck):              # (self, duck )to pass duck argument.
        duck.walk()
        duck.talk()
        print("You caught the critter!")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
person.catch(chicken)                   # even though duck object is in parameter, it will still work with chicken class
                                        # since chicken and duck have the same attributes

print("--------------------------------")






# WALRUS OPERATOR ":=" = assignment expression (walrus) which assigns values to variables as part of a larger expression

happy = True
print(happy)

print(happy := True)

'''
foods = list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food)
'''

foods = list()
while food := input("What food do you like?: ") != "quit":              # functions the same as previous code
    foods.append(food)

print("--------------------------------")
