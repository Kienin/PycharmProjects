# FOR LOOPS: used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

print("For Loops:")
print("Looping through Iterables:")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print()
print("Looping through Strings:")
for x in "banana":
  print(x)

print("----------------------")
print()

# Break Statements: can stop the loop before it has looped through all the items:
fruits = ["apple", "banana", "cherry"]
print("List: ", fruits)

print("Break Statement:")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

print()
# Continue Statements: can stop the current iteration of the loop, and continue with the next:
print("Continue Statement:")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

print("----------------------")
print()
print("Range() Function: ")
# Range() Function: to loop through a set of code a specified number of times
for x in range(11):
  print(x)

print()
print("From a specified beginning and end:")
for x in range(2, 6):
  print(x)

print()
print("From a specified beginning and end that skips 2")
for x in range(2, 30, 2):
  print(x)

print("----------------------")
print()
print("Else Statements:")
for x in range(6):
  print(x)
else:
  print("Finally finished!")

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

print("----------------------")
print()
print("Nested Loops:")
# The "inner loop" will be executed one time for each iteration of the "outer loop":
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
    