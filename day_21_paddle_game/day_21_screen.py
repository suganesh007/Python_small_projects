from turtle import Turtle


POSITIONS_X = []
POSITIONS_Y = []


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()  # it's calling the turtle init by using the super class
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        self.goto(x=self.xcor(), y=self.ycor() + 30)

    def down(self):
        self.goto(x=self.xcor(), y=self.ycor() - 30)

    def up_arrow(self):
        self.goto(x=self.xcor(), y=self.ycor() + 30)

    def down_arrow(self):
        self.goto(x=self.xcor(), y=self.ycor() - 30)
