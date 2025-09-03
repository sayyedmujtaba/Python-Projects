import random 
attempts = 0
max_attempts = 7

random_number = random.randint(1, 100) # geerating a random number between 1 and 100
print("Welcome to the Number Guessing Game!")

while attempts < max_attempts: # loop until max attempts are reached
    try:
        guess = int(input(f"Attempt {attempts + 1}: Enter your guess (1-100): "))
        attempts += 1

        # ---------------------------------------------------------------------------- #
        #                  comparing user guess with the random number                 #
        # ---------------------------------------------------------------------------- #
        
        if guess == random_number:
            print(f"Congratulations! You've guessed the correct number in {attempts} attempts.")
            break

        elif guess < random_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 100.")

    if attempts == max_attempts:
        print(f"Sorry, you've used all your attempts. The correct number was {random_number}.")