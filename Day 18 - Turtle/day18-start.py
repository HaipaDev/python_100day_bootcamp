# import subprocess
# module_name = "Turtle"
# subprocess.run(["pip", "install", module_name])

import turtle as t
import random
tim=t.Turtle()

tim.shape("turtle")
tim.color("aquamarine4")

## Square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

## Dashed Line
# for _ in range(20):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

## Triangle
# for _ in range(3):
#     tim.forward(40)
#     tim.right(360/3)
    
## Pentagon
# for _ in range(5):
#     tim.forward(40)
#     tim.right(360/5)
    
## Hexagon
# for _ in range(6):
#     tim.forward(40)
#     tim.right(360/6)

## Heptagon
# for _ in range(7):
#     tim.forward(40)
#     tim.right(360/7)
    
## Octagon
# for _ in range(8):
#     tim.forward(30)
#     tim.right(360/8)

## Nonagon
# for _ in range(9):
#     tim.forward(30)
#     tim.right(360/9)

## Decagon
# for _ in range(10):
#     tim.forward(30)
#     tim.right(360/10)

colors=["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]
t.colormode(255)

def draw_shape(num_sides):
    angle=360/num_sides
    for _ in range(num_sides):
        tim.forward(50)
        tim.right(angle)

def draw_shapes_in_succession():
    for n in range(3,11):
        tim.color(random.choice(colors))
        draw_shape(n)
        
        
directions=[0,90,180,270]
def random_walk(steps=200):
    tim.shape("arrow")
    tim.pensize(15)
    tim.speed(0)
    for i in range(steps):
        #tim.color(random.choice(colors))
        tim.color(get_random_color())
        tim.forward(20)
        tim.setheading(random.choice(directions))
        
def get_random_color():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        
def manji():
    tim.shape("arrow")
    tim.pensize(15)
    #tim.speed(0)
    tim.color("gold")
    for j in range(4):
        tim.forward(40)
        tim.left(90)
        tim.forward(40)
        tim.right(180)
        
        tim.forward(40)
        tim.right(90)
        tim.forward(40)
        tim.left(180)
        tim.right(90)

def swastika():
    tim.shape("arrow")
    tim.pensize(15)
    #tim.speed(0)
    tim.color("red")
    for j in range(4):
        tim.forward(40)
        tim.right(90)
        tim.forward(40)
        tim.left(180)
        
        tim.forward(40)
        tim.left(90)
        tim.forward(40)
        tim.right(180)
        tim.left(90)
        
def sprirograph(size_of_gap=10):
    tim.shape("arrow")
    tim.speed(0)
    for _ in range(int(360/size_of_gap)):
        tim.color(get_random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)


#random_walk()
sprirograph()



screen=t.Screen()
screen.exitonclick()