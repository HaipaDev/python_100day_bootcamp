age=int(input("What is your age? \n"))
yearsRemaining=90-age
weeksInYear=52
weeksLeft=yearsRemaining*weeksInYear
daysLeft=weeksLeft*7
print(f"You have {weeksLeft} weeks left, and {daysLeft} days left to live")