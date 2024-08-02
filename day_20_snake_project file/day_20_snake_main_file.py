import time
from turtle import Screen
from day_20_snake_class_file import Snake
from day_20_snake_food import Food
from day_20_snake_score_file import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

# creating the square(snake)

# controlling the directions
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_on = True
while is_on:

    snake.move()
    # we're updating the screen after all the parts move to the next step
    screen.update()
    time.sleep(0.1)
    # moving the snake

    # increment of the score when the snake eat the food
    if snake.head.distance(food) < 15:  # it denotes that the snake ate the food
        food.refresh()  # used to replaces the position of the food
        snake.extend()
        score.inc_score()

    # it occurs when the snake goes to the nearest to the wall and hit the wall

    # *** Here the -290 is greater than the -300 because it was negative digit ***

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset_the_game()
        snake.reset()

    for segment in snake.segments[3:]:
        if segment.distance(snake.head) < 10:
            score.reset_the_game()
            snake.reset()

"""In your original code, you were checking for collisions between the snake's head and its body segments starting 
from the second segment onward (snake.segments[1:]). This can cause an issue because:

Initial Proximity:
            At the start of the game, the snake's body segments are very close to each other.

Immediate Collision Detection: As soon as the game starts, the snake moves, and the head's distance from its body 
segments can be very small,potentially triggering a false positive collision detection.

" Why Checking from the Fourth Segment Works " : By checking for collisions starting from the fourth segment (
snake.segments[3:]), you effectively skip the first few segments. Here’s why this helps:

Initial Movement Phase: During the initial phase of the game, the snake is still small, and the first few segments 
are too close to detect a real collision. By skipping these segments, you avoid false positives.

Sufficient Growth Time: The snake needs some time to grow and move away from its initial tightly-packed 
configuration. Starting from the fourth segment gives it that time."""
screen.exitonclick()
