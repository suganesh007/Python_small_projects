from turtle import Screen
from day_21_screen import Paddle
from day_21_ball import Ball
from score import Score
import time

screen = Screen()
score = Score()

screen.setup(width=800, height=500)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()

screen.listen()
screen.onkeypress(fun=l_paddle.up, key="w")
screen.onkeypress(fun=l_paddle.down, key="z")

screen.onkeypress(fun=r_paddle.up_arrow, key="Up")
screen.onkeypress(fun=r_paddle.down_arrow, key="Down")

is_true = True
while is_true:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 225 or ball.ycor() < -225:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 70 and ball.xcor() > -340:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.restart()
        score.l_scores()
        ball.bounce_x()

    elif ball.xcor() < -410:
        ball.restart()
        score.r_scores()
        ball.bounce_x()
screen.exitonclick()
