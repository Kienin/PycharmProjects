# VARIABLES = a container for a value of different data types.

#Strings:
name = "Kevin"
last_name = 'Dacanay'
full_name = name + " " + last_name
print("Hello", full_name)

print(type(name))

# check string
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
print("--------------------------------")

# STRING.FORMAT() = gives more control when displaying output

animal = "cow"
item = "moon"
# print("The", animal, "jumped over the ", item)
print("The {} jumped over the {}".format(animal,item))
print("The {1} jumped over the {0}".format(animal,item))                          # positional argument
print("The {animal} jumped over the {item}".format(animal="dog",item="table"))          # keyword argument

text = "The {} jumped over the {}"
print(text.format(animal, item))

name = "Kevin"
print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))                     # {:N} to create padding/space
print("Hello, my name is {:<10}. Nice to meet you".format(name))                    # {:<N} to create padding/space
print("Hello, my name is {:>10}. Nice to meet you".format(name))                    # {:>N} to create padding/space
print("Hello, my name is {:^10}. Nice to meet you".format(name))                    # {:N} to create center padding/space


number = 3.14159

print("The number pi is {:.2f}".format(number))                                     # {:.2f(float)} displays only the first two digits after decimal
print("The number pi is {:.3f}".format(number))                                     # {:.3f(float)} displays only the first three digits after decimal

number = 1000

print("The number is {:,}".format(number))                                          # {:,} adds a comma all one thousandths place value
print("The number is {:b}".format(number))                                          # {:b(binary)} changes number into binary
print("The number is {:o}".format(number))                                          # {:o(octal)} changes number into binary
print("The number is {:x}".format(number))                                          # {:x/X(Hexadeciaml)} changes number into hexadecimals
print("The number is {:E}".format(number))                                          # {:e/E(Scientific notaion)} changes number into scientific notation

print("--------------------------------")

# remove white space:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# split string
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

print("--------------------------------")

# STRING FORMAT METHOD:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# or
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
print("--------------------------------")

'''
ESCAPE CHARACTERS:
\\'	Single Quote	
\\	Backslash	
\\n	New Line	
\\r	Carriage Return	
\\t	Tab	
\\b	Backspace	
\\f	Form Feed	
\ooo	Octal value	
\\xhh	Hex value	


STRING METHODS: 
Method	Description
capitalize()	Converts the first character to upper case
casefold()	    Converts string into lower case
center()	    Returns a centered string
count()	        Returns the number of times a specified value occurs in a string
encode()	    Returns an encoded version of the string
endswith()	    Returns true if the string ends with the specified value
expandtabs()    Sets the tab size of the string
find()	        Searches the string for a specified value and returns the position of where it was found
format()	    Formats specified values in a string
format_map()	Formats specified values in a string
index()	        Searches the string for a specified value and returns the position of where it was found
isalnum()	    Returns True if all characters in the string are alphanumeric
isalpha()	    Returns True if all characters in the string are in the alphabet
isascii()	    Returns True if all characters in the string are ascii characters
isdecimal()	    Returns True if all characters in the string are decimals
isdigit()	    Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	    Returns True if all characters in the string are lower case
isnumeric()	    Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	    Returns True if all characters in the string are whitespaces
istitle()	    Returns True if the string follows the rules of a title
isupper()	    Returns True if all characters in the string are upper case
join()	        Joins the elements of an iterable to the end of the string
ljust()	        Returns a left justified version of the string
lower()	        Converts a string into lower case
lstrip()	    Returns a left trim version of the string
maketrans()	    Returns a translation table to be used in translations
partition()	    Returns a tuple where the string is parted into three parts
replace()	    Returns a string where a specified value is replaced with a specified value
rfind()	        Searches the string for a specified value and returns the last position of where it was found
rindex()	    Searches the string for a specified value and returns the last position of where it was found
rjust()	        Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	    Splits the string at the specified separator, and returns a list
rstrip()	    Returns a right trim version of the string
split()	        Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	        Returns a trimmed version of the string
swapcase()	    Swaps cases, lower case becomes upper case and vice versa
title()	        Converts the first character of each word to upper case
translate()	    Returns a translated string
upper()	        Converts a string into upper case
zfill()	        Fills the string with a specified number of 0 values at the beginning
'''
# ARITHMETIC OPERATORS:
'''
+	Addition	        x + y	
-	Subtraction	        x - y	
*	Multiplication	    x * y	
/	Division	        x / y	
%	Modulus	            x % y	
**	Exponentiation	    x ** y	
//	Floor division	    x // y
'''

# ASSIGNMENT OPERATORS:
'''
=	    x = 5       x = 5	
+=	    x += 3	    x = x + 3	
-=	    x -= 3	    x = x - 3	
*=	    x *= 3	    x = x * 3	
/=	    x /= 3	    x = x / 3	
%=	    x %= 3	    x = x % 3	
//=	    x //= 3	    x = x // 3	
**=	    x **= 3	    x = x ** 3	
&=	    x &= 3	    x = x & 3	
|=	    x |= 3	    x = x | 3	
^=	    x ^= 3	    x = x ^ 3	
>>=	    x >>= 3	    x = x >> 3	
<<=	    x <<= 3	    x = x << 3
'''
# COMPARISON OPERATORS:
'''
==	Equal	                    x == y	
!=	Not equal	                x != y	
>	Greater than	            x > y	
<	Less than	                x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	    x <= y
'''
# BITWISE(BINARY) OPERATORS:
'''
& 	AND	    Sets each bit to 1 if both bits are 1	                                                                            x & y	
|	OR	    Sets each bit to 1 if one of two bits is 1	                                                                        x | y	
^	XOR	    Sets each bit to 1 if only one of two bits is 1	                                                                    x ^ y	
~	NOT	    Inverts all the bits	                                                                                            ~x	
<<	Zero    fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	                x << 2	
>>	Signed  right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off x >> 2
'''
'''
Operator	Description	
()	        Parentheses	
**	        Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	    Addition and subtraction	
<<  >>	    Bitwise left and right shifts	
&	        Bitwise AND	
^	        Bitwise XOR	
|	        Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	        NOT	
and	        AND	
or	        OR
'''

#Integer:
age = 18
age = age + 1
age += 1
print(age)
print("Your are " + str(age) + " years old.")

print(type(age))

print("--------------------------------")

#Float:
height = 250.5
print("your height is " + str(height) + " cm.")
print(type(height))

print("--------------------------------")





#Boolean (True or False):
human = True
print(human)
print("Are you a human:", str(human))
print(type(human))

# almost all booleans are TRUE except empty ones or 0:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a
# class with a __len__ function that returns 0 or False:
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# Functions can also return booleans:
def myFunction() :
  return True

print(myFunction())
if myFunction():
  print("YES!")
else:
  print("NO!")

# can determine if a value is a certain type
x = 200
print(isinstance(x, int))
print("--------------------------------")





# MULTIPLE ASSIGNMENT = allows us to assign multiple variables at the same time in one line of code.

name, age, attractive = "Kevin", 18, True
print(name)
print(age)
print(attractive)

Spongebob = Patrick = Sandy = Squidward = 30
print(Spongebob)
print(Patrick)
print(Sandy)
print(Squidward)

print("--------------------------------")





#String Methods:

name = "kevin"

print(len(name)) #How long the string is
print(name.find("k")) #Find the first index of where a character is
print(name.capitalize()) #Capitalize the first letter
print(name.upper()) #All upper cases
print(name.lower()) #All lower cases
print(name.isdigit()) #Returns true or false is string is a digit
print(name.isalpha()) #Returns true or false is string is alphabetical
print(name.count("i")) #Count how many chacarters are in the string
print(name.replace("i","a")) #Replace certain characters with new characters
print(name*3)

print("--------------------------------")





# TYPE CASTING : convert the data type of a value to another data type.

x = 1    #integer
y = 2.0  #float
z = "3"  #string

y = int(y) #permanent change

print(float(x))
print(int(y))
print(int(z))

print("Y is " + str(y))

print("--------------------------------")





# RANDOM NUMBERS:
import random

x = random.randint(1, 10)                  # random.randint(a,b) generates random numbers within num a and num b
y = random.random()                              # random.random() generates random floats

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)                        # random.choice() generates random choice from list

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]
random.shuffle(cards)                            # random.shuffle() shuffles a list

print(x)
print(y)
print(z)
print(cards)

