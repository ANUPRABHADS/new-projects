from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.leval = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.write(f"Score = {self.leval}", align='center',font=FONT)

    def score_add(self):
        self.clear()
        self.leval += 1
        self.write(f"Score = {self.leval}", align='center', font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align='center', font=FONT)


