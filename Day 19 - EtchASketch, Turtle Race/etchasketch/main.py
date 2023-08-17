import turtle as t
tim=t.Turtle()
screen=t.Screen()
screen.listen()

def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def rot_left():
    tim.setheading(tim.heading()+10)
def rot_right():
    tim.setheading(tim.heading()-10)
def reset():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()
    

screen.onkeypress(key="w",fun=move_forwards)
screen.onkeypress(key="s",fun=move_backwards)
screen.onkeypress(key="a",fun=rot_left)
screen.onkeypress(key="d",fun=rot_right)
screen.onkeypress(key="c",fun=reset)

screen.exitonclick()