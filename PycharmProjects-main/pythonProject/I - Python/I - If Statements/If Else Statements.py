# PYTHON CONDITIONAL STATEMENTS:

'''
LOGICAL OPERATORS:
Equals:                     a == b
Not Equals:                 a != b
Less than:                  a < b
Less than or equal to:      a <= b
Greater than:               a > b
Greater than or equal to:   a >= b
'''

# IF:
a = 33
b = 200
if b > a:
    print(f"{b} is greater than {a}")

# ELIF:
b = 33
if b > a:
  print(f"{b} is greater than {a}")
elif a == b:
  print(f"{a} and {b} are equal")

# ELSE:
a = 200
b = 33
if b > a:
  print(f"{b} is greater than {a}")
elif a == b:
  print(f"{a} and {b} are equal")
else:
  print(f"{a} is greater than {b}")


# Short Hand If Else:
print("Short Hand If Else:")
a = 2
b = 330
print("A") if a > b else print("B")
print("A") if a > b else print("=") if a == b else print("B")
print()

print("-----------------------------------")
print()

print("Logical Operators:")
# And: a logical operator, and is used to combine conditional statements
print("And:")
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
print()

# Or: a logical operator, and is used to combine conditional statements
print("Or:")
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
print()

# Not: a logical operator, and is used to reverse the result of the conditional statement
print("Not:")
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
print()

# Nested if:
print("Nested If:")
x = 11

if x > 10:
  print(f"x({x}) is above 10,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


# Pass Statement: if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error
a = 33
b = 200

if b > a:
  pass