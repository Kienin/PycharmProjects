'''
o	Modify the previously written Rock-Paper-Scissors game as best of X (X = odd number, 3 or greater)
o	Allow the user to enter only one letter for choice - R r for Rock, P p for Paper, and S s for Scissors
o	Display what the user and computer chose and who won
o	Display who won the game
o	You must use a loop
o	Optional - If you are up for a challenge…in addition to the above items, you can make it best out of x (user provided). X should be an odd integer number. Also, display the score.
'''

import random

print("Let's play Rock Paper Scissors!")

while True:
    rounds = int(input("How many rounds do you want to play for? (enter an odd number) "))
    if rounds % 2 != 0:
        break
    else:
        print("Please enter an odd number of rounds.")

player_wins = 0
computer_wins = 0
winning_score = (rounds + 1) // 2

while player_wins < winning_score and computer_wins < winning_score:
    print(f"Player Score: {player_wins} | Computer Score: {computer_wins}")

    player = input("Rock, Paper, or Scissors? ").lower()
    if player not in ["rock", "paper", "scissors"]:
        print("Invalid input. Try again.")
        continue

    computer = random.choice(["rock", "paper", "scissors"])

    print(f"Player: {player} | Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("Player wins!")
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("Player wins!")
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1
    elif player == "scissors":
        if computer == "paper":
            print("Player wins!")
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1

if player_wins > computer_wins:
    print("CONGRATULATIONS, YOU WON!")
else:
    print("Oh no, the computer won. Better luck next time!")

print(f"FINAL SCORE - Player: {player_wins} | Computer: {computer_wins}")