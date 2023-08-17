from turtle import Turtle
import random

SHAPE="turtle"
COLOR="#5e785d"
SIZE=0.5 # 1.0 is default for 20

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.setheading(90)
        self.shapesize(stretch_len=SIZE,stretch_wid=SIZE)
        self.color(COLOR)
        self.penup()
        self.speed(0)
        self.randpos()
    def randpos(self):
        rand_x=random.randint(-280,280)
        rand_y=random.randint(-280,280)
        self.goto(rand_x,rand_y)