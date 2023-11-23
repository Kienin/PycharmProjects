# INHERITANCE: children class inherits attributes and methods of the parent class

# Parent Class:
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("Hello there")
# Children Classes:
# class Children_Class(Parent_Class): inherits the attributes of the parent class

class Cat(Pet):
    def __init__(self, name, age, color):
        # super() function used to give access to the methods of a parent class
        super().__init__(name, age)
        self.color = color
    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I'm {self.color}")
class Dog(Pet):
    def speak(self):
        print("Bark")


pet = Pet("Kevin", 18)
pet.show()
pet.speak()

cat = Cat("Hermoine", 3, "brown")
cat.show()
cat.speak()

dog = Dog("Bubs", 2)
dog.show()
dog.speak()