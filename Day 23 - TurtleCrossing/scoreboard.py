from turtle import Turtle
import random
FONT = ("Comic Sans MS", 24, "normal")
FONT_GAMEOVER = ("Comic Sans MS", 48, "normal")
COLOR="#ebddda"

class Scoreboard(Turtle):
    def __init__(self):
        self.level=1
        
        super().__init__()
        self.hideturtle()
        self.color(COLOR)
        self.penup()
        self.speed(0)
        self.goto(-270,250)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT_GAMEOVER)
        
    def addlevel(self):
        self.level+=1
        self.update_scoreboard()