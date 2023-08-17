import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password=""

print("\nWelcome to the PyPass Generator!")
lettersCount=int(input("How many letters would you like in your password? "))
numbersCount=int(input("How many numbers would you like? "))
symbolsCount=int(input("How many symbols would you like? "))
totalCount=lettersCount+numbersCount+symbolsCount
print("Your password's length sums up to: ",totalCount)

randomLetter=letters[random.randint(0,len(letters)-1)]
randomNumber=numbers[random.randint(0,len(numbers)-1)]
randomSymbols=symbols[random.randint(0,len(symbols)-1)]

# totalAmount=0
# lettersAmount=0
# numbersAmount=0
# symbolsAmount=0
# if(totalAmount<totalCount):
#     for i in range(0,totalCount):
#         totalAmount+=1
#         signType=random.randint(0,2)
#         if(signType==0 and lettersAmount<lettersCount):
#             randomSign=random.choice(letters)
#             lettersAmount+=1
#         elif(signType==2 and numbersAmount<numbersCount):
#             randomSign=random.choice(numbers)
#             numbersCount+=1
#         elif(signType==1 and symbolsAmount<symbolsCount):
#             randomSign=random.choice(symbols)
#             symbolsCount+=1
#         password+=randomSign
password_list=[]
for i in range(1,lettersCount+1):
    password_list.append(random.choice(letters))
for i in range(1,numbersCount+1):
    password_list.append(random.choice(numbers))
for i in range(1,symbolsCount+1):
    password_list.append(random.choice(symbols))
print(password_list)
random.shuffle(password_list)
print(password_list)
for i in range(1,len(password_list)):
    password+=password_list[i]
print(password)