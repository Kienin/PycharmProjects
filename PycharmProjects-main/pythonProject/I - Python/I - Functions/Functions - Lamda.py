# LAMBDA FUNCTION = function written in 1 line using lambda keyword; accepts any number of arguments, but only has one
#                   expression (like a shortcut; useful if needed for a short period of time to throw away)
# lambda parameters: expression

def double(x):
    return x * 2

print(double(5))

double = lambda x: x * 2                                       # lambda then parameters (x) then expression : x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z

print(double(10))
print(multiply(10, 10))
print(add(15, 3, 2))

full_name = lambda first_name, last_name: first_name + " " + last_name
age_check = lambda age: True if age >= 18 else False

print(full_name("Kevin", "Dacanay"))
print(age_check(15))
print(age_check(18))

# examples:

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def myfunc(n):
  return lambda a : a * n

doubler = myfunc(2)
tripler = myfunc(3)
print(doubler(11))
print(tripler(11))

print("-------------------------------------")
print()

# LAMBDA CONDITIONALS:
print("Lambda Conditionals:")

# lambda args: a if boolean_expression else b
starts_with_J = lambda x: True if x.startswith('J') or ('j') else False
j = input('Enter a name that starts with J: ')
print(starts_with_J(j))

# lambda checking the word before specified word in a sentence:
word_before = lambda s, w: s.split()[s.split().index(w)-1] if w in s else None
sentence = 'Four score and seven years ago'
print(word_before(sentence, 'seven'))