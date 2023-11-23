class Person:
    number_of_people = 0

    # Class Attribute: def __init__(self):
    def __init__(self, name):
        self.name = name
        # everytime we instantiate Person, number of people goes up by 1
        Person.add_person()

    # Class Methods: def x(self):
    @classmethod
    # @classmethod decorator used to declare a method in class as a class method that can be called using ClassName.
    def number_of_peoples(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("Kevin")
#print(Person.number_of_people)
p2 = Person("Jasmine")
#print(Person.number_of_people)

print("Pesons added:", Person.number_of_peoples())

