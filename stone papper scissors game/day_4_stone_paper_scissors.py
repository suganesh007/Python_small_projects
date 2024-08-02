# 0 for rock 1 for paper 2 for scissors
rock = '''

rock
    ______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper = '''

paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''

scissors
  _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list = [rock,paper,scissors]
user_choice = int(input("enter the value (0,1,2)= "))
if user_choice>=0 and user_choice<=2:
    print("your choice is = ",list[user_choice])


    import random
    computer_choice = random.randint(0,2)
    print("computer choice is = ",list[computer_choice])

    if user_choice==0 and computer_choice==2:
        print("you win")
    elif computer_choice==0 and user_choice==2:
        print("you lose")

    elif computer_choice > user_choice:
        print("you lose")
    elif user_choice > computer_choice:
        print("you win")
    elif user_choice==computer_choice:     
        print("its draw")
else:
    print("type error-write only the numbers between 0 ,1 ,2 ")