from turtle import Turtle,Screen
timmy = Turtle()
timmy.color("royal blue")
timmy.shape("circle")
timmy.fillcolor("dark olive green")
for i in range(4):
    timmy.forward(200)
    timmy.left(90)

screen=Screen()
screen.exitonclick()