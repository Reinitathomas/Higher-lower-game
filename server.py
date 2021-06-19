from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)


@app.route('/')
def home():
    return "<h1>Choose a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route('/<int:guess>')
def guess_number(guess):
    if guess < random_number:
        return "<h1 style='color:#04009A'>The number you chose is Too Low, Try Again!!</h1>" \
               "<img src='https://media.giphy.com/media/12ELmx0C4EFKcE/giphy.gif'>"
    elif guess > random_number:
        return "<h1 style='color:#FF96AD'>The number you chose is Too high, Try again</h1>" \
               "<img src='https://media.giphy.com/media/hvS1eKlR75hMr0l7VJ/giphy.gif'>"
    elif guess == random_number:
        return "<h1 style='color:#942E88'>You found me!!</h1>" \
               "<img src='https://media.giphy.com/media/11kXFNRcZBFgwo/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
