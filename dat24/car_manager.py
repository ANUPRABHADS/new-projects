from  turtle import  Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_car=[]
        self.car_speed=STARTING_MOVE_DISTANCE
        
        
    def cars(self):
        choice = random.randint(1,8)
        if choice == 1:
            new_car=Turtle("square")
            new_car.penup()
            new_car.shapesize(1,2)
            new_car.color(random.choice(COLORS))
            new_y=random.randint(-250,250)
            new_car.goto(300,new_y)
            self.all_car.append(new_car)

    def move_cars(self):
        for car in self.all_car:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed+=MOVE_INCREMENT






