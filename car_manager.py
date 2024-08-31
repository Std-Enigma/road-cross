import random
from turtle import Turtle

from player import MOVE_DISTANCE

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []

    def spawn_car(self):
        chance_of_spawn = random.randint(1, 6)
        if chance_of_spawn == 6:
            car = Turtle()
            car.penup()
            car.color(random.choice(COLORS))
            car.shape('square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(x=300, y=random.randint(-250, 250))
            self.cars.append(car)

    def reset_location(self, car: Turtle):
        car.goto(x=300, y=random.randint(-325, 325))

    def move_cars(self, level):
        for car in self.cars:
            car.backward(level * MOVE_DISTANCE)
