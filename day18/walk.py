from turtle import Turtle,Screen
import random
tim=Turtle()
tim.speed(10)
tim.pen(fillcolor="medium slate blue", pencolor="deep pink", pensize=5)
colour=["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
        "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction=[0,90,180,270]
for i in range(100):
    tim.color(random.choice(colour))
    tim.setheading(random.choice(direction))
    tim.forward(30)

screen=Screen()
screen.exitonclick()

