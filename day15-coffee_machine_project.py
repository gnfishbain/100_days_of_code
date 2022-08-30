MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,

        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

user_choise = input("What would you like? (espresso/latte/cappuccino):").lower()

kind = MENU[user_choise]
cost = kind['cost']

for _ in resources:
    if resources[_] >= kind['ingredients'][_]:
        make_coffe = True
        print(f"you need to pay {cost}$")
    else:
        print (f"sorry not enaghe {_} for coffe")

def hading_money():
    cost = kind['cost']
    quarters = int(input("how many quarters you want to had? "))
    cost -= (quarters * 0.25)
    print (f"you gat {cost} $ left")
    dimes = int(input("how many dimes you want to had? "))
    cost -= (dimes * 0.10)
    print(f"you gat {cost} $ left")
    nickles = int(input("how many nickles you want to had? "))
    cost -= (nickles * 0.05)
    print(f"you gat {cost} $ left")
    pennies = int(input("how many pennies you want to had? "))
    cost -= (pennies * 0.01)
    print(f"you gat {cost} $ left")
    return cost

curract_amount = hading_money()

if curract_amount == 0:
    print (f"making coffe")
if curract_amount < 0:
    print (f"your change is{curract_amount * -1}$, enjoy you coffe")



#quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01









