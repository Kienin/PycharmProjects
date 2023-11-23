# INPUT - get name and word (or even a sentence)
name = str(input("Hi! What's your name? "))
print(f"Hi {name.capitalize()}! This is a vowel detector program.\n"
      f"Type in a word or a phrase and let's check how many vowels it has!\n")

# PROCESS - in a while True loop if user wants to input again.
#           Word will be put in a for loop to iterate each letter checking if they are a vowel
#           If vowel is detected, vowel count will go up and letter will be put in vowel_present list
while True:
    word = str(input("Enter a word: "))

    vowel_count = 0

    A = []
    A_count = 0
    for i in word:
        if i == "A":
            vowel_count += 1
            A_count += 1
            A.append(i)
        else:
            continue

    E = []
    E_count = 0
    for i in word:
        if i == "E":
            vowel_count += 1
            E_count += 1
            E.append(i)
        else:
            continue

    I = []
    I_count = 0
    for i in word:
        if i == "I":
            vowel_count += 1
            I_count += 1
            I.append(i)
        else:
            continue

    O = []
    O_count = 0
    for i in word:
        if i == "O":
            vowel_count += 1
            O_count += 1
            O.append(i)
        else:
            continue

    U = []
    U_count = 0
    for i in word:
        if i == "U":
            vowel_count += 1
            U_count += 1
            U.append(i)
        else:
            continue

    a = []
    a_count = 0
    for i in word:
        lettera = ["a"]
        if i in lettera:
            vowel_count += 1
            a_count += 1
            a.append(i)
        else:
            continue

    e = []
    e_count = 0
    for i in word:
        if i == "e":
            vowel_count += 1
            e_count += 1
            e.append(i)
        else:
            continue

    letteri = []
    i_count = 0
    for i in word:
        if i == "i":
            vowel_count += 1
            i_count += 1
            letteri.append(i)
        else:
            continue

    o = []
    o_count = 0
    for i in word:
        if i == "o":
            vowel_count += 1
            o_count += 1
            o.append(i)
        else:
            continue

    u = []
    u_count = 0
    for i in word:
        if i == "u":
            vowel_count += 1
            u_count += 1
            u.append(i)
        else:
            continue

# OUTPUT - print out the word, number of vowels, and the vowels detected
    print(f"There are {vowel_count} vowels in \'{word}\'")

    if A_count > 0:
        print(f"\'A\' is present {A_count} times in your word")
    if E_count > 0:
        print(f"\'E\' is present {E_count} times in your word")
    if I_count > 0:
        print(f"\'I\' is present {I_count} times in your word")
    if O_count > 0:
        print(f"\'O\' is present {O_count} times in your word")
    if U_count > 0:
        print(f"\'U\' is present {U_count} times in your word")
    if a_count > 0:
        print(f"\'a\' is present {a_count} times in your word")
    if e_count > 0:
        print(f"\'e\' is present {e_count} times in your word")
    if i_count > 0:
        print(f"\'i\' is present {i_count} times in your word")
    if o_count > 0:
        print(f"\'o\' is present {o_count} times in your word")
    if u_count > 0:
        print(f"\'u\' is present {u_count} times in your word")

# If user wants to input again
    again = str(input("\nDo you want to enter another word? (y/n) ").lower())
    if again != "y":
        print("Goodbye!")
        break
