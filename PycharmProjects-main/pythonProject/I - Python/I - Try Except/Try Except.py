# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

print("Exception Error:")
try:
  print(x)
except:
  print("An exception occurred")

#----------------------------------------

print('\nNameError:')
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

#----------------------------------------

print("\nElse")
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

#----------------------------------------

print('\nFinally:')
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

#----------------------------------------

# Raise an Exception:
print('\nRaise (an exception):')
x = -1
if x < 0:
    raise Exception('Sorry, no numbers below zero')

# Raise a specific kind of error:
y = 'hello'
if not type(y) is int:
    raise TypeError("Sorry, only integers allowed")