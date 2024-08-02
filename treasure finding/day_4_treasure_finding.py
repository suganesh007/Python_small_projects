line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map_content = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("enter the position(first letter(a,b,c) next number(1,2,3)) = ")
position_1 = position[0].lower()

abc = ["a","b","c"]
finding_value = abc.index(position_1)
position_letter = int(position[1])-1
map_content[position_letter][finding_value] = "x"
print(f"{line1}\n{line2}\n{line3}")
