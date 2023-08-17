############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

## "Oczko" would be that jack is 2, queen is 3 and king is 4 and ace is always 11
## cards = [2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11]
## Alternative "Oczko" is from 9 to ace and 9 is worth 0
## cards = [2, 3, 4, 0, 10, 11]

###############

import subprocess ##subprocess.run('cls',shell=True)##
import random
from art import logo

decks = {
    "blackjack":[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
    "oczko":[2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11],
    "alt-oczko":[2, 3, 4, 0, 10, 11],
}
deck_selected=""
cards=[]
your_cards=[]
your_score=0
cpu_cards=[]
cpu_score=0
newGame=True
continueGame=True
firstGameFinished=False

#region Functions
def deal_card():
    return cards[random.randint(0,len(cards)-1)]
def player_get_card():
    your_cards.append(deal_card())
def cpu_get_card():
    cpu_cards.append(deal_card())

def calculate_score(carddeck):
    if(deck_selected=="blackjack"):
        if(11 in carddeck and sum(carddeck)>21):
            carddeck.remove(11)
            carddeck.append(1)
    # if(deck_selected=="oczko" or deck_selected=="alt-oczko"):
    #     ace_count=0
    #     for carddeck in carddeck:
    #         if(carddeck==11): ace_count+=1
    #     if(ace_count==2):
    #         print("you won")
    return sum(carddeck)
def calculate_your_score():
    global your_score
    your_score=calculate_score(your_cards)
def calculate_cpu_score():
    global cpu_score
    cpu_score=calculate_score(cpu_cards)
def select_deck(deck_name):
    global deck_selected,cards
    if(deck_name=="o"):
        deck_selected="oczko"
    elif(deck_name=="a"):
        deck_selected="alt-oczko"
    elif(deck_name=="d" or deck_name=="b"):
        deck_selected="blackjack"
    cards=decks[deck_selected]

def start_game():
    player_get_card()
    player_get_card()
    calculate_your_score()
    cpu_get_card()
    cpu_get_card()
    calculate_cpu_score()
    if(your_score>=21 or cpu_score==21 or (cpu_score==22 and deck_selected!="blackjack")):
        round_end()
def reset():
    global your_cards,cpu_cards,continueGame
    your_cards=[]
    cpu_cards=[]
    continueGame=True
def round_end():
    global continueGame,firstGameFinished
    continueGame=False
    firstGameFinished=True
    #print(compare())

def compare():
    if((your_score > 21 and cpu_score > 21) and deck_selected=="blackjack"):
        return "You went over. You lose 😤"
    if(((len(your_cards)>2 and your_score > 21) and (len(cpu_cards)>2 and cpu_score > 21)) and deck_selected!="blackjack"):
        return "You went over. You lose 😤"
  
    if your_score == cpu_score:
        return "Draw 🫡"
    elif cpu_score == 21:
        return "Lose, opponent has Blackjack 😱"
    elif (your_score == 21):
        return "Win with a Blackjack 😎"
    elif (len(your_cards)==2 and your_score==22 and (deck_selected!="blackjack")):
        return "Win with a Persian Ace 😎"
    elif (len(cpu_cards)==2 and cpu_score==22 and (deck_selected!="blackjack")):
        return "Lose, opponent has a Persian Ace 😱"
    elif ((your_score > 21 and deck_selected=="blackjack") or (len(your_cards)>2 and your_score > 21 and deck_selected!="blackjack")):
        return "You went over. You lose 💀"
    elif ((cpu_score > 21 and deck_selected=="blackjack") or (len(cpu_cards)>2 and cpu_score > 21 and deck_selected!="blackjack")):
        return "Opponent went over. You win 😁"
    elif your_score > cpu_score:
        return "You win 🗣️"
    else:
        return "You lose 😤"
# def printFinalResult():
#     if((your_score<=21 and your_score>cpu_score) or cpu_score>21): print("You won!🗣️")
#     elif(your_score==cpu_score and your_score<21 and cpu_score<21): print("Draw.🫡")
#     elif((cpu_score<=21 and cpu_score>your_score) or your_score>21): print("You lost.💀")
#endregion

#region Game Logic
while(newGame):
    if(not firstGameFinished):
        deck_selected="blackjack"
        play_question=input("Do you want to play a game of Blackjack?: ")
    else:
        play_question=input("Do you want to play another round?: ")
    subprocess.run('cls',shell=True)
    reset()

    if(play_question=="" or play_question=="y" or play_question=="Y" or play_question=="yes" or play_question=="Yes"):
        print(f"Do you want to change the rules? Current ruleset is: {deck_selected}\n")
        print("The default 'blackjack' set of cards consists of: ")
        print(f"    {decks['blackjack']}")
        print("The set for 'oczko' consists of: ")
        print(f"    {decks['oczko']}")
        print("The set for 'alt-oczko' consists of (9 is worth 0): ")
        print(f"    {decks['alt-oczko']}")
        print("And in both 'Oczko' rules Ace is always worth 11\nand a double ace; so called Persian Ace is considered a win even though the score sums up to 22")
        print("\n(skip for current/default rules, 'd' or 'b' for blackjack")
        select_deck(input("'o' for oczko or 'a' for alternative oczko): "))

        start_game()
        print(logo)
        print(f"Ruleset chosen is: {deck_selected}")#{decks.keys[deck_id_selected]}")
        #print(f"Deck consists of: {cards}")
        while(continueGame):
            print(f"    Your cards: {your_cards}, current score: {your_score}")
            print(f"    Computers first card: {cpu_cards[0]}")

            get_card=input("Type 'y' to get another card, type 'n' to pass: ")
            if(get_card=="" or get_card=="y" or get_card=="Y" or get_card=="yes" or get_card=="Yes"):
                player_get_card()
                if(cpu_score<17):cpu_get_card()
                calculate_your_score()
                calculate_cpu_score()
            else:
                round_end()
            if(your_score>=21 or cpu_score==21 or (cpu_score==22 and deck_selected!="blackjack")):
                round_end()
        print(f"    Your cards: {your_cards}, final score: {your_score}")
        print(f"    Computers cards: {cpu_cards}, final score: {cpu_score}")
        print(compare())
        #printFinalResult()
    else:
        newGame=False
print("Thank you for playing C: ")
#endregion