import turtle as t

terry = t.Turtle()
screen = t.Screen()

def move_forward():
    terry.forward(10)




screen.listen()
screen.onkey(key="space" , fun =move_forward)
screen.exitonclick()