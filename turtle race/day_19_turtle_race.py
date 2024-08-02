from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=500)
user_input = screen.textinput(title="guess the winner", prompt="guess which color is won? = ")
colors = ["red", "green", "blue", "violet", "black", "orange", "purple"]
all_turtles = []

line = Turtle()
line.penup()
line.shape("square")
line.shapesize(stretch_len=0.1, stretch_wid=40)
line.forward(230)
line.pendown()
# race starting positioning in the y_direction
y = [-70, -40, -10, 20, 50, 80]
for i in range(0, 6):
    timmy = Turtle()
    timmy.penup()
    timmy.color(random.choice(colors))
    timmy.shape("turtle")
    timmy.goto(x=-230, y=y[i])  # positioning the turtles
    all_turtles.append(timmy)

is_on = True
# forwarding the turtle
while is_on:
    for turtle in all_turtles:

        turtle.forward(random.randint(15, 17))

        if turtle.xcor() > 210:
            is_on = False
            win_color = turtle.pencolor()
            if win_color == user_input:
                print("you won")
                break
            else:
                print("you lose")
                is_on = False
                break



screen.exitonclick()
