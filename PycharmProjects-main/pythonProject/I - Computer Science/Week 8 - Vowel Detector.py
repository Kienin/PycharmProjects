'''
•	Option 2 - Vowel detector
o	Ask a user for a string
o	Find out how many vowels the string has
o	Display
i.	The string user provided
ii.	the result (how many vowels there are)
iii. Be sure to check for both upper-case and lower-case vowels
iv.	Display the found vowels and how many times those vowels occurred. i.e., e – 3 times. A – 1 time, etc.
'''

# INPUT - get name and word (or even a sentence)
name = str(input("Hi! What's your name? "))
print(f"Hi {name.capitalize()}! This is a vowel detector program.\n"
      f"Type in a word or a phrase and let's check how many vowels it has!\n")

# PROCESS - in a while True loop if user wants to input again.
#           Word will be put in a for loop to iterate each letter checking if they are a vowel
#           If vowel is detected, vowel count will go up and letter will be put in vowel_present list
while True:
    word = str(input("Enter a word: "))

    vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    vowel_count = 0
    present_vowels = []

    for i in word:
        if i in vowel:
            vowel_count += 1
            present_vowels.append(i)
        else:
            continue

# OUTPUT - print out the word, number of vowels, and the vowels detected
    print(f"There are {vowel_count} vowels in your word")
    print(f'The vowel/s in your word (\'{word}\') are: {present_vowels}')

# If user wants to input again
    again = str(input("\nDo you want to enter another word? (y/n) ").lower())
    if again != "y":
        print("Goodbye!")
        break
