from turtle import Turtle
import random
#COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
COLORS = ["#a73428", "#c1492c", "#ebd477", "#bdc039", "#43a29c", "#572d42"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.movespeed=STARTING_MOVE_DISTANCE
    
    def create_car(self):
        rand_chance=random.randint(1,6)
        if(rand_chance==1):
            new_car=Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.speed(0)
            rand_y=random.randint(-250,250)
            new_car.goto(300,rand_y)
            new_car.speed(6)
            self.all_cars.append(new_car)
        
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.movespeed)
            if(car.xcor()<-340):
                self.all_cars.remove(car)
            
    def levelup(self):
        self.movespeed+=MOVE_INCREMENT