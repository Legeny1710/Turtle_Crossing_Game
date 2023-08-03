from turtle import Screen
import  time
from player import Player
from score_board import ScoreBoard
from car_manager import CarManager






screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

Player1 = Player()

screen.listen()
screen.onkey(key="space", fun=Player1.move)



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()







screen.exitonclick()