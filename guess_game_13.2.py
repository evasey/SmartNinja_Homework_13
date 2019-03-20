
import datetime
import json
import random

class Result():
    def __init__(self, score, player_name, date):
        self.score = score
        self.player_name = player_name
        self.date = date

def end():
    the_end = input("Would you like to (a) play a new game or (b) quit? ")
    if the_end == "a":
        secret_number()
    else:
        print("Good bye.")

with open("results.txt", "r") as results_file:
    results = json.loads(results_file.read())
    print(results)

player_name = input("Hello, what is your name?  ")

def secret_number():
    secret = random.randint(1, 30)
    attempts = 0

    while True:
        attempts += 1
        guess = input("Guess the secret number (between 1 and 30): ")
        if secret == int(guess):

            player = Result(
                score = str(attempts),
                player_name = str(player_name),
                date = str(datetime.datetime.now()))

            results.append({
                "Attempts:": player.score,
                "Name:": player.player_name,
                "Date:": player.date})
            with open("results.txt", "w") as results_file:
                results_file.write(json.dumps(results))
            print("You've guessed it - congratulations!")

            end()
            break

        elif secret > int(guess):
            print("Your guess is not correct... try something bigger")


        elif secret < int(guess):
            print("Your guess is not correct... try something smaller")

secret_number()

