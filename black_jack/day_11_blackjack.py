import random


def black_jack():
    # importing random for to select the cards

    # cards variable containing all the different values for all cards
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # assigning variable
    count = 2
    user_choice = []
    computer_choice = []

    # for loop to get random card values to the assigned variables
    for i in range(count):
        # random cards for user_choice
        random_choice = random.choice(cards)
        user_choice.append(random_choice)

        # random cards for computer_choice
        com_random_choice = random.choice(cards)
        computer_choice.append(com_random_choice)

    # end of the for loop

    # printing the total amounts for user
    print("your_total = ", sum(user_choice))

    # printing the 1st card and the second card was hidden to hide it from the user
    print("computer_total = ", computer_choice[0], "hidden")

    # adding user and computer total
    user_total = sum(user_choice)
    computer_total = sum(computer_choice)


    # while continues for comparing the card values to finalize the answer
    is_true = True
    while is_true:



        # computer == user
        if computer_total == 21:
            print("computer_total = ", computer_total)
            print("your_total = ", user_total)
            print("computer wins")
            break

        # user == 21
        elif user_total == 21:
            print("computer_total = ", computer_total)
            print("your_total = ", user_total)
            print("you win")
            break

        # computer == user
        elif computer_total == 21 and user_total == 21:
            print("computer_total = ", computer_total)
            print("your_total = ", user_total)
            print("draw")
            break

        # for user line (63 - 80)
        # 1.) user>21 , then check 11 in the choice , then change [11 = 1] to decrease the value below 21
        if user_total > 21:
            if 11 in user_choice:
                ind = user_choice.index(11)
                user_choice[ind] = 1
                print("user_choice = ", user_choice)
                continue  # the continue statement used to *** break the continuation *** and goes to the starting of
                # the while loop

            #  user has above 21 without having 11 in the cards then user lose
            else:
                print("computer_total = ", computer_total)
                print("your_total = ", user_total)
                print(" you lose")
                break

        # looped if condition ends

        # for computer line(81-96)
        # 2.) computer >21 , then check 11 in the choice , then change [11 = 1] to decrease the value below 21
        if computer_total > 21:
            if 11 in computer_choice:
                ind = computer_choice.index(11)
                computer_choice[ind] = 1
                continue
                # the continue statement used to *** break the continuation *** and goes to the starting of the while
                # loop

            #  computer has above 21 without having 11 in the cards then user lose
            else:
                print("computer_total = ", computer_total)
                print("your_total = ", user_total)
                print("you win")
                break

        # looped if ends

        # computer <17 , add cars to attain more than 17 and goes to the loop from the starting for checking the limits
        if computer_total < 17:
            computer_another_choice = random.choice(cards)
            computer_choice.append(computer_another_choice)
            continue

        # computer exceeds more than 21 than user won
        elif computer_total > 21:
            print("computer_total = ", computer_total)
            print("your_total = ", user_total)
            print("you win")
            break

        # user wish to increase the cards total
        user_choice_wish = input("type 'y' to add card , or type 'n' to continue = ")

        # if user = yes , then card value will add and goes to the starting fo the while loop
        if user_choice_wish == "y":
            user_another_choice = random.choice(cards)
            user_choice.append(user_another_choice)
            continue

        # checking the final_values by comparing --> for the ( winner )

        # computer == user then it's ( draw )
        if computer_total == user_total:
            print("computer_total = ", computer_total)
            print("your_total = ", user_total)
            print("draw")
            break

        # computer < user , then( user win )
        elif computer_total < user_total:
            print("computer_total = ", computer_total)
            print("your_total = ", user_total)
            print("you win")
            break

        # else , ( user lose )
        else:
            print("computer_total = ", computer_total)
            print("your_total = ", user_total)
            print("you lose")
            break

    # calling function for a looping game without ends
    black_jack()


black_jack()
