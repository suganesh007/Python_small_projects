inp_1 = int(input("how many letters do : "))
inp_2 = int(input("how many symbols do : "))
inp_3 = int(input("how many numbers do : "))

#letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']


#numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


#symbols
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
           '*', '(', ')', '<']


import random


#assigning to return the final password
random_password = []


#generating random letters ans append it to the random_password
for i in range(1,inp_1+1):
    random_password.append(random.choice(letters))

#generating random symbol and assign it to the random_password
for i in range(1,inp_2+1):
    random_password.append(random.choice(symbols))

#generating random numbers and assign it to the random_password
for i in range(1,inp_3+1):
    random_password.append(random.choice(numbers))
    

#shuffling the finally generated password which is saved in the **list**
random.shuffle(random_password)


#changing from list to string letters and printing it
final_password = ""
for i in random_password:
    final_password = final_password + i
print(f"your password is = {final_password}")