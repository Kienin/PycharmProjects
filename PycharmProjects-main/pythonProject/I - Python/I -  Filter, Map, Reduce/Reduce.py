# REDUCE() = apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeats process until 1 value remains
# reduce(function, iterable)

import functools

letters = ["H", "E", "L", "L", "O"]
word = functools.reduce(lambda x,y:x + y, letters)           # cycles through the iterable until the word HELLO is formed
print(word)

factorial = [5,4,3,2,1]
result = functools.reduce(lambda x,y: x*y, factorial)
print(result)


# ISINSTANCE: checks whether an object is part of a certain class type
# isinstance(object, classinfo)

x = 5

if isinstance(x, int):
    print(x,"is an integer")

y = "Hello World"

if isinstance(y, str):
    print(y,"is a string")


input = [[1,1],2,[1,1]]

def flatten_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):                         # isinstance checks whether an object belongs to a class type
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

output_list = flatten_list(input)
print(output_list)