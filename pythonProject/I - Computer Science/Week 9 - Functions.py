# Week 9 function code
# program 1 - say hello
def Hello():
    print("Hello from a function")

Hello()
print("====================")

# program 2 - play RPS once with function
def RPS():
    import random
    print('welcome to RPS')
    user_choice = input('You go first. Enter your choice: r, p, s ')
    print('You chose', user_choice)

    list_choices = ['r', 'p', 's']
    computer_choice = random.choice(list_choices)
    print('Computer chose', computer_choice)

    if user_choice == computer_choice:
        print('It is a draw. We both chose', user_choice)
    elif user_choice == 'r' and computer_choice == 's':
        print('You win. You chose rock. Computer chose scissor')
    elif user_choice == 'r' and computer_choice == 'p':
        print('You lose. You chose rock. Computer chose paper')
    elif user_choice == 'p' and computer_choice == 's':
        print('You lose. You chose paper. Computer chose scissor')
    elif user_choice == 'p' and computer_choice == 'r':
        print('You win. You chose paper. Computer chose rock')
    elif user_choice == 's' and computer_choice == 'p':
        print('You win. You chose scissor. Computer chose paper')
    elif user_choice == 's' and computer_choice == 'r':
        print('You lose. You chose scissor. Computer chose rock')
    print("thank you for playing")

RPS()

print("====================")

# Program 3 - single argument
def function_name(Name):
    print("Hello ", Name)


print("Enter your first name: ")
Name = input()
function_name(Name)

print("====================")

# program 4 - multiple arguments with same names
def Name(first_Name, last_Name):
    print("Hello ", first_Name, last_Name)


print("Enter your first name: ")
first_Name = input()
print("Enter your last name: ")
last_Name = input()
Name(first_Name, last_Name)

print("====================")
# program 5 - multiple arguments with different names
def function_Name(animal, vacation):
    print("Hello ", animal, vacation)


print("What animal do you like the best? ")
animal = input()
print("Where do you want to vacation? ")
vacation = input()
function_Name(animal, vacation)

print("====================")

# program 6  - multiple arguments with different ORDER
def vacay_animal(vacation, animal):
    print("Hello ", animal, vacation)


print("What animal do you like the best? ")
animal = input()
print("Where do you want to vacation? ")
vacation = input()
vacay_animal(animal, vacation)

print("====================")
