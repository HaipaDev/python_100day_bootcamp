print("Welcome to the Corinthino Adventure!")
choice1=input("1 to go left, 2 to go right " )
if choice1=="1":
    print("There's a lake")
    choice2=input("1 to swim, 2 to wait for a boat " )
    if(choice2=="2"):
        choice3=input("Which door? 1 - Red, 2 - Yellow, 3 - Blue " )
        if(choice3=="2"): print("You have found korynt's kidney stones! You win!")
        elif(choice3=="1"): print("Nah bro you got burned")
        else: print("Monday left you broken")
    else: print("Nah you got eaten by the black fish")
else: print("Korynt literally ate your ass")