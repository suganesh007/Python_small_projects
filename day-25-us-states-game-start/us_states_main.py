import turtle

import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"

# adding the image to the screen
# we first add/upload the shape to the screen then only we can use it as a turtle
screen.addshape(image)  # adding the image size in the screen
turtle.shape(image)  # creating the shape to image as square, circle.

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
print(states)
score = 0
total = 50
correct_guess = []

while len(correct_guess) <= 50:

    answer = screen.textinput(title=f"{score}/{total}state correct", prompt="what another state name ?").title()

    # picking the unknown states from the user and get the lists into the csv in csv format
    if answer == "Exit":
        # list comprehensive
        unknown_states = [state for state in states if state not in correct_guess]
        # for state in states:
        #     if state not in correct_guess:
        #         unknown_states.append(state)

        data_dict = {
            "states": unknown_states
        }
        data_frame = pandas.DataFrame(data_dict)
        data_frame.to_csv("unknown states.csv")
        break

    if answer in states:
        # it works only if the states are in list if the states are in series then it odes not work
        # then we have to use for range function and use the if condition to check the state is correct with the answer

        x_and_y = data[data["state"] == answer]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # here the code gets future error, so we want to add ilco[0] to avoid this error
        t.goto(x=int(x_and_y.x.iloc[0]), y=int(x_and_y.y.iloc[0]))

        # t.write(f"{answer}")          # this is the correct but also the pandas tag [x_and_y.state.item()] gives the
        # first item in the row
        t.write(x_and_y.state.item())
        if answer not in correct_guess:
            score += 1
            correct_guess.append(answer)

# turtle.onscreenclick(fun=calling(data, states, answer), btn=1)
# used to stay open the page after the code is finished
