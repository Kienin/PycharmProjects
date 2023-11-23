
print("Let's take a quiz!")

# ----------------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("----------------------")
        print(key)                                                  # key in dictionary = questions
        for i in options[question_num-1]:                           # options[question_num-1] index to show options only for question 1
            print(i)
        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess)                                       # append/add current guess to guesses list

        correct_guesses += check_answer(questions.get(key), guess)  # check_answer function checks answers from keys in dictionary and also adds points if answer is correct
        question_num += 1                                           # increment question_num by 1 so question 2 while have options set 2 and so on...

    display_score(correct_guesses, guesses)                         # displays the correct guesses and list of guesses
# ----------------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("Correct!")
        return 1                                                    # returns 1 point for correct answer
    else:
        print("Wrong!")
        return 0

# ----------------------------------
def display_score(correct_guesses, guesses):
    print("----------------------")
    print("RESULTS: \n")

    print("Answers: ", end="")                                  # DISPLAYS "ANSWERS:XXXX" end= doesnt end on a new line
    for i in questions:
        print(questions.get(i), end=" ")                        # DISPLAYS "GUESSES: XXXX" all the answers in dictionary
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")  # displays all the answers in dictionary
    print()

    score = int((correct_guesses/len(questions)) * 100)         # DISPLAYS SCORE
    print("You got "+str(score)+"% correct answers\n")

# ----------------------------------
def play_again():

    response = input("Do you want to play again? y/n: ").upper()
    if response == "Y" or "YES" or "sure" or "yeah":
        return True
    else:
        return False

# ----------------------------------

# Dictionary for questions: {key: answers}
questions = {
    "What's my name?: ": "A",
    "What year was I born?: ": "B",
    "Where was I born?: ": "C",
    "What is my second language?: ": "A"
}

# 2D list for options:
options = [["A. Kevin", "B. Ken", "C. Kyle", "D. Fides"],
           ["A. 2000", "B. 2004", "C. 2003", "D. 2023"],
           ["A. America", "B. China", "C. Philippines", "D. Canada"],
           ["A. English", "B. Tagalog", "C. Spanish", "D. French"]]

new_game()

while play_again() is True:
    new_game()
else:
    print("Have a good day!")
