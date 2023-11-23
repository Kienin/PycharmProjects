# A variable is only available from inside the region it is created. This is called scope.

# Local Scope:
print("Local Scope:")
def myfunc():
  x = 300
  print(x)
myfunc()

print()
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()
myfunc()

print()

# Global Scope:
# A variable created in the main body of the I - Python code is a global variable and belongs to the global scope.

print("Global Scope:")

x = 300
def myfunc():
  print(x)
myfunc()
print(x)

# Global Keyword:
x = 300
def myfunc():
  global x
  x = 200
myfunc()
print(x)