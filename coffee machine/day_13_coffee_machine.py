data = {

    #esperssso
    "espresso": {
        "ingredients": {"milk": 10,
                        "coffee": 10
                        },
        "cost": 5.0
    },

    # latte
    "latte": {
        "ingredients": {"milk": 10,
                        "water": 10,
                        "coffee": 10
                        },

        "cost": 15.0
    },

    # cappuccino
    "cappuccino": {
        "ingredients": {"milk": 10,
                        "water": 10,
                        "coffee": 10
                        },

        "cost": 20.0
    }

}

report = {
    "water": 30,
    "milk": 30,
    "coffee": 30
}
profit = 0


# checking the sufficient sources for the coffee_input
def sufficient_resources():
    global materials
    ingredients = materials["ingredients"]
    for key in ingredients:
        if ingredients[key] > report[key]:
            print(f"Sorry , There is not enough {key}")
            return False
    return True


# changing the report by reducing the used ingredients
def report_0():
    global materials
    ingredients = materials["ingredients"]
    for key in ingredients:
        report[key] = report[key] - ingredients[key]


# full process of the user_coin inputs
def coin_process():
    list_values = [1, 2, 5, 10]
    total_value = 0
    global materials
    for i in range(0, len(list_values)):
        coin = list_values[i]

        if total_value < materials["cost"]:
            coin_input = int(input(f"enter the {coin} coin  = "))
            total_value += coin_input * coin
    if total_value < materials["cost"]:
        print("sorry that's not enough money")
        return False
    else:
        global profit
        balance = total_value - materials["cost"]
        print(f"your balance is rs,{round(balance, 2)}")
        profit += materials["cost"]


# start of the program
is_true = True
while is_true:
    coffee_input = input("what would you like(espresso / latte / cappuccino) : ")
    if coffee_input == "off":
        is_true = False
        break
    elif coffee_input == "report":
        print(report)
        continue      # continue returns to the top of the while loop and continue from th top
    elif coffee_input == "profit":
        print(profit)
        continue
    materials = data[coffee_input]
    if sufficient_resources():
        if coin_process():
            report_0()    # it replaces the balance values to the report
            print(f"your order {coffee_input}, is ready")
