from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import random
#Turtle.colormode(255)
screen=Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
screen.bgcolor("#252b25")
screen.title("HyperSnake")

snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.update()
screen.listen()

screen.onkey(key="w",fun=snake.up)
screen.onkey(key="s",fun=snake.down)
screen.onkey(key="a",fun=snake.left)
screen.onkey(key="d",fun=snake.right)

BOUNDARIES=280

def reset():
    time.sleep(0.2)
    snake.reset()
    scoreboard.reset_scoreboard()

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    ## Detect collision with food
    if(snake.head.distance(food)<=15):
        scoreboard.addscore()
        food.randpos()
        snake.add_segment()
    
    ## Detect collision with wall
    if((snake.head.xcor()>BOUNDARIES or snake.head.xcor()<-BOUNDARIES) or (snake.head.ycor()>BOUNDARIES or snake.head.ycor()<-BOUNDARIES)):
        reset()
        
    ## Detect collision with tail
    for seg in snake.segments[1:]:
        if(snake.head.distance(seg)<10):
            reset()

    
screen.exitonclick()