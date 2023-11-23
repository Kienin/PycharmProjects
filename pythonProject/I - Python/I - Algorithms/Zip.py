# ZIP(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each element

usernames = ["Kevin", "Brian", "Kienin"]                    # list
passwords = ("p@ssword", "abc123", "guest")                 # tuple

users = zip(usernames, passwords)                           # zip() pairs usernames with passwords
for i in users:
    print(i)

print("")

users = list(zip(usernames, passwords))
for i in users:
    print(i)

print("")

users = dict(zip(usernames, passwords))
for key,value in users.items():
    print(key+": "+value)

print("")

usernames = ["Kevin", "Brian", "Kienin"]                    # list
passwords = ("p@ssword", "abc123", "guest")                 # tuple
login_dates = ["1/1/2023", "1/2/2023", "1/3/2023"]          # list

users = zip(usernames, passwords, login_dates)
for i in users:
    print(i)