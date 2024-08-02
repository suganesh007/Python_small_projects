from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.score()

    def score(self):
        self.penup()
        self.hideturtle()
        self.goto(-260, 270)
        self.clear()
        self.write(f"LEVEL = {self.level}", align="center", font=("Arial", 10, "normal"))

    def increase_level(self):
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 10, "normal"))
