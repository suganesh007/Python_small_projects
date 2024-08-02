from turtle import Turtle
import random


# inheritance
# turtle inherit to the food now the food can all the work of the turtle that can do

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)   # it used to reduce the actual size of the circle
        self.color("blue")
        self.refresh()

    # it replaces the co-ordinations of the food
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
