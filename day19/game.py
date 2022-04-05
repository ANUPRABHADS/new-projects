from turtle import  Turtle,Screen
import random

screen=Screen()
screen.setup (width=500, height=400)
user_bet=screen.textinput("Make the bet", "Which turtle win the race? Enter a colour :")
print(user_bet)
color=["red","orange","yellow","green","blue","violet"]
position=[-150,-100,-50,0,50,100]
move=[50,40,30,20,10]
all_turtle=[]
for index in range(6):
    tim = Turtle(shape="turtle")
    tim.color(color[index])
    tim.penup()
    tim.goto(x=-230, y=position[index])
    all_turtle.append(tim)
if user_bet:
    on_race=True

while on_race:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            on_race=False
            win_color=turtle.pencolor()
            if win_color==user_bet:
                print(f"You have win! the {win_color} turtle is the winner")
            else:
                print(f"You have lose! the {win_color} turtle is the winner")
        turtle.forward(random.choice(move))







screen.exitonclick()