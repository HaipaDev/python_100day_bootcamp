from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import random
#Turtle.colormode(255)
screen=Screen()
screen.setup(width=800,height=600)
screen.tracer(0)
screen.bgcolor("#252b25")
screen.title("HyperPong")

paddle1=Paddle(-350)
paddle2=Paddle(350)
ball=Ball()
scoreboard=Scoreboard()
screen.update()
screen.listen()


screen.onkeypress(key="w",fun=paddle1.moveup)
screen.onkeypress(key="s",fun=paddle1.movedown)
screen.onkeypress(key="Up",fun=paddle2.moveup)
screen.onkeypress(key="Down",fun=paddle2.movedown)

game_is_on=True
time.sleep(0.5)
while game_is_on:
    screen.update()
    time.sleep(ball.sleepspeed)
    ball.move()
    
    ## Detect collision with ball
    if(paddle1.distance(ball)<50 and ball.xcor()<340):
        ball.bounce_paddle()
    if(paddle2.distance(ball)<50 and ball.xcor()>340):
        ball.bounce_paddle()
        
    ## Detect ball collision with wall
    if(ball.ycor()<=-290 or ball.ycor()>=290):
        ball.bounce_wall()
        
    ## Detect ball collision with goalie
    if(ball.xcor()<=-410):
        scoreboard.addscore_player2()
        ball.reset()
    elif(ball.xcor()>=410):
        scoreboard.addscore_player1()
        ball.reset()


screen.exitonclick()