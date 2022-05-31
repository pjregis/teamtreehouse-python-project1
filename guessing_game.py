"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""
import random
import os

def start_game():
    best_score = None
    lowest_number = 1
    highest_number = 10
    while True:        
        number_of_guesses = 0
        secret_number = None
        guess = None
        # 1. Display an intro/welcome message to the player.
        print("Welcome to 'Guess the Number'!")
        # As a player of the game, at the start of each game I should be shown the current high score (least amount of points) so that I know what I am supposed to beat.
        if best_score is None:
            print("A best score hasn't been set yet.")
        else:
            print("The current best score is {} tries.".format(best_score))
        # 2. Store a random number as the answer/solution.
        # Every time a player decides to play again, the random number to guess is updated so players are guessing something new each time.
        if secret_number is None:
            secret_number = random.randint(1,10)
        # 3. Continuously prompt the player for a guess.
        while guess != secret_number:
            try:
                guess = int(input("Guess a number between {} and {} >> ".format(lowest_number, highest_number)))
            except ValueError:
                print("Invalid input. Your guess must be a digit between {} and {}. Try again.".format(lowest_number, highest_number))
                continue
            if guess < lowest_number or guess > highest_number:
                print("Invalid input. Your guess must be a digit between {} and {}. Try again.".format(lowest_number, highest_number))
                continue
            number_of_guesses += 1
            # As a player of the game, my guess should be within the number range. If my guess is outside the guessing range I should be told to try again.
            if guess != secret_number:
                if guess > secret_number:
                    print("Your guess is HIGHER than the secret number. Try again!")
                elif guess < secret_number:
                    print("Your guess is LOWER than the secret number. Try again!")
        if best_score is None or number_of_guesses < best_score:
            best_score = number_of_guesses
        # 4. Once the guess is correct, stop looping, inform the user they "Got it"
        print("Congratulations! You guessed the secret number!")
        print("It took you {} tries.".format(number_of_guesses))
        print("The current best score is {} tries.".format(best_score))
        # As a player of the game, after I guess correctly I should be prompted if I would like to play again.
        while True:            
            play_again = input("Would you like to play again? [y]es | [n]o >> ")   
            if play_again.upper() == "Y" or play_again.upper() == "N":
                break     
        if play_again.upper() == "Y":
            continue   
        break
    print("Exiting the game...")
    exit()    

# Kick off the program by calling the start_game function.
start_game()