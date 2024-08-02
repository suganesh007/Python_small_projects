import turtle
from turtle import Screen
screen = Screen()

screen.listen()


def move_forward():
    turtle.forward(40)


def backwards():
    turtle.backward(40)


def clock_wise():
    turtle.right(90)


def counter_clock_wise():
    turtle.left(90)


def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.onkey(key="d", fun=clock_wise)
screen.onkey(key="a", fun = counter_clock_wise)
screen.onkey(key="w", fun = move_forward)
screen.onkey(key="s", fun = backwards)
screen.onkey(key="c", fun = clear)

screen.exitonclick()
