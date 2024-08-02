print("The Love Calculator is calculating your score...")
name1 = input("enter your name")  # What is your name?
name2 = input("enter your loved once name")  # What is your loved once name?

# lowering the values
combined_names = name1.lower() + name2.lower()

# counting 1
t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")
cal_1 = str(t + r + u + e)

# counting 2
l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")
cal_2 = str(l + o + v + e)

# final adding of true and love
final = cal_1 + cal_2

# final value
print(f"Your score is {final}")
