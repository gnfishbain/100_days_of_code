rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

"chose what your play"
my_choice = int(input("please select: 1-paper, 2-rock, 3-scissors: "))
if my_choice == 1:
    print (f"you selected {paper}")
if my_choice == 2:
    print (f"you selected {rock}")
if my_choice == 3:
    print (f"you selected {scissors}")

"computer random choice"
comp_choice = random.randint(1, 3)
print (comp_choice)

if comp_choice == 1:
    print (f"computer selected {paper}")
if comp_choice == 2:
    print (f"computer selected {rock}")
if comp_choice == 3:
    print (f"computer selected {scissors}")

if my_choice == comp_choice:
    print ("TIE")
if my_choice == 2 and comp_choice == 1:
    print ("computer won!")
if my_choice == 1 and comp_choice == 2:
    print ("you won!")
if my_choice == 3 and comp_choice == 2:
    print ("computer won!")
if my_choice == 2 and comp_choice == 3:
    print ("you won!")
if my_choice == 1 and comp_choice == 3:
    print ("you won!")
if my_choice == 2 and comp_choice == 1:
    print ("comp won!")

