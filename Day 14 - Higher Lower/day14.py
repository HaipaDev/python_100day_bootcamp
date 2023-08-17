import random
import subprocess ##subprocess.run('cls',shell=True)##
from game_data import data
from art import logo
from art import vs

compareA=data[random.randint(0,len(data)-1)]
compareB=data[random.randint(0,len(data)-1)]
score=0
_guessedCorrectly=False
game_over=False

def get_current_score_message():
    global _guessedCorrectly
    if(_guessedCorrectly):
        _guessedCorrectly=False
        return f"You're right! Current score: {score}"
    if(game_over):
        return f"Sorry, that's wrong Final score: {score}"
    return "\n"
def compare(compareInput):
    global compareA,compareB,score,game_over,_guessedCorrectly
    higherchosen={}
    if(compareInput=="b" or compareInput=="B" or compareInput=="2"):
        higherchosen=compareB
        lowerchosen=compareA
    else:
        higherchosen=compareA
        lowerchosen=compareB

    if(higherchosen["follower_count"]>lowerchosen["follower_count"]):
        _guessedCorrectly=True
        score+=1
        compareA=compareB
        compareB=data[random.randint(0,len(data)-1)]
    else:
        game_over=True

def game_logic():
    while(not game_over):
        print(logo)
        print(get_current_score_message())
        print(f'Compare A: {compareA["name"]}, a {compareA["description"]}, from {compareA["country"]}')
        print(f"\n{vs}\n")
        print(f'Compare B: {compareB["name"]}, a {compareB["description"]}, from {compareB["country"]}')

        compareInput="-"
        while((compareInput!="" and compareInput!="1" and compareInput!="a" and compareInput!="A") and (compareInput!="2" and compareInput!="b" and compareInput!="B")):
            compareInput=input("Who has more followers? Type ('A' or '1') or ('B' or '2'): ")
        compare(compareInput)
    #After game over
    print(logo)
    print(get_current_score_message())

    
game_logic()