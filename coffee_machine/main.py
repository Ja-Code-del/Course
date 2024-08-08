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
            "water": 100,
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
    "coffee": 10,  #100,
}
choice_of_coffee = input("What would you like? (espresso/latte/cappuccino): ")
#TODO 1 - Print Report
print(f"These are the available resources : ")
for key, value in resources.items():
    print(f"{key} : {value}")

#TODO 2 - Check Resources

ingredients = MENU[choice_of_coffee]["ingredients"]
for coffee_resource, valueCoffee in ingredients.items():
    if ingredients[coffee_resource] > resources[coffee_resource]:
        print(f"{coffee_resource} is not sufficient")
#TODO 3 - Process coins

#TODO 4 - Check transaction successful
