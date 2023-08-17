from turtle import Turtle
import random

SHAPE="circle"
COLOR="#5e785d"
SIZE=1 # 1.0 is default for 20
SPEED=30
SLEEPSPEED_DEF=0.05
BOUNCE_SPEED_INCREMENT=0.9

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.setheading(90)
        self.shapesize(stretch_len=SIZE,stretch_wid=SIZE)
        self.color(COLOR)
        self.penup()
        self.speed(6)
        self.x_move=10
        self.y_move=10
        self.sleepspeed=SLEEPSPEED_DEF
        self.randomize_direction()
    
    def move(self):
        _x=self.xcor()+self.x_move
        _y=self.ycor()+self.y_move
        self.goto(_x,_y)
        
    def bounce_y(self):
        self.y_move*=-1
    def bounce_x(self):
        self.x_move*=-1
        
    def bounce_wall(self):
        self.bounce_y()
    def bounce_paddle(self):
        self.bounce_y()
        self.bounce_x()
        self.sleepspeed*=BOUNCE_SPEED_INCREMENT
    
    def reset(self):
        self.speed(0)
        self.goto(0,0)
        self.speed(6)
        #self.randomize_direction()
        self.bounce_paddle()
        self.sleepspeed=SLEEPSPEED_DEF
        
    def randomize_direction(self):
        x_randMult=1
        rand=random.randint(1,2)
        if(rand==2):
            x_randMult=-1
        self.x_move*=x_randMult
        y_randMult=1
        rand=random.randint(1,2)
        if(rand==2):
            y_randMult=-1
        self.y_move*=y_randMult