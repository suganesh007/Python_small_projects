from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 10, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(x=200, y=260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()  # to clear the 0 which is set as the actual value
        self.write(f"SCORE = {self.score}, HIGH SCORE = {self.high_score}", align=ALIGN, font=FONT)

    def inc_score(self):
        self.score += 1
        self.update_score()

    def reset_the_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file="data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGN, font=FONT)
