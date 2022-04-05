from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score=0
        self.r_score=0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update()
    def update(self):
        self.clear()
        self.goto(-100, 250)
        self.write( self.l_score ,align='left', font=('Arial', 22, 'normal'))
        self.goto(100, 250)
        self.write(self.r_score,align='right', font=('Arial', 22, 'normal'))

    def l_point(self):
        self.l_score += 1
        self.update()


    def r_point(self):
        self.r_score += 1
        self.update()


