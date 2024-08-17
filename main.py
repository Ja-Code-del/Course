import menu
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#print report
barista = CoffeeMaker()
money_machine = MoneyMachine()
my_menu = Menu()


user_choice = input("Hello welcome on my super coffee machine\nType 'report' to get the values of available resource\n"
                    "Or simply type in the name of the coffe you want").lower()

if user_choice == 'report':
    print("AVAILABLE RESOURCES ARE :\n")
    barista.report()

elif user_choice in my_menu.get_items():
    #create a MenuItem called coffee_choice with the function find_drink
    coffee_choice = my_menu.find_drink(user_choice)
    # Check resources
    if barista.is_resource_sufficient(coffee_choice):
        print("Can make your coffee")
    else:
        print("Sorry Resources are not sufficient to make this coffee")

    # Process coins
    #Check transaction successful
    if money_machine.make_payment(coffee_choice.cost):
        #Serve coffee and ask if user wants another one
        barista.make_coffee(coffee_choice)
