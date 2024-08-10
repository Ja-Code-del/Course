from calculator import operators

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

in_service = True
profit = 0
start = True



def report():
    print(f"These are the available resources : ")
    for ingredient, value in resources.items():
        print(f"{ingredient} : {value}")

 
while start:
    choice_of_user = input("What would you like? (espresso/latte/cappuccino): "
                           "\nType 'report' to see the resources\nType 'Off' to switch the machine off").lower()

    if choice_of_user == "report":
        report()
    elif choice_of_user == "off":
        in_service = False
        start = False
    else:
        if choice_of_user in MENU:

            #Check Resources
            ingredients = MENU[choice_of_user]["ingredients"]
            cost_of_coffee = MENU[choice_of_user]["cost"]

            #check if resources are enough to make the coffee
            for coffee_resource, valueCoffee in ingredients.items():
                if ingredients[coffee_resource] > resources[coffee_resource]:
                    #print(f"{coffee_resource} is not sufficient")
                    in_service = False
                else:
                    in_service = True

            #Process coins

            def fund_calculator(q, d, n, p):
                """Convert the coins in dollar and return the sum"""
                # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
                coins = {"quarters": 0.25, "dime": 0.10, "nickles": 0.05, "pennies": 0.01}
                quarter_in_dollar = operators.mlt(coins["quarters"], q)
                dime_in_dollar = operators.mlt(coins["dime"], d)
                nickels_in_dollar = operators.mlt(coins["nickles"], n)
                pennies_in_dollar = operators.mlt(coins["pennies"], p)
                fund = operators.add(operators.add(operators.add(pennies_in_dollar, nickels_in_dollar), dime_in_dollar),
                                     quarter_in_dollar)
                return fund


            def serving_coffee(right_condition):
                """Perform the service of the coffee if there are enough resources"""

                if right_condition:
                    print("Please insert coin")
                    #Record how much of each coin the machine receive
                    quarters_numb = float(input("How many quarters?\n"))
                    dime_numb = float(input("How many dime?\n"))
                    nickles_numb = float(input("How many nickles?\n"))
                    pennies_numb = float(input("How many pennies?\n"))
                    #Compute the user fund
                    user_fund = fund_calculator(quarters_numb, dime_numb, nickles_numb, pennies_numb)
                    print(f"You own ${user_fund}")
                    #TODO 4 - Check transaction successful

                    #decrease the volume of the ingredient into the machine
                    for key in ingredients:
                        resources[key] = resources.get(key) - ingredients.get(key)
                    print(f"These are the available resources : ")
                    for new_key, new_value in resources.items():
                        print(f"{new_key} : {new_value}")

                    # if the user fund is greater than his coffee price so variable user_change is positive
                    # the coffee is made and the change is calculated and given
                    user_change = operators.sub(user_fund, cost_of_coffee)
                    if user_change >= 0:
                        print("Hold your coffee")
                        print(f"And here is your change : ${user_change}")
                    else:
                        print("You don't have enough fund to buy this coffee")
                else:
                    print("Resources of the machine are not sufficient")


            serving_coffee(in_service)
            #ask if the user wants another coffee if not set start to False, 
            #or does he want tonsee the report? call function report and ask il he wants a coffee, 
            #think of a while loop
        #if the choice of coffee is not available
        else:
            print("Sorry we don't have this coffee")

print("GOOD BYE")