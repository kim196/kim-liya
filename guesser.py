import random

#loads all the words in the file
def load_dictionary(file):
    with open(file) as f:
        words = [line.strip() for line in f]
        return words

#checks if this is a valid guess
def is_valid_guess(guess, guesses):
    return guess in guesses

#evaluates the color of each letter depending on its location in the word
def evaluate_guess(guess, place):
    
    if guess != place : 
        return "Try Again"

    print("Congrats! You got it")

#loads the game 
def guesser(guesses, answers):
    print("Welcome to CampusGueser! You have 6 chances to guess the locstion on campus.")
    place = random.choice(answers)

    attempts = 1

    while(attempts <= 3):
        guess = input ("Enter guess #" + str(attempts) + ": ").lower()

        if not is_valid_guess:
            print("Invalid location.")
            continue
        elif place == guess:
            print("Congratulations! You guessed the location.")
            break
        else:
            attempts +=1 
            feedback = evaluate_guess(guess, place)
            print(feedback)

    if attempts > 6:
        print("Game over. The location was: ", place)
        
guesses = load_dictionary("guesses.txt")
answers = load_dictionary("answers.txt")

guesser(guesses, answers)

