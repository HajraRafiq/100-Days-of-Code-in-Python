print("Welcome to the rollercoaster! ")
height = int(input("What is your height in cm ?\n"))
bill = 0
if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?\n"))
    if age <= 12:
        bill = 5
        print("Child tickets are $5")
        
    elif age <=18 :
        bill = 7 
        print("Youth tickets are 7$")
    else:
        bill = 12
        print("Adult tickets are $12")
    want_photos = input("Do you want photos ?  If yes enter Y , if no then enter N\n")
    if want_photos == "Y":
        bill = bill + 3
    print(f"Your final bill is {bill}")

else:
    print("Sorry you're too short")