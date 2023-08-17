from turtle import Turtle

POS_X=100
POS_Y=240
FONT=("Comic Sans MS", 24, "normal")
COLOR="#555a56"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scorePlayer1=0
        self.scorePlayer2=0
        self.hideturtle()
        self.penup()
        self.color(COLOR)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-POS_X,POS_Y)
        self.write(f"{self.scorePlayer1}", align="left", font=FONT)
        self.goto(POS_X,POS_Y)
        self.write(f"{self.scorePlayer2}", align="right", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
        
    def addscore_player1(self):
        self.scorePlayer1+=1
        self.update_scoreboard()
    def addscore_player2(self):
        self.scorePlayer2+=1
        self.update_scoreboard()