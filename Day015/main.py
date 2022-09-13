import os
logo = """"
 ██████╗ ██████╗ ███████╗███████╗███████╗███████╗    
██╔════╝██╔═══██╗██╔════╝██╔════╝██╔════╝██╔════╝    
██║     ██║   ██║█████╗  █████╗  █████╗  █████╗      
██║     ██║   ██║██╔══╝  ██╔══╝  ██╔══╝  ██╔══╝      
╚██████╗╚██████╔╝██║     ██║     ███████╗███████╗    
 ╚═════╝ ╚═════╝ ╚═╝     ╚═╝     ╚══════╝╚══════╝    
                                                     
"""

print(logo)
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def resource_sufficient (order_ingredients):
    for items in order_ingredients:
        if order_ingredients[items] >= resources[items]:
            print(f"Sorry there is not enough {items}")
            return False
        else:
            return True

def process_coins():
    """"Returns total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?: "))*0.25
    total += int(input("How many dime?: "))*0.10
    total += int(input("How many nickle?: "))*0.05
    total += int(input("How many penny?: "))*0.01
    return total

def transaction(money_received,drink_cost):
    """"Returns True if the payment is accepted , or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost ,2)
        print(f"Here is your change ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, thats not enough money. Money refunded")

def make_coffee(drink_name,order_ingredients):
    for items in order_ingredients:
        resources[items]-= order_ingredients[items]
    print(f"Here is your {drink_name} ☕")


is_on = True

while is_on:
    
    choice = input("What would you like to have? (espresso/latte/cappuccino)\n")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        print(drink)
        if resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            transaction(payment,drink["cost"])
            make_coffee(choice,drink["ingredients"])
            
            