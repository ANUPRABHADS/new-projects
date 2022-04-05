from  turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.high_score=0
        self.hideturtle()
        self.penup()
        self.goto(0,220)
        self.update()

    def score_add(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
        self.score=0
        self.update()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align='center', font=('Arial', 22, 'normal'))

    def update(self):
        self.clear()
        self.write(f"Score = {self.score} High Score: {self.high_score}", align='center', font=('Arial', 22, 'normal'))














