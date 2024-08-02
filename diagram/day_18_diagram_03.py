# import colorgram
#
# colors = colorgram.extract("20_001.jpg", 15)  # 15 denotes the 15 types of colors that are imported from the picture
# list_0 = []
import turtle
import random
from turtle import Screen
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#
#     rgb = r, g, b
#     list_0.append(rgb)
# print(list_0)


turtle.colormode(255)
list_rgb = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57),
            (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174),
            (64, 153, 138), (39, 36, 36), (76, 40, 48)]

turtle.penup()
turtle.speed(0.001)
turtle.hideturtle()
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
no_of_dots = 100
for i in range(1, no_of_dots+1):
    # turtle.pendown()
    turtle.dot(30, random.choice(list_rgb))
    # turtle.penup()
    turtle.forward(50)

    if i % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)


screen = Screen()
screen.exitonclick()
