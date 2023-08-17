print("Thank you for ordering at Los Pollos Hermanos, lets calculate the tip")
billAmount=float(input("What was the total bill? $"))
percentage=int(input("What percentage tip would you like to give? 10, 12, or 15%? "))
peopleToSplit=int(input("How many people to split the bill? "))

tipFromBill=round(billAmount*percentage/100,2)
totalBill=round(billAmount+tipFromBill,2)
toPayForEach=round(totalBill/peopleToSplit,2)

totalBill_formatted="{:.2f}".format(totalBill)
toPayForEach_formatted="{:.2f}".format(toPayForEach)

print(f"\nThe total bill comes down to ${totalBill_formatted} & each person should pay: ${toPayForEach_formatted}")