import random
from logo import *
from game_data import data

# Generate a random account from the game data.
right_answer = True
score = 0

random_accountA = (random.choice(data))

while right_answer:

    random_accountB = (random.choice(data))
    if random_accountB == random_accountA:
        random_accountB = (random.choice(data))

    # Format account data into printable format.
    def print_question():
        print (logo)
        print (random_accountA['name'])
        print (random_accountA['follower_count'])
        print (vs)
        print(random_accountB['name'])
        print (random_accountB['follower_count'])
        print (F"you score is: {score}")

    print_question()

    # Ask user for a guess.
    user_guess = input ("What is your guss A or B?").lower()

    # Check if user is correct.
    ## Get follower count.
    countA = random_accountA['follower_count']
    countB = random_accountB['follower_count']

    ## If Statement
    if user_guess == "a":
        if countA > countB:
            print ("Great!")
            score += 1
        if countA < countB:
            print ("You lose")
            right_answer = False
    if user_guess == "b":
        if countA < countB:
            print ("Great!")
            score += 1
            random_accountA = random_accountB
        if countA > countB:
            print ("You lose")
            right_answer = False


