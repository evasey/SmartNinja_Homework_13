import json

class Player():  #new model called Player
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds

# we moved all the code that BasketballPlayer and FootballPlayer can share in the Player class.
# let's adapt our BasketballPlayer and FootballPlayer models so they inherit the code from the Player model

class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(
            first_name=first_name,
            last_name=last_name,
            height_cm=height_cm,
            weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(
            first_name=first_name,
            last_name=last_name,
            height_cm=height_cm,
            weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

kev_dur = BasketballPlayer(
    first_name="Kevin", last_name="Durant", height_cm=210, weight_kg=108, points=27.2, rebounds=7.1,assists=4)

print(kev_dur.last_name)
print (kev_dur.__dict__)
print(kev_dur.rebounds)
print(kev_dur.weight_to_lbs())

messi = FootballPlayer(
    first_name="Lionel", last_name="Messi", height_cm=170, weight_kg=67, goals=575, yellow_cards=67, red_cards=0)

print(messi.first_name)
print(messi.goals)
print(messi.weight_to_lbs())


# Add an option that a user can enter data (via input())and at the end of the program the data gets saved in a text file (using json library).


def end():
    quest_continue = input("Do you want to continue?: y = yes, n = no")
    if quest_continue == "y":
        new_data()
    else:
        print("Thank you. Bye.")

def new_data():
    while True:
        sporttype = input("What sport do you do? (a) Basketball or (b) Football")

        if sporttype == "a":
            with open("basketball.txt", "r") as basketball_file:
                basketball = json.loads(basketball_file.read())
                print(basketball)
            basketballplayer = BasketballPlayer(
                    first_name=input("Please enter your first name: "),
                    last_name=input("Please enter your last name: "),
                    height_cm=input("Please enter your height(cm): "),
                    weight_kg=input("Please enter your weight: "),
                    points=input("Please enter your points: "),
                    rebounds=input("Please enter your rebounds: "),
                    assists=input("Please enter your assists: "))
            basketball.append({
                    "First name: ": basketballplayer.first_name,
                    "Last name: ": basketballplayer.last_name,
                    "Height: ": basketballplayer.height_cm,
                    "Weight: ": basketballplayer.weight_kg,
                    "Points: ": basketballplayer.points,
                    "Rebounds: ": basketballplayer.rebounds,
                    "Assists: ": basketballplayer.assists})

            with open("basketball.txt", "w") as basketball_file:
                basketball_file.write(json.dumps(basketball))
            end()
            break

        elif sporttype == "b":
            with open("football.txt", "r") as football_file:
                football = json.loads(football_file.read())
                print(football)
            footballplayer= FootballPlayer(
                    first_name=input("Please enter your Firstname: "),
                    last_name=input("Please enter your last name: "),
                    height_cm=input("Please enter your height(cm): "),
                    weight_kg=input("Please enter your weight: "),
                    goals=input("Please enter your goals: "),
                    yellow_cards=input("Please enter your yellow cards: "),
                    red_cards=input("Please enter your red cards: "))
            football.append({
                    "Fist name: ": footballplayer.first_name,
                    "Last name: ": footballplayer.last_name,
                    "Height: ": footballplayer.height_cm,
                    "Weight: ": footballplayer.weight_kg,
                    "Goals: ": footballplayer.goals,
                    "Yellow cards: ": footballplayer.yellow_cards,
                    "Red cards: ": footballplayer.red_cards})
            with open("football.txt", "w") as football_file:
                football_file.write(json.dumps(football))
            end()
            break

        else:
            break
new_data()

