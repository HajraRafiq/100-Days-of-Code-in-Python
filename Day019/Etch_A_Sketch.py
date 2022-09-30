import turtle as t

terry = t.Turtle()
screen = t.Screen()

def move_forward():
    terry.forward(10)

def move_back():
    terry.backward(10)

def turn_left():
    terry.left(10)

def turn_right():
    terry.right(10)

def clear():
    terry.clear()
    terry.penup()
    terry.home()
    terry.pendown()

screen.listen()
screen.onkey(move_forward , "w")
screen.onkey(move_back, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
clear()
screen.exitonclick()