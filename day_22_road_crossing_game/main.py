import time
from turtle import Screen
from player import Player
from cars import CarManager
from scoreboard import ScoreBoard

# screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# assigning the names
car_manager = CarManager()
player = Player()
score_board = ScoreBoard()

# screen listening
screen.listen()
screen.onkeypress(fun=player.up, key="Up")
screen.onkeypress(fun=player.down, key="Down")

# true
is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    score_board.score()
    car_manager.create_new_car()
    car_manager.move_cars()

    # detect the collision for the car
    for car in car_manager.cars_list:
        if player.distance(car) < 30:
            score_board.game_over()
            is_on = False

    # if player finish the current level then increasing the car speed and increasing the level then reset the player
    # to the starting position
    if player.is_at_finish_line():
        score_board.increase_level()
        car_manager.increase_speed()
        player.go_to_starting_line()

screen.exitonclick()
