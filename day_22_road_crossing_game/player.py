from turtle import Turtle

POSITION = (0, -280)


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.setheading(90)
        self.goto(POSITION)

    def up(self):
        self.forward(10)

    def down(self):
        self.back(10)

    def is_at_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False

    def go_to_starting_line(self):
        self.goto(POSITION)
