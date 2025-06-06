import random
from termcolor import colored

user_score = 0
computer_score = 0
ties = 0
rounds = 0

choices = ['rock', 'paper', 'scissors']

while True:
    user_in = input(colored("Enter rock, paper, or scissors (or 'exit' to quit): ", "yellow")).lower()
    if user_in == 'exit':
        print("Exiting the game.")
        break

    if user_in not in choices:
        print("Invalid input. Please try again.")
        continue

    computer_in = random.choice(choices)
    print(f"Computer chose: {computer_in}")

    if user_in == computer_in:
        print("It's a tie!")
        ties += 1
    # The user wins if they choose rock against scissors, paper against rock, or scissors against paper else the computer wins
    elif (user_in == 'rock' and computer_in == 'scissors') or (user_in == 'paper' and computer_in == 'rock') or (user_in == 'scissors' and computer_in == 'paper'):
        print(colored("You win!", "green"))
        user_score += 1
    else:
        print(colored("Computer wins!", "red"))
        computer_score += 1
    rounds += 1

# Display the scores after the game ends
print(f"Scores:\nUser: {user_score}\nComputer: {computer_score}\nTies: {ties}\nRounds: {rounds}")