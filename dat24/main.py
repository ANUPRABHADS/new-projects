import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager=CarManager()

player=Player()

scoreboard=Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.cars()
    car_manager.move_cars()
    screen.listen()
    screen.onkey(player.up,"Up")

    for car in car_manager.all_car:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()


    if player.finish():
        player.go_start()
        car_manager.level_up()
        scoreboard.score_add()





screen.exitonclick()
