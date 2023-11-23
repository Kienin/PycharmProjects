# format{} allows you to format selected parts of a string

print("Formatting:")
price = 49
msg = "The price is {} dollars"
print(msg.format(price))

print("\nSpecify decimals:")
txt = "The price is {:.2f} dollars"
print(txt.format(price))

# Formatting Multiple Values:
print('\nFormatting Multiple Values:')
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Indexing Format:
print("\nIndexing Format:")
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

print()
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

print("\nNamed Indexing:")
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))