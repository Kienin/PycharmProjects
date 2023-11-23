# Slicing = create a substring by extracting elements from another string
# indexing[] or slice()
# [start:stop:step]

# INDEXING:
# Starting index:          Starting index = 0 which is the letter "K"
name = "Kevin Dacanay"
first_name = name[0:5]     #[:5] means everything before index 5
last_name = name[6:13]     #[6:] means everthing after index 6
print("First name:",first_name)
print("Last name:",last_name)

# Step is how much we're increasing our index by; a step of 2 means we're going to count evert second character
# name = Kevin Dacanay          name[0:13:2] = KvnDcny
x_name = name[::2]             # Empty start and stop means you are including everything
print(x_name)

reversed_name = name[::-1]     # Reverses a string
print(reversed_name)

print("--------------------------------")



# SLICING:
website = "http://google.com"
website2 = "http://wikipedia.com"

# Negative index: the right most character in the string has an index of -1  (i.e. the "." has an index of -4)
slice = slice(7,-4)

print(website[slice])
print(website2[slice])

print("--------------------------------")




# Extra functions:
names = ["Kevin", "Kyle", "Fides"]
names[2] = "Ken"
print(names[0:4])                    #[value = oder of names]

numbers = [1, 2, 3, 4, 5]            # .append adds a number to the array
numbers.append(6)
print(numbers)

numbers = [1, 2, 3, 4, 5]
numbers.insert(0, -1)         # .insert inserts a number; (n, N) = n: the order where N would be (inserts N in index n)
print(numbers)

numbers = [1, 2, 3, 4, 5]            # .removes takes away a specific number
numbers.remove(5)
print(numbers)

numbers = [1, 2, 3, 4, 5]            # .clears, clears the whole array
numbers.clear()
print(numbers)

numbers = [1, 2, 3, 4, 5]            # returns a Boolean: checks if 4 and 6 is in the array
print(4 in numbers)
print(6 in numbers)

numbers = [1, 1, 1, 1, 1, 1, 1, 1]   # len shows the length/amount that are inside an array
print(len(numbers))