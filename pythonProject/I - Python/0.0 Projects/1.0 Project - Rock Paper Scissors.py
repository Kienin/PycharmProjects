import random

choices = ['Rock', 'Paper', 'Scissors']
score = {"player_score": 0, "computer_score": 0}

print("Let's play Rock, Paper, Scissors!")

while True:
        player_choice = input("Pick Rock, Paper, or Scissors: ").capitalize()
        while player_choice not in choices:
            player_choice = input("Invalid choice! Please try again: ").capitalize()

        computer_choice = random.choice(choices)
        print(f"\nYou chose '{player_choice}'. The computer chose '{computer_choice}'.")

        if computer_choice == player_choice:
            print("It's a tie!")
        elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
                (player_choice == 'Paper' and computer_choice == 'Rock') or \
                (player_choice == 'Scissors' and computer_choice == 'Paper'):
            print("Player Wins!")
            score["player_score"] += 1
        else:
            print("Computer Wins!")
            score["computer_score"] += 1

        print(f"\nScore = Player: {score['player_score']} - Computer: {score['computer_score']}\n")
        print("----------------------------------")
        play_again = str(input("Do you want to play again? y/n: "))
        if play_again != "y":
            break


print("\nFinal Score:")
print(f"Player: {score['player_score']} - Computer: {score['computer_score']}")
