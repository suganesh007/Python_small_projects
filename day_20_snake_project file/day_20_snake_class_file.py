from turtle import Turtle, Screen

# X_cor positions
STARTING_POSITIONS = [(-40, 0), (-20, 0), (0, 0)]  # because the box size is 20
MOVE_FORWARD = 20

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


# creating the snake body
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())  # the position() gives the x and y co-ordinations

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # output = 2, 1
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_FORWARD)  # forward is 20 because the width of the square is 20

    # up, down, left, right

    def up(self):
        # the heading is used to find the current position of the heading in 360deg as numbers
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
