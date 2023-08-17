import subprocess
module_name = "colorgram.py"
subprocess.run(["pip", "install", module_name])

import turtle as t
import colorgram
import random
tim=t.Turtle()
t.colormode(255)

colors_extracted=colorgram.extract("image.jpg",30)
colors=[]
for col in colors_extracted:
    c=col.rgb
    colors.append((c.r,c.g,c.b))
#print(colors)

#def hirst_painting(x,y):
def hirst_painting(number_of_dots):
    tim.penup()
    tim.hideturtle()
    tim.speed(0)
    # pos=tim.pos()
    # tim.setposition(0,0)
    # for _y in range(y):
    #     for _x in range(x):
    #         tim.dot(10,random.choice(colors))
    #         tim.setposition(pos.x+10,pos.y)
    #     tim.setposition(pos.x,pos.y+10)
    
    # tim.setheading(225)
    # tim.forward(300)
    # tim.setheading(0)
    tim.setposition(-230,-230)
    for dot_count in range(1,number_of_dots+1):
        tim.dot(20,random.choice(colors))
        tim.forward(50)
        
        if(dot_count%10==0):
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)

#hirst_painting(10,10)
hirst_painting(100)

screen=t.Screen()
screen.exitonclick()