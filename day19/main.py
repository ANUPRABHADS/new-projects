from turtle import Turtle,Screen
tim=Turtle()
tim.speed(1)
def forward():
    tim.forward(10)
def backward():
    tim.backward(10)
def counter_clock():
    new = tim.heading() + 10
    tim.setheading(new)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def clockwise():
    new = tim.heading() - 10
    tim.setheading(new)


screen=Screen()
screen.listen()
screen.onkey(forward, "w")
screen.onkey(backward, "s")
screen.onkey(counter_clock, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear, "c")
screen.exitonclick()

