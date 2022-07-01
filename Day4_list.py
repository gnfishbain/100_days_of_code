# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random

print (names)

list_lan = len(names)
print (f"lan is {list_lan}")


name_choice = random.randint(0,list_lan - 1)

print (f"{names[name_choice]} is going to pay the bill today")



