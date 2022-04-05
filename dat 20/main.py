from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.title("Snake Game")
screen.setup(width=500, height=500)
screen.tracer(0)
snake = Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score_add()

    if snake.head.xcor() < -240 or snake.head.xcor() > 240 or snake.head.ycor() < -240 or snake.head.ycor() > 240:
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:

        if snake.head.distance(segment)<10:
            score.reset()
            snake.reset()



screen.exitonclick()
