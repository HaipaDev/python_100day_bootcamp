from turtle import Turtle

MOVE_DISTANCE=20
COLOR="#84d07d"
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
        
    def add_segment(self,append=True):
        new_segment=Turtle(shape="square")
        new_segment.color(COLOR)
        new_segment.penup()
        new_segment.speed(6)
        if(len(self.segments)>1):
            new_segment.goto(self.segments[len(self.segments)-1].xcor(),self.segments[len(self.segments)-1].ycor())
        if(append):
            self.segments.append(new_segment)
        return new_segment
    
    def create_snake(self):
        for i in range(3):
            new_segment=self.add_segment(append=False)
            if(i>0):
                new_segment.goto(self.segments[i-1].xcor()-20,0)
            self.segments.append(new_segment)
            
        self.head=self.segments[0]
        
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        
    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            _x=self.segments[i-1].xcor()
            _y=self.segments[i-1].ycor()
            self.segments[i].goto(_x,_y)
        self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        if(self.head.heading()!=DOWN):
            self.head.setheading(UP)
    def down(self):
        if(self.head.heading()!=UP):
            self.head.setheading(DOWN)
    def left(self):
        if(self.head.heading()!=RIGHT):
            self.head.setheading(LEFT)
    def right(self):
        if(self.head.heading()!=LEFT):
            self.head.setheading(RIGHT)