import random

print("\nLet's roll who pays the bill!")
names_string=input("Give me everybody's name, seperated by a comma: \n")
names=names_string.split(", ")

randomNum=random.randint(0,len(names)-1)
personChosen=names[randomNum]
# personChosen=random.choice(names)
print(f"{personChosen} is paying the bill!")