# IF STATEMENTS = a block of code that will execute if conditions are true

age = int(input("How old are you? "))

if age == 100:
    print("You've lived for way too long!")
elif age >100:
    print("You are about to die!")
elif age >= 18:
    print("You are an adult!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You are a child!")

# LOGICAL OPERATORS (and,or,not) = used to check if two or more conditional statements are met

temp = float(input("What is the temperature outside? "))

if temp >= 0 and temp <= 30:
    print("The temperature is good today!")
    print("Go outside!")
elif temp < 0 or temp > 30:
    print("The temperature is bad today!")
    print("Stay inside!")

    # NOT STATEMENT = flips true to false and false to true
temp = float(input("What is the temperature outside? "))

if not(temp >= 0 and temp <= 30):
    print("The temperature is good today!")
    print("Go outside!")
elif not(temp < 0 or temp > 30):
    print("The temperature is bad today!")
    print("Stay inside!")


# Weight converter(lbs/kgs) using if statements:
Weight = float(input("How much do you weigh? "))
Unit = input("(K)g or (L)bs? ")
if Unit.upper() == "K":
    converted = Weight / 0.45
    print("Your weight in Lbs is: ", str(converted))
if Unit.upper() == "L":
    converted = Weight * 0.45
    print("You weight in Kgs is: ", str(converted))






# CONDITIONAL EXPRESSIONS:
print("Conditional Expressions:")
user_val = int(input("Enter a number: "))
cond_str = "negative" if user_val < 0 else "nonnegative"
print(f'{user_val} is {cond_str}')


num_users = int(input("Enter a number: "))
update_direction = int(input("Enter another number: "))
num_users = num_users + 1 if update_direction == 3 else num_users - 1
print(f'New value is: {num_users}')

print("--------------------------------")


# Nested If
print("Nested If:")
x = int(input("Enter a number"))
if x >= 10:
    print("Above ten,")
    if x >= 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

print("--------------------------------")
print()

# Conditional and If Statements:

# Equals:                   a == b
# Not Equals:               a != b
# Less than:                a < b
# Less than or equal to:    a <= b
# Greater than:             a > b
# Greater than or equal to: a >= b


