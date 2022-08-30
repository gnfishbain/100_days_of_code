#Number Guessing Game Objectives:
import random
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
random_num = random.randint(0,101)


guess_left = True
def live():
    difficulty = input("please select difficulty level: Hard, Easy: ").lower()
    if difficulty == "hard":
        return 5
    if difficulty == "easy":
        return 10

lives = live()
print (lives)

while guess_left:
    user_guess = int(input("please guess a number: "))
    if random_num < user_guess:
        print ("To High")
        lives = lives - 1
        if lives == 0:
            print ("you lose")
            break
        else:
            print (f"you gat: {lives}  tries ")
    if random_num > user_guess:
        print ("To Low")
        lives = lives - 1
        if lives == 0:
            print ("you lose")
            break
        else:
            print(f"you gat: {lives}  tries ")
    if random_num == user_guess:
        print (f"The number is: {random_num} ,You Won!")
        guess_left = False


# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

