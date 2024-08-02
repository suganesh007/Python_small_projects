def starting_from():
    import art
    print(art.logo)
    #import random for chose the number from 1 to 100
    import random as r

    #printing the introduction
    print("Welcome to the number guessing Game ! ")
    print("i'm thinking the number between 1 to 100")

    #random value generation
    random_value = r.randint(1, 100)
    print(f"Psst , the correct answer is = ,{random_value} ")

    #asking the user for difficulty level from easy to hard easy=10chances and hard=5chances
    difficulty = input("Enter The difficulty 'Easy' or 'Hard' = ")

    #attempts increases based on the loop selection
    attempts = 0
    if difficulty == "easy":
        attempts += 10
    elif difficulty == "hard":
        attempts += 5
    else:
        print("type error")

    # loop discontinues when attempt gets 0
    # guessing the number will occur for a one while full rotation
    while attempts > 0:

        #input for user guessing number
        user_guess = int(input("Make a Guess = "))
        if user_guess == random_value:
            print(
                f"You got it! The answer was {random_value}")  # return key used bcoz it exit the loop after the return occurs
            break

        elif user_guess > random_value:
            print("Too High")
            attempts -= 1
            print(f"You Have , {attempts} attempts remaining to guess the number .")
            print("Guess again")

        elif user_guess < random_value:
            print("Too Low")
            attempts -= 1
            print(f"You Have , {attempts} attempts remaining to guess the number .")
            print("Guess again")

    # this occurs then when the attempts get 0 then the whike loop will break then the print will occurs
    if attempts == 0:
        print("you lose")

    # to continue the games 'yes' or 'no'
    guess_again = input("enter 'Y' to continue or 'N'stop = ").lower()
    if guess_again == "y":
        starting_from()
    else:
        print("Thanks For Your Game Play!!!")


starting_from()
