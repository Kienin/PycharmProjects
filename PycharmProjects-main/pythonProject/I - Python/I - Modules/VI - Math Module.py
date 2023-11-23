import math

pi = 3.14
x = 1
y = 2
z = 3

print(round(pi))       #round up to nearest whole integer
print(math.ceil(pi))   #round up another whole integer
print(math.floor(pi))  #round down another whole integer
print(abs(pi))         #gives the absolute value of number
print(pow(pi, 2))      #exponent; to the power of 2
print(math.sqrt(pi))   #gives square root of a number
print(max(x, y, z))      #finds the largest value
print(min(x, y, z))      #finds the smallest value

print("--------------------------------")



# ARITHMETIC

#Expressions:
print(10+5)   #addition
print(10-5)   #subtraction
print(10*5)   #multiplication
print(10/5)   #division
print(10//5)  #floor division - ignores the remainder
print(10%5)   #modulus - gives the remainder
print(10**5)  #exponent

x = 10
x += 5
print(x)

x -= 5
print(x)

c = 10
c = c/5
print(c)

z = 10 + 3 * 2
print(z)

print("--------------------------------")



#Comparison operators:
'''
== is equal to
!= is not equal to
< is less than
> is greater than
<= is less than or equal to
>= is greater than or equal to
'''

x = 3 >= 2
print(x)
x - 3 <= 2
print(x)
x = 3 == 2
print(x)
x = 3 == 3
print(x)
x = 3 != 3
print (x)
x = 3 != 2
print(x)

print("--------------------------------")




#Boolean Logic:
'''
and (both)
or (at least one is true)
not (neither; makes true to false and false to true)
'''
price = 25
print(price > 10)
print(price >= 10 and price < 30)
print(price >= 26 and price < 30)
print(not price > 10)


# Counter that increases by 1 everytime it's called:
def counter():
    global count
    if 'count' not in globals():
        count = 0
    count += 1
    return count