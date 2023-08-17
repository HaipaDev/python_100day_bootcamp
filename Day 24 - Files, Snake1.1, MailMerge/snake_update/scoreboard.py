from turtle import Turtle

POS_X=200
POS_Y=240
ALIGN="center"
FONT=("Comic Sans MS", 24, "normal")
COLOR="#555a56"
SAVEFILE="savefile"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.highscore=0
        self.hideturtle()
        self.penup()
        self.color(COLOR)
        self.goto(POS_X,POS_Y)
        self.load_highscore()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-POS_X,POS_Y)
        self.write(f"Score: {self.score}", align="left", font=FONT)
        self.goto(POS_X,POS_Y)
        self.write(f"Highscore: {self.highscore}", align="right", font=FONT)
        
    def reset_scoreboard(self):
        if(self.score>self.highscore):
            self.highscore=self.score
        self.score=0
        self.update_scoreboard()
        self.save_highscore()
        
    def addscore(self):
        self.score+=1
        self.update_scoreboard()
        
    def save_highscore(self):
        with open(SAVEFILE,mode="w") as file:
            file.write(f"{self.highscore}")
            file.close()
        
    def load_highscore(self):
        import os
        if(os.path.exists(SAVEFILE)):
            with open(SAVEFILE) as file:
                content=file.read()
                self.highscore=int(content)
                file.close()
        