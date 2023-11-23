# FUNCTION = a block of code which is executed when it's called

def hello():
    print("Hello!")
    print("Have a nice day!")
hello()

def hello(name):
    print("Hello " + name)
    print("Have a nice day!")
hello("Kevin")

my_name = "Dacanay"
hello(my_name)


def hello(first_name, last_name, age):                                      # 3 parameters for 3 arguements
    print("Hello",first_name,last_name,)
    print("You are", age,"years old.")
    print("Have a nice day!")
hello("Kevin","Dacanay", 21)

print("--------------------------------")





# RETURN STATEMENTS = used within functions to send I - Python values/objects back to the caller.
                    # These values/objects are known as the function's return value

def multiply(number1,number2):
    result = number1 * number2
    return result

print(multiply(6,6))

x = multiply(6,8)
print(x)

def divide(number1,number2):
    return number1 / number2

print(divide(36,6))

print("--------------------------------")






# KEYWORD ARGUEMENTS = agruements preceded by an identifier when we pass them to a function.
                     # The order of the arguments doesn't matter, unlike positional arguments
                     # I - Python knows the names of the argument that our function recieves

    # Positional Arguement- where order matters:
def hello(first,middle,last):
    print("Hello",first,middle,last)

hello("Kevin", "Brian", "Dacanay")

    # Keyword Arguement - where order doesn't matter
def hello(first,middle,last):
    print("Hello",first,middle,last)

hello(last="Kevin", middle="Brian", first="Dacanay")

print("--------------------------------")





# NESTED FUNCTION CALLS = function calls inside another function calls
                        # innermost function calls are resolved first
                        # returned value is used as argument for the next other function

num = input("Enter a whole positive number ")
num = float(num)
num = abs(num)                                    # abs = absolute value
num = round(num)
print(num)

    # Nested Function: reads from right to left
print(round(abs(float(input("Enter a whole positive number: ")))))

print("--------------------------------")





# SCOPE = the region that a variable is recognized; a variable is only available from inside the region it's created
       # a global and locally scoped versions of a variable can be created

    #Local Scope (since it's inside of a function):
def display_name():
    name = "Kevin"
    print(name)

display_name()

    #Global Scope (available inside and outside of functions):
name = "Mister"
def display_nickname():
    name = "Kevin"
    print(name)

display_nickname()
print(name)

print("--------------------------------")






# *ARGS = parameter that will pack all argumnets into a tuple
#         useful so that function can accept varying amounts of arguments

def add(*args):                                    # (*args):can be anything; lets you input more argumnts in a function
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3))

def add(*stuff):                                   # (*args):can be anything; lets you input more argumnts in a function
    sum = 0
    stuff = list(stuff)                            # To change one of the values within the tuple since list() are changeable
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum

print(add(1,2,3,4,5,6))

print("--------------------------------")





# **KWARGS = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept varying amount of keyword arguments

def hello(**kwargs):
  # print("Hello", kwargs['first'],"", kwargs['last'])
    print("Hello", end=" ")
    for key,value in kwargs.items():                              # in kwargs.items(): puts the arguements into a dictionary
        print(value, end=" ")

hello(title="Mr", first="Kevin", middle="Brian", last="Dacanay", race="is Filipino") # you can add more **kwargs

print("\n--------------------------------")






# FUNCTIONS TO VARIABLES:
def hello():
    print("Hello")

print(hello)                                                      # will print the memory address of the function in hex
hi = hello                                                        # assign that address to a variable
print(hi)

hi = hello
hi()                                                              # hi() calls the hello() function

say = print                                                       # say and print() has the same memory adress now...
say("Whoa I am printing even though I'm not using print()")       # say() will work the same was as print()

print("--------------------------------")






# HIGH ORDER FUCNTIONS = a function that either: 1. accepts a function as an argument, or 2. returns a function
#                        in I - Python, functions are treated as objects

# Example 1: accepts a function as an argument
def loud(text):
    return text.upper()
def quiet(text):
    return text.lower()
def hello(func):                    # the higher order function; func = either loud or quiet func can be passed
    text = func("Hello")
    print(text)

hello(loud)                         # typing in the name of the higher order func then passing a function as an argument
hello(quiet)

# Example 2: returns a function
def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)                 # assigns 2 to divisor; y = 10 and x = 2
print(divide(10))                   # assigns 10 to dividend(x)

print("--------------------------------")

# Counter Function: increases by 1 everytime the function is called
def counter():
    global count
    if 'count' not in globals():
        count = 0
    count += 1
    return count
