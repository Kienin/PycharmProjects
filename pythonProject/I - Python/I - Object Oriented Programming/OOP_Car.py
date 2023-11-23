class Car:
# CLASS VARIABLES: declared inside the class and outside of the constructor

    wheels = 4                                               # class variable

# Special Method: (constructor) assigns arguments to the attributes
    def __init__(self, make, model, year, color):            # self refers to the object we're working on
        self.make = make                                     # instance variable
        self.model = model                                   # instance variable
        self.year = year                                     # instance variable
        self.color = color                                   # instance variable
                                                         # each object can have their own unique values assigned to each

# Methods:
    def drive(self):
        print("This "+self.model+" is driving")
    def stop(self):
        print("This "+self.model+" is stopped")