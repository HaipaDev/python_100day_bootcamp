import turtle as t
import random
t.colormode(255)
t.hideturtle()
screen=t.Screen()
screen.setup(width=500,height=400)

user_bet=t.textinput("Make your bet!","Which turtle will rin the race? Enter a color: ")

timmies=[]
colors=["red","orange","yellow","green","blue","purple"]
for i in range(6):
    new_turtle=t.Turtle(shape="turtle")
    new_turtle.speed(8)
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(-((screen.window_width()/2)-20),(-100+(30*i)))
    timmies.append(new_turtle)

if user_bet:
    is_race_on=True
    
while(is_race_on):
    for turtle in timmies:
        if(turtle.xcor()>((screen.window_width()/2)-20)):
            is_race_on=False
            winning_color=turtle.pencolor()
            if(winning_color==user_bet):
                print("You've won!")
            else:
                print("You've lost.")
            print(f"The {winning_color} turtle is the winner!")
        
        t.speed(6)
        turtle.forward(random.randint(2,5))




screen.exitonclick()