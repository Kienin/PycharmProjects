'''
Hello! My name is Kevin Dacanay and this is a Rock, Paper, Scissors game.
The program will be taking in user input (their name and their choice
of either rock, paper, or scissors), process the outcome, and
output the results (the winner and final score)
'''

import random

# INPUT - name and choice

choices = ["R", "P", "S"]
score = {"player_score": 0, "computer_score": 0}

name = str(input("Let's play Rock, Paper, Scissors! What is your name? ").capitalize())
print(f"Hello {name}!\n")

# the whole game is in a while loop so that we can play again
while True:
    player_choice = str(input("(R) for Rock, (P) for Paper, (S) for Scissors. What is your choice: ").capitalize())
    while player_choice not in choices:
        player_choice = str(input("Invalid input! Please select R, P, or S: "))

    computer_choice = random.choice(choices)

# PROCESS - scoring
# player and computer choices are changed to the actual words for readability.
    if player_choice == "R":
        player_choice = "Rock"
    elif player_choice == "P":
        player_choice = "Paper"
    else:
        player_choice = "Scissors"

    if computer_choice == "R":
        computer_choice = "Rock"
    elif computer_choice == "P":
        computer_choice = "Paper"
    else:
        computer_choice = "Scissors"

    print(f"\nYou chose {player_choice}. The computer chose {computer_choice}")

# program checks who wins the round and also tracks score
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
            (player_choice == 'Paper' and computer_choice == 'Rock') or \
            (player_choice == 'Scissors' and computer_choice == 'Paper'):

# OUTPUT - shows who wins their score
        print(f"{name} Wins!")
        score["player_score"] += 1
    else:
        print("Computer wins!")
        score["computer_score"] += 1

    print(f"Score = {name}: {score['player_score']} - Computer: {score['computer_score']}\n")
    print("______________________________________")

    play_again = str(input("Do you want to play again? (y/n) ").capitalize())
    if play_again != "Y":
        break

print(f"\nFinal Score = {name}: {score['player_score']} - Computer: {score['computer_score']}")
