import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

# TODO.1: Create turtle controls
screen.listen()
screen.onkeypress(fun=turtle.move, key='Up')
screen.onkeypress(fun=turtle.move, key='space')
screen.onkeypress(fun=turtle.move, key='w')

car_manager.spawn_car()

is_game_over = False
while not is_game_over:
    time.sleep(0.1)
    screen.update()

    # TODO.2: detect  car collisions
    for car in car_manager.cars:
        if turtle.distance(car) < 20:
            is_game_over = True

    if turtle.is_at_finish_line():
        scoreboard.increase_score()
        turtle.reposition()
    else:
        car_manager.spawn_car()
        car_manager.move_cars(level=scoreboard.score)

    # TODO.3: detect if a player has reached the finish line
scoreboard.game_over()

screen.exitonclick()
