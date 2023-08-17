from turtle import Turtle
import random
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
COLOR="#846e5a"

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.color(COLOR)
        self.penup()
        self.speed(0)
        self.reset()

    def reset(self):
        self.goto(0,-280)
        self.speed(6)
        
    def move_up(self):
        self.forward(MOVE_DISTANCE)
