from art import logo, vs
from game_data import data
import random


# Compare A:
# Against B:
# Who has more followers? Type 'A' or 'B':
# Sorry, that's wrong. Final score: 0
# You're right! Current score: 1.

# 1. Start game
# 2.Ask question import the data randomly for a and b
def get_instagram_acc():
    """Gets the initial instagram account randomly"""
    account = random.choice(data)

    return account


def get_instagram_acc_next():
    """Gets the next instagram account without choosing the same one from before"""
    # make sure that we do not get the same next account
    account = random.choice([x for x in data if x != person_a])
    return account


def print_instagram_acc(person, person2):
    """Prints comparison"""
    print(f'Compare A: {person["name"]}, a {person["description"]}, from {person["country"]}')
    print(vs)
    print(f'Against B: {person2["name"]}, a {person2["description"]}, from {person2["country"]}')


# game starts here
score = 0
continue_game = True
print(logo)

person_a = get_instagram_acc()
person_b = get_instagram_acc_next()

# exit when response is wrong
while continue_game:
    print_instagram_acc(person_a, person_b)

    response = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check response and calculate score
    if response == 'a' and person_a["follower_count"] > person_b["follower_count"]:
        score += 1
        print(f"You are right, A has more. Current score: {score}")
    elif response == 'b' and person_b["follower_count"] > person_a["follower_count"]:
        score += 1
        print(f"You are right, A has more. Current score: {score}")
    else:
        continue_game = False
        print(f"Sorry, that's wrong. Final score: {score}")

    person_a = person_b
    person_b = get_instagram_acc_next()
