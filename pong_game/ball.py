from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.shapesize(1)
        self.penup()
        self.color("white")
        self.xmove=10
        self.ymove=10


    def move(self):
        x=self.xcor()+self.xmove
        y=self.ycor()+self.ymove
        self.goto(x,y)
    def bounce(self):
        self.ymove*=-1
    def bounce_x(self):
        self.xmove*=-1
    def reset(self) -> None:
        self.goto(0,0)
        self.bounce_x()








