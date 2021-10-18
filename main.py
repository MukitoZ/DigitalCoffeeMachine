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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
help_command = {
    "report": "To see the resources inside the coffee machine.",
    "price": "To see coffee's price."
}


def check_resource(coffee):
    """Function to check if there is enough resources in resources dictionary"""
    ingredient = MENU[coffee]["ingredients"]
    for check_ingredient in ingredient:
        ingredient_resource = resources[check_ingredient]
        if ingredient_resource < ingredient[check_ingredient]:
            print(f"Sorry, there is not enough {check_ingredient}")
            return False
        return True


def check_money(coffee, coins):
    """Function to check the money user inserted inside the coffee machine"""
    price = MENU[coffee]["cost"]
    if price > coins:
        print("Sorry, that's not enough money. Money refunded.")
    elif price == coins:
        resources["money"] += coins
    elif price < coins:
        change = coins - price
        resources["money"] += price
        print(f"Here is ${round(change, 2)} dollars in change.")


def make_coffee(coffee):
    """Function to reduce ingredients in resources dictionary minus coffee ingredients"""
    drink = MENU[coffee]["ingredients"]
    for minus_ingredient in drink:
        recipe = drink[minus_ingredient]
        resources[minus_ingredient] -= recipe
    print(f"Here is your {coffee}. Enjoy!")


def coffee_machine():
    is_on = True
    resources["money"] = 0
    print("Type 'help' to check command.")
    while is_on:
        command = input("What would you like? (espresso/latte/cappuccino):").lower()
        if command == "report":
            for x in resources:
                if x == "money":
                    print(f"{x.title()}: ${resources[x]}")
                else:
                    print(f"{x.title()}: {resources[x]}")
        elif command == "off":
            return
        elif command == "price":
            for coffee in MENU:
                price = MENU[coffee]["cost"]
                print(f"{coffee.title()}: ${price}")
        elif command == "help":
            for h in help_command:
                print(f"{h}: {help_command[h]}")
        elif command == "espresso" or command == "latte" or command == "cappuccino":
            is_resource = check_resource(command)
            if is_resource:
                print("Please insert coins.")
                quarters = float(input("How many quarters?($0.25): ")) * 0.25
                dimes = float(input("How many dimes?($0.10): ")) * 0.10
                nickles = float(input("How many nickles?($0.05): ")) * 0.05
                pennies = float(input("How many pennies?($0.01): ")) * 0.01
                total_money = quarters + dimes + nickles + pennies
                check_money(command, total_money)
                make_coffee(command)
        else:
            print("Type the right input!")


coffee_machine()
