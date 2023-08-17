import random
playerChoice = int(input("\nChoose 1 for rock, 2 for paper, 3 for scissors: "))-1
# 0 for rock, 1 for paper, 2 for scissors
cpuChoice = random.randint(0, 2)
playerWon=False

if (playerChoice==0):  print("You chose rock.")
if (playerChoice==1):  print("You chose paper.")
if (playerChoice==2):  print("You chose scissors.")

if (cpuChoice==0):  print("Computer chose rock!")
if (cpuChoice==1):  print("Computer chose paper!")
if (cpuChoice==2):  print("Computer chose scissors!")

if (playerChoice==0 and cpuChoice==1):
    playerWon=False
elif (playerChoice==0 and cpuChoice==2):
    playerWon=True
elif (playerChoice==1 and cpuChoice==0):
    playerWon=True
elif (playerChoice==1 and cpuChoice==2):
    playerWon=False
elif (playerChoice==2 and cpuChoice==0):
    playerWon=False
elif (playerChoice==2 and cpuChoice==1):
    playerWon=True

if((playerChoice==0 and cpuChoice==0) or (playerChoice==1 and cpuChoice==1) or (playerChoice==2 and cpuChoice==2)):
    playerWon=False
    print("It's a draw!")
else:
    if(playerWon): print("Player Won!")
    else: print("Player Lost!")
