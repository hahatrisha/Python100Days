"""Coffee Machine Program"""

# Defining Menu
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "price": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        },
        "price": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100
        },
        "price": 2.5
    },
}

# Defining resources and profit
resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200
}
profit = 0


# Checking if resources are sufficient
def is_resource_sufficient(order_ingredients):
    """Returns True when there are sufficient ingredients to make the order"""
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# Prompting the user to insert coins
def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?:")) * 0.25
    total += int(input("How many dimes?:")) * 0.1
    total += int(input("How many nickles?:")) * 0.05
    total += int(input("How many pennies?:")) * 0.01
    return total


# Checking if transaction is successful
def is_transaction_success(money_received, drink_cost):
    """Returns True when the payment is accepted, or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough. Money refunded.")
        return False


# Making coffee
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


is_on = True

while is_on:
    # Prompt user by asking "What would you like?"
    # Check the user's input to decide what to do next
    user = input("What would you like? (espresso/latte/cappuccino):")

    # turn off the machine by entering "off" to the prompt
    if user == "off":
        is_on = False

    # generate a report when the user enters "report" to the prompt
    elif user == "report":
        print(f"Water: {resources['water']}ml; \nMilk: {resources['milk']}; "
              f"\nCoffee: {resources['coffee']}g; \nMoney: ${profit}.")

    # when the user chooses a drink, make that drink
    elif user == "espresso" or user == "latte" or user == "cappuccino":
        drink = menu[user]
        if is_resource_sufficient(drink["ingredients"]):
            money_received = process_coins()
            if is_transaction_success(money_received, drink["price"]):
                make_coffee(user, drink["ingredients"])

    # when the user enters something else, ask them to reselect the drink
    else:
        print("Selection error. Please reselect your drink.")