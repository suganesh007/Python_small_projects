data = [
     {

          "name":"instagram",
          "follower_count":350,
          "description":"soical media platform",
          "country":"US"
     },

          {
          "name":"cristiano_ronaldo",
          "follower_count":215,
          "description":"fottballer",
          "country":"protugal"
          },

          {
               "name":"arina grade",
               "follower_count":183,
               "description":"musician and dancer",
               "country":"US"
          },
          {
               "name":"dwanyne johnson",
               "follower_count":181,
               "description":"actor",
               "country":"US"
          },
          {
               "name":"suganesh",
               "follower_count":1234,
               "description":"crickerter",
               "country":"india"
          }
]



#random generation for random value selection
def random_generation(value):
     name=value["name"]
     description=value["description"]
     country=value["country"]
     return f"{name} , is {description} , in {country}"
     


def comparing():
     if account_a["follower_count"] < account_b["follower_count"]:
          return "h"
     else:
          return "l"


is_true=True
def again():
     global is_true
     again_play=input("'y' to play again 'n' to exit = ")
     if again_play=='y':
          is_true=True
     else:
          print("thank you !!")
          is_true=False

def comparing_inputs():
     input_A=input("guess the followers for 'B' (higher for 'h' or lower for 'l') = ").lower()
     if input_A==comparing():
          global score
          score+=1
          global account_a
          account_a=account_b
          print("your current score  = ", score)
          print( "you are right !")
     else:
          print("final score = ",score)
          print ("end !")
          again()


import random
score=0
account_a = random.choice(data)
while is_true:
   
     account_b = random.choice(data)
     while account_a==account_b:
          account_b=random.choice(data)

     random_value_for_a = random_generation(account_a)
     random_value_for_b = random_generation(account_b)
     print("A = " ,random_value_for_a)
     print("B = " ,random_value_for_b)
     comparing_inputs()

