from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()

coffee_maker.report()
money_machine.report()

is_on=True
while(is_on):
    #options=menu.get_items()
    #choice=input(f"What would you like? ({options})")
    
    typeMessage=""
    while(typeMessage!="espresso" and typeMessage!="e" and typeMessage!="1" and 
    (typeMessage!="latte" and typeMessage!="l" and typeMessage!="2") and 
    (typeMessage!="cappuccino" and typeMessage!="c" and typeMessage!="3")and
    (typeMessage!="report" and typeMessage!="raport" and typeMessage!="r" and typeMessage!="0")
    and (typeMessage!="o" and typeMessage!="off")):
        typeMessage=input("\nWhat would you like? (espresso/latte/cappuccino) | (e/l/c) | (1/2/3) || (report / r): ")
    
    if(typeMessage=="report" or typeMessage=="raport" or typeMessage=="r" or typeMessage=="0"):
        coffee_maker.report()
        money_machine.report()
        typeMessage=""
    elif(typeMessage=="o" or typeMessage=="off"):
        is_on=False
    else:
        drink=menu.find_drink(typeMessage)
        if(coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost)):
            coffee_maker.make_coffee(drink)