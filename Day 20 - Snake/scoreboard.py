from turtle import Turtle

POS_X=0
POS_Y=240
ALIGN="center"
FONT=("Comic Sans MS", 24, "normal")
COLOR="#555a56"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.color(COLOR)
        self.goto(POS_X,POS_Y)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
        
    def addscore(self):
        self.score+=1
        self.update_scoreboard()