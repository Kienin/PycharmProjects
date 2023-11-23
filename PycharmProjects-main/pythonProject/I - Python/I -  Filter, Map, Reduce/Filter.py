# FILTER() = creates a collection of elements from an iterable for which a function returns
# filter(function, iterable)

friends = [("Kevin", 18),
           ("Jasmine", 17),
           ("Ben", 16),
           ("Seb", 15),
           ("John", 19)]

age = lambda data: data[1] >= 18                              # lambda func checks if x on index 1 is x > 18

drinking_buddies = list(filter(age, friends))
for i in drinking_buddies:
    print(i)

print("--------------------------------")