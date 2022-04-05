from turtle import Turtle
import random
tim=Turtle()
tim.speed(10)
tim.penup()
tim.right(90)
tim.forward(50)
tim.left(90)
tim.pendown()
colour=["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
for i in range(3,11):
    for no in range(i):
        tim.color(random.choice(colour))
        angle=360/i
        tim.forward(100)
        tim.left(angle)