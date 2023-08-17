
from turtle import Turtle

SIZE_LEN=1
SIZE_WID=5
MOVE_DISTANCE=20
COLOR="#84d07d"
UP=90
DOWN=270

class Paddle(Turtle):
    def __init__(self,posx):
        super().__init__()
        self.shape("square")
        self.color(COLOR)
        self.penup()
        self.shapesize(stretch_len=SIZE_LEN,stretch_wid=SIZE_WID)
        self.speed(6)
        self.goto(posx,0)
        
        
    def moveup(self):
        if(self.ycor()<250):
            self.goto(self.xcor(),self.ycor()+MOVE_DISTANCE)
    def movedown(self):
        if(self.ycor()>-250):
            self.goto(self.xcor(),self.ycor()-MOVE_DISTANCE)