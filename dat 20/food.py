from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("dark blue")
        self.speed(0)
        self.refresh()

    def refresh(self) -> object:
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        self.goto(x, y)
