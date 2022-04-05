import random
import turtle
from turtle import Turtle
tom =Turtle()
tom.speed(1)
turtle.colormode(255)
def random_colour():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour=(r,g,b)
    return random_colour
for i in range(10):
    tom.color((random_colour()))
    tom.forward(10)
    tom.penup()
    tom.forward(10)
    tom.pendown()

