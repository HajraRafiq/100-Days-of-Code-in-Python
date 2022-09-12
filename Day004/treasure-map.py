# 🚨 Don't change the code below 👇
row1 = ["️⬜️","️️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

horizontal= int(position[0]) #row
vertical = int(position[1]) #column

selected_row=map[vertical - 1]
selected_row[horizontal-1]="X"*5



print(f"{row1}\n{row2}\n{row3}")
