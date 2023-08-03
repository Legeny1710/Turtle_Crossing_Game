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
carManager = CarManager()

screen.listen()
screen.onkey(key="Up", fun=Player1.move)
screen.onkey(key="Right", fun=Player1.go_right)
screen.onkey(key="Left", fun=Player1.go_left)



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carManager.create_cars()
    carManager.move_cars()







screen.exitonclick()