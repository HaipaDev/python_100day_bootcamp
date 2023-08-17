import random

#word_list = ["ardvark", "baboon", "camel"]
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
incorrect_guesses=[]

from hangman_art import logo
print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"
print(f"{''.join(display)}")

from hangman_art import stages
while(not end_of_game):
    if(len(incorrect_guesses)>0): print(f"Incorrect guesses: {' '.join(incorrect_guesses)}")
    guess=input("Guess a letter: ").lower()
    if(guess in display):
        print(f"You have already guessed {guess}.🤓")
    for i in range(word_length):
        print(f"Current position: {i} | Current letter: {chosen_word[i]} | Guess: {guess}  | Lives: {lives}")
        if(chosen_word[i]==guess):
            display[i]=guess
    if(guess not in chosen_word):
        if(guess not in incorrect_guesses):
            incorrect_guesses+=guess
            print(f"{guess} is not inside of the word!🫡")
            if(lives>0):lives-=1
            if(lives<=0):end_of_game=True
        else:
            print(f"You have already guessed {guess} and it was incorrect.🤓")
    print(stages[lives])
    print(f"\n{''.join(display)}")

    if("_" not in display):
        end_of_game=True
if(end_of_game):
    if(lives>0):print("YOU WON!🥹")
    else:print("💀💀💀")