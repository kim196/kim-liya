import random
import os
from PIL import Image

# Returns a dictionary where the keys are image filenames and the values are the corresponding locations
def load_dictionary(file):
    with open(file) as f:
        data = {}
        for line in f: 
            filename, location = line.strip().split(',')
            data[filename.strip()] = location.strip()
        return data
    
# Display image
def display_image(image_filename):
    img = Image.open(image_filename)
    img.show()

# Checks if this is a valid guess
def is_valid_guess(guess, guesses):
    return guess in guesses

#evaluates the color of each letter depending on its location in the word
def evaluate_guess(guess, location):
    
    if guess != location : 
        return "Try Again"

    print("Congrats! You got it")

#loads the game 
def guesser(images):
    print("Welcome to CampusGueser! You have 3 chances to guess the location on campus.")
    image_filename, location = random.choice(list(images.items()))
    display_image(image_filename)

    attempts = 1

    while(attempts <= 3):
        guess = input ("Enter guess #" + str(attempts) + ": ").lower()
        

        if not is_valid_guess(guess, "guesses.txt"):
            print("Invalid location.")
            continue
        elif guess == location:
            print("Congratulations! You guessed the location.")
            break
        else:
            attempts +=1 
            feedback = evaluate_guess(guess, location)
            print(feedback)

    if attempts > 6:
        print("Game over. The location was: ", location)

# Load images       
images = load_dictionary("images.txt")

# Start the game
guesser(images)

