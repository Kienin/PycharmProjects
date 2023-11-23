# WHILE LOOPS = a statement that will execute as long as it's condition remains true

'''

infinite while loop - will keep going over and going.

while 1==1:
    print("Help! I'm stuck in a loop!!!")

'''

    # Necessary input - must input a name or program will keep asking for input
name = ""

while len(name) == 0:
    name = input("Enter your name: ").capitalize()
print("Hello,", name, "!")

while True:
    name = input("Enter your name: ")
    if name != "":
        break

    # End goal while loop - while loop will end after meeting end goal
i = 1
while i <= 5:
    print(i * 'Boom')
    i = i + 1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1





# FOR LOOPS = a statement that will execute for a limited amount of time
for i in range(10):
    print(i + 1)                          # "+ 1" to count to one more

    # For loops with starting and ending points:
for i in range(50, 100):
    print(i + 1)

    # For loops with starting, ending, and step:
for i in range(50, 100, 2):               # will skip 2 everytime
    print(i)


    # For loop that will print out every character in string:
for i in "Kevin Dacanay":
    print(i)

# COUNTDOWN TIMER
import time

for seconds in range(10, 0, -1):          # "-1" means it counts down
    print(seconds)
    time.sleep(1)                         # time.sleep(1) means the countdown will lag by 1 second
print("HAPPY NEW YEAR!!!")





# NESTED LOOPS = The "inner loop" will finish all it's iterations before finishing one iteration of the "outer loop"
rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):                      # common practice to use j for inner loops
        print(symbol, end="")                     # 'end=""' prevents cursor from moving down to the next line
    print()





# BREAK CONTINUE PASS
# LOOP CONTROL = change a loops execution from its normal sequence

# break    = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass     = does nothing; acts as a placeholder

    # BREAK: Necessary input = must input or program will keep asking for input
while True:
    name = input("Enter your name: ")
    if name != "":
        break

print("--------------------------------")

    # CONTINUE: skips a character
phone_number = "630-890-5069"

for i in phone_number:
    if i == "-":
        continue                      # skips whever "-" is present
    print(i, end="")                  # 'end=""' prevents the program from moving down the next line (prints out in one line)

print("")
    # PASS: does nothing
for i in range(1, 21):
    if i == 13:
        pass                          # pass skips the number 13
    else:
        print(i) #end="")

