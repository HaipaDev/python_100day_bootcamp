import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("#c9bcb4")
screen.title("TurtleCrossing")

player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()
screen.update()
screen.listen()

screen.onkeypress(key="w",fun=player.move_up)

game_is_on = True
time.sleep(0.2)
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()

    # Detect player collision with finish goal
    if(player.ycor()>280):
        player.reset()
        scoreboard.addlevel()
        car_manager.levelup()
    
    for car in car_manager.all_cars:
        if(player.distance(car)<20):
            game_is_on=False
            scoreboard.game_over()
            
screen.exitonclick()