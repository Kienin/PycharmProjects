# Multiple Classes in Object-Oriented Programming:

# define class:
class Student:

    # define attributes:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    # define methods:
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            # Return True if student is added successfully, False if not
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value/len(self.students)


student_1 = Student("Kevin", 19, 100)
student_2 = Student("Jasmine", 18, 98)
student_3 = Student("Ben", 17, 69)

course = Course("I - Computer Science", 2)
course.add_student(student_1)
course.add_student(student_3)
print(course.students[0].name)
print("The average grade of students in the class is:", course.get_average_grade())
