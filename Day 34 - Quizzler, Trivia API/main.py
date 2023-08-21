## Again modified from the base course, with a config file allowing for setting the amount and category of questions ##
## 31 is for weebs, 15 is for real gamers and 18 is for nerds setting the config category to -1 will leave it as any/all categories ##
## The max number of questions is 50 and also depends on the category ##
## I hope im not stressing out their API with these requests lmaoo ##

from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface
import requests
import json
from tkinter import messagebox

AMOUNT=10
INITIAL_AMOUNT=AMOUNT
CATEGORY=-1
## --------- CONFIG --------- ##
def generate_default_config():
    with open("config.json","w") as config_file:
        default_config_data={
            "amount": AMOUNT,
            "category": CATEGORY,
        }
        json.dump(default_config_data, config_file,indent=4)
def read_config():
    global AMOUNT,INITIAL_AMOUNT,CATEGORY
    try:
        with open("config.json","r") as config_file:
            try:
                config_data=json.load(config_file)
                AMOUNT=config_data["amount"]+1
                INITIAL_AMOUNT=config_data["amount"]
                CATEGORY=config_data["category"]
            except:
                messagebox.showerror(title="Error",message="config.json broken | You should replace it with a new one")
                print("config.json broken | You should replace it with a new one")
                generate_default_config()
    except:
        messagebox.showerror(title="Error",message=f"config.json not found/broken | Leaving the amount at {AMOUNT} & category as {CATEGORY}")
        print(f"config.json not found/broken | Leaving the amount at {AMOUNT} & category as {CATEGORY}")
        generate_default_config()
        
read_config()

## --------- REQUEST --------- ##
request_parameters={
    "type": "boolean",
    "amount": AMOUNT,
    "category": CATEGORY,
}
def update_request_parameters():
    global request_parameters
    request_parameters["amount"]=AMOUNT
    request_parameters["category"]=CATEGORY
    if CATEGORY==-1:
        del request_parameters["category"]
    print(f"Request parameters: {request_parameters}")

request_data={"response_code":1}
while request_data["response_code"]==1:
    AMOUNT-=1
    update_request_parameters()
    
    response = requests.get("https://opentdb.com/api.php",request_parameters)
    response.raise_for_status()
    
    request_data=response.json()
    question_data=request_data["results"]
    print(request_data)

if INITIAL_AMOUNT > 50:
    messagebox.showinfo(title="Yikes",message=f"The number of questions is capped at 50!")
if AMOUNT != INITIAL_AMOUNT:
    messagebox.showwarning(title="Yikes",message=f"Number of questions too high for this category!\nThe max is {AMOUNT}")

## --------- QUIZ --------- ##
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(f"Length of question bank: {len(question_bank)}\n")
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
