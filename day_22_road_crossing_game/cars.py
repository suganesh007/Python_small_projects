from turtle import Turtle
import random

COLORS = ["blue", "red", "green", "orange", "pink", "yellow", "purple"]


class CarManager:
    def __init__(self):
        self.cars_list = []
        self.move = 5

    def create_new_car(self):
        random_value = random.randint(1, 6)  # to reduce the number of cars   when the value is equal to 1 then only
        # the car will be created
        if random_value == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=3)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-200, 200)
            new_car.goto(x=300, y=random_y)
            self.cars_list.append(new_car)

    def move_cars(self):
        for car in self.cars_list:
            car.backward(self.move)

    def increase_speed(self):
        self.move += 10
