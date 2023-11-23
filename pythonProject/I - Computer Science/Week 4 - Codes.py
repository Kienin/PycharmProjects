x = input("Please enter r, p, or s: ")
if x == "r":
    print("You entered Rock")
elif x == "p":
    print("You entered Paper")
else:
    print("You entered Scissors")

# -----------------------------
# indentation is important

num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")

# ---------------------
# Nested If; https: // www.w3schools.com / python / gloss_python_if_nested.asp

x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

#---------------------------
# Assigning a letter grade

grade = int(input("Enter a number between 0 - 100: "))
if grade >= 90:
    print('you got a A')
elif grade >= 80:
    print('you got a B')
elif grade >= 70:
    print('you got a C')
elif grade >= 60:
    print('you got a D')
else:
    print('you got a F')

# ----------------------------
grade = int(input("Enter a number between 0 - 100: "))
if grade <= 60:
    print('you got a F')
elif grade <= 70:
    print('you got a D')
elif grade <= 80:
    print('you got a C')
elif grade <= 90:
    print('you got a B')
else:
    print('you got a A')

#--------------------------------
# How is this code different from above? Logical operator: use lower case, CAPITAL errors out

grade = int(input("Enter a number between 0 - 100: "))
if grade >= 90 and grade <= 100:
    print('you got a A')
if grade >= 80 and grade < 90:
    print('you got a B')
if grade >= 70 and grade < 80:
    print('you got a C')
if grade >= 60 and grade < 70:
    print('you got a D')
if grade < 60:
    print('you got a F')

#-------------------------
# Grade calculator Little bit different.You will need to modify - formatting,  # of exams, program, etc. IPO

name = input('enter Name: ')

exam1 = int(input('enter exam 1 score 0-100: '))
exam2 = int(input('enter exam 2 score 0-100: '))

p1 = int(input('enter programing score1 0-10: '))
p2 = int(input('enter programing score2 0-10: '))
p3 = int(input('enter programing score3 0-10: '))

exam_average = (exam1 + exam2) / 2
program_average = (p1 + p2 + p3) / 3
grade = (0.6 * exam_average) + (0.4 * 10 * program_average)

print(name)
print('Your average exam score is', exam_average)
print('Your average programing score is ', program_average)
print('your overall grade is: ', grade)

# Think about the logic below
if grade >= 90:
    print('you got a A')
elif grade >= 80:
    print('you got a B')
elif grade >= 70:
    print('you got a C')
elif grade >= 60:
    print('you got a D')
else:
    print('you got a F')




# CONDITIONAL EXPRESSIONS:
user_val = int(input())
cond_str = "negative" if user_val < 0 else "nonnegative"
print(f'{user_val} is {cond_str}')


num_users = int(input())
update_direction = int(input())
num_users = num_users + 1 if update_direction == 3 else num_users - 1
print(f'New value is: {num_users}')

import this
