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
coins=[0.01,0.05,0.10,0.25]

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money=0.0

def process_coins():
    print("Please insert coins.")
    quartersMessage=""
    while(not quartersMessage.isnumeric()):
        quartersMessage=input("How many quarters(0.25)?: ")
    quarters=int(quartersMessage)

    dimesMessage=""
    while(not dimesMessage.isnumeric()):
        dimesMessage=input("How many dimes(0.10)?: ")
    dimes=int(dimesMessage)

    nicklesMessage=""
    while(not nicklesMessage.isnumeric()):
        nicklesMessage=input("How many nickles(0.05)?: ")
    nickles=int(nicklesMessage)

    penniesMessage=""
    while(not penniesMessage.isnumeric()):
        penniesMessage=input("How many pennies(0.01)?: ")
    pennies=int(penniesMessage)

    total=((0.25*quarters)+(0.1*dimes)+(0.05*nickles)+(0.01*pennies))
    return total


def calculate_order(typeMessage,money_inserted):
    global resources,money
    _type=""
    if(typeMessage=="espresso" or typeMessage=="e" or typeMessage=="1"):
        _type="espresso"
    elif(typeMessage=="latte" or typeMessage=="l" or typeMessage=="2"):
        _type="latte"
    elif(typeMessage=="cappuccino" or typeMessage=="c" or typeMessage=="3"):
        _type="cappuccino"
    
    ingredients=MENU[_type]["ingredients"]
    cost=MENU[_type]["cost"]
    if(money_inserted>=cost):
        for item in ingredients:
            if(resources[item]<ingredients[item]):
                print(f"Sorry there is not enough {item}.")
                return False
            else:
                order_coffee(_type,money_inserted)
                return True
    else:
        print("Sorry that's not enough money. Refunded.")
        return False

def order_coffee(_type,money_inserted):
    global money
    ingredients=MENU[_type]["ingredients"]
    cost=MENU[_type]["cost"]

    for item in ingredients:
        resources[item]-=ingredients[item]
    money+=cost
    change=round(money_inserted-cost,2)
    print(f"Here is ${change} in change.")
    print(f"Here is your {_type}. Enjoy!")

def give_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

is_on=True
while(is_on):
    typeMessage=""
    while(typeMessage!="espresso" and typeMessage!="e" and typeMessage!="1" and 
    (typeMessage!="latte" and typeMessage!="l" and typeMessage!="2") and 
    (typeMessage!="cappuccino" and typeMessage!="c" and typeMessage!="3")and
    (typeMessage!="report" and typeMessage!="raport" and typeMessage!="r" and typeMessage!="0")
    and (typeMessage!="o" and typeMessage!="off")):
        typeMessage=input("\nWhat would you like? (espresso/latte/cappuccino) | (e/l/c) | (1/2/3) || (report / r): ")
        if(typeMessage=="report" or typeMessage=="report" or typeMessage=="r" or typeMessage=="0"):
            give_report()
            typeMessage=""
        elif(typeMessage=="o" or typeMessage=="off"):
            is_on=False

    money_inserted=process_coins()
    calculate_order(typeMessage,money_inserted)