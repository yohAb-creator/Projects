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

# TODO: 1. Print resources.
print(resources)

# TODO: 2. Prompt user
def order():
    order = input("What would you like? Type 'espresso', 'latte', 'cappuccino'")
    return order
def report():
    profit = 0
    water = str(resources["water"]) + " ml"
    milk = str(resources["milk"]) + " ml"
    coffees = str(resources["coffee"]) + " g"
    reporter = f"water: {water}\nmilk: {milk}\ncoffee: {coffees}"
    return reporter, profit
def recipe(orders):
    return MENU[orders]['ingredients']
def payment():
    dime = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    pennies = int(input("How many pennies?"))
    quarters = int(input("How many quarters?"))
    pay = dime*0.1 + nickles*0.05 + pennies*0.01 + quarters * 0.25
    return pay
def prices():
    print(f'Espresso: ${MENU["espresso"]["cost"]}')
    print(f'Latte: ${MENU["latte"]["cost"]}')
    print(f'Cappuccino: ${MENU["cappuccino"]["cost"]}')


def coffee():
    fr, profits = report()
    is_on = True
    while is_on:
        orders = order()
        if orders == 'off':
            is_on = False
        if orders == 'report':
            print(f"{fr}\nprofit: ${profits}")
            coffee()
        if orders == 'prices':
            prices()
            coffee()
        else:
            for values in recipe(orders):
                if recipe(orders)[values] > resources[values]:
                    print("Not enough resources!")
                    coffee()

        money = payment()
        for values in recipe(orders):
            resources[values] -= recipe(orders)[values]
        if money == MENU[orders]['cost']:
            print(f"Here is your {orders}. You paid ${money}.")
            profits += MENU[orders]['cost']
        elif money > MENU[orders]['cost']:
            print(f"You paid ${MENU[orders]['cost']}. Your change is ${round(money -  MENU[orders]['cost'], 2)}. Here is your {orders}")
            profits += MENU[orders]['cost']

        else:
            print("Not enough money!")
        is_on = True




coffee()

