import turtle as t
import random

screen = t.Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title = "Make your bet" , prompt = "Which turtle will win the race? Enter the color : 'red' , 'yellow' , 'green' , 'blue' , 'indigo' , 'orange' ,'violet")
colors = ['red' , 'yellow' , 'green' , 'blue' , 'indigo' , 'orange' ,'violet']
y_pos = [-70,-40,-10,20,50,80,110]

is_race_on = False
all_turtles = []

for turtles in range (0,7):


    my_turtle = t.Turtle(shape='turtle')
    my_turtle.penup()
    my_turtle.color(colors[turtles])
    my_turtle.speed('fast')

    my_turtle.goto(x=-230, y=y_pos[turtles])
    all_turtles.append(my_turtle)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()> 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won the bet The winning turtle is {winning_color}")
            else:
                print(f"You've lost. The winning turtle is {winning_color}")
        random_distance = random.randint(3,12)
        turtle.forward(random_distance)


screen.exitonclick()