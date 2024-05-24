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
def evaluate_guess(guess, word):
    str = ""

    for i in range(5):
        if guess[i] == word[i]:
            str += "\033[32m" + guess[i]
        elif guess[i] in word:
            str += "\033[33m" + guess[i]
        else: 
            str += "\033[0m" + guess[i]

    return str + "\033[0m" 

#loads the game 
def guesser(guesses, answers):
    print("Welcome to CampusGueser! You have 6 chances to guess a 5 letter word.")
    place = random.choice(answers)

    attempts = 1

    while(attempts <= 6):
        guess = input ("Enter guess #" + str(attempts) + ": ").lower()

        if not is_valid_guess:
            print("Invalid word. Please enter a 5 letter english word.")
            continue
        elif place == guess:
            print("Congratulations! You guessed the word.")
            break
        else:
            attempts +=1 
            feedback = evaluate_guess(guess, place)
            print(feedback)

    if attempts > 6:
        print("Game over. The word was: ", place)
        
guesses = load_dictionary("guesses.txt")
answers = load_dictionary("answers.txt")

guesser(guesses, answers)

