# import subprocess
# ## Install pandas if its not already installed
# module_name = "pandas"
# subprocess.run(["pip", "install", module_name])
import pandas

import turtle

screen=turtle.Screen()
screen.setup(width=725,height=491)
screen.title("US States Game")
DATA_PATH="50_states.csv"
IMG_PATH="./blank_states_img.gif"
screen.addshape(IMG_PATH)
turtle.shape(IMG_PATH)


data=pandas.read_csv(DATA_PATH)
states_data=data.state
states_list=states_data.to_list()

guessed_states=[]
while len(guessed_states)<50:
    answer_state=screen.textinput(title=f"Guess the State {len(guessed_states)}/{len(states_list)}", prompt="What's another state name?").title()
    if(answer_state=="Exit"):
        missing_states=[]
        for state in states_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if(answer_state in states_list and (not answer_state in guessed_states)):
        state=data[data.state==answer_state]
        guessed_states.append(answer_state)
        text=turtle.Turtle()
        text.hideturtle()
        text.penup()
        text.speed(0)
        text.goto(int(state.x),int(state.y))
        text.write(answer_state)