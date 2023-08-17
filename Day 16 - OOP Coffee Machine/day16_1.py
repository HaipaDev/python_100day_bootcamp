from turtle import Turtle, Screen

timmy=Turtle()
timmy.shape("turtle")
timmy.color("aquamarine4")
timmy.forward(100)

my_screen=Screen()
print(f"{my_screen.canvheight} x {my_screen.canvwidth}")
my_screen.exitonclick()