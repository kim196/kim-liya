import random
import os
from PIL import Image
from flask import Flask, url_for, render_template, request

app = Flask(__name__, static_folder='static')

# Returns dictionary of guesses
def load_dictionary(file):
    with open(file) as f:
        words = [line.strip() for line in f]
        return words

# Returns a dictionary where the keys are image filenames and the values are the corresponding locations
def load_locations(file):
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

        guesses = load_dictionary("guesses.txt")
        

        if not is_valid_guess(guess, guesses):
            print("Invalid location.")
            continue
        elif guess == location:
            print("Congratulations! You guessed the location.")
            break
        else:
            attempts +=1 
            feedback = evaluate_guess(guess, location)
            print(feedback)

    if attempts > 3:
        print("Game over. The location was: ", location)

# Path to Flask folder of images   
image_dir = os.path.join(app.static_folder, 'images')
# List of images (URLS) in Flask folder
images = os.listdir(image_dir)  
# URL to img of random location
location_img = random.choice(images)
# Name of random location
location = load_locations('images.txt').get(location_img)

attempts = 1


# Default home/start page
@app.route("/")
def home():
    map_url = url_for('static',filename=f'map/map.jpeg')
    return render_template("index.html",  map_url = map_url)

# Game pages
@app.route("/start_game")
def game():
    img_url = url_for('static',filename=f'images/{location_img}')
    return render_template("game.html", image_url=img_url)

# Provides feedback based on answer
@app.route("/feedback", methods=['POST'])
def feedback( ):
    global attempts 
    guess = request.form['guess']
    
    if guess.lower() != location:
        if attempts < 3: 
            attempts =  attempts + 1
            img_url = url_for('static',filename=f'images/{location_img}')
            return render_template("try_again.html", image_url=img_url, num_attempts = 4 - attempts)
        else:
            return "GAME OVER :("
    else: 
        return "Congratulations! You guessed the location correctly :)"
   

if __name__ == "__main__":
    app.run()