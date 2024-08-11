from utils import *

in_service = True
profit = 0
start = True

while start:
    choice_of_user = input("What would you like? (espresso/latte/cappuccino): \n"
                           "****************************** FOR MAINTENANCE**********************************\n"
                           "Type 'report' : to see the resources \n"
                           
                           "Type 'Off' : to switch the machine off \n"
                           
                           "Type 'profit' : to see the profit made\n ").lower()
    if choice_of_user == "report":
        report()
    elif choice_of_user == "off":
        in_service = False
        start = False
    else:
        if choice_of_user in MENU:
            # Check Resources
            ingredients = MENU[choice_of_user]["ingredients"]
            cost_of_coffee = MENU[choice_of_user]["cost"]

            # check if resources are enough to make the coffee
            for coffee_resource, valueCoffee in ingredients.items():
                if ingredients[coffee_resource] > resources[coffee_resource]:
                    # print(f"{coffee_resource} is not sufficient")
                    in_service = False
                else:
                    in_service = True
            #Process coins and serve the coffee
            serving_coffee(in_service, choice_of_user)
            profit += cost_of_coffee
        #if the choice of coffee is not available
        else:
            print("Sorry we don't have this coffee")

print("GOOD BYE")
