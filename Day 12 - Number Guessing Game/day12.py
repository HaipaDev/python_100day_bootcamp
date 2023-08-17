import random

randomNumber=random.randint(1,100)
lives_easy=10
lives_hard=5
lives=lives_easy
diff="easy"
game_over=False
newGame=True

def compare(guess):
    global game_over
    if(guess<randomNumber): return "Too low."
    elif(guess>randomNumber):   return "Too high."
    else:
        game_over=True
        return "You got it!"

def set_difficulty(difficulty):
    global diff,lives
    if(difficulty=="hard" or difficulty=="h" or difficulty=="hc"):
        diff="hard"
        lives=lives_hard
    elif(difficulty=="easy" or difficulty=="e" or difficulty=="ez"):
        diff="easy"
        lives=lives_easy
def reset():
    global randomNumber,lives
    randomNumber=random.randint(1,100)
    if(diff=="hard"):   lives=lives_hard
    else:   lives=lives_easy

def game_logic():
    global lives,game_over,newGame
    print("Welcome to the Number Guessing Game!")

    while(newGame):
        print("Im thinking of a number between 1 and 100")
        print(f"Psst, the correct answer is {randomNumber}")
        set_difficulty(input("Choose a difficulty. Type 'e' for easy or 'h' for hard: "))

        while(not game_over):
            print("\n")
            print(f"You have {lives} attempts remaining.")
            guess=0
            guessMessage=""
            while(not guessMessage.isnumeric()):
                guessMessage=input("Make a guess: ")
            guess=int(guessMessage)
            print(compare(guess))
            if(lives>1):
                lives-=1
            else:
                print("You have failed :C")
                game_over=True
        retry_input=input("Would you like another go?")
        if(retry_input=="" or retry_input=="y" or retry_input=="Y" or retry_input=="yes" or retry_input=="Yes"):
            reset()
            game_over=False
            newGame=True
        else:
            newGame=False

game_logic()