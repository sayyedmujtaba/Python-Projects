import random

user_score = 0
computer_score = 0
ties = 0
rounds = 0

choices = ['rock', 'paper', 'scissors']

while True:
    user_in = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
    if user_in == 'exit':
        print(f"Final Scores:\nUser: {user_score}\nComputer: {computer_score}\nTies: {ties}\nRounds: {rounds}")
        break

    if user_in not in choices:
        print("Invalid input. Please try again.")
        continue

    computer_in = random.choice(choices)
    print(f"Computer chose: {computer_in}")

    if user_in == computer_in:
        print("It's a tie!")
        ties += 1
    elif (user_in == 'rock' and computer_in == 'scissors') or (user_in == 'paper' and computer_in == 'rock') or (user_in == 'scissors' and computer_in == 'paper'):
        print("You win!")
        user_score += 1