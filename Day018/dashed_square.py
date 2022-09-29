from turtle import Turtle , Screen

my_turtle = Turtle()
my_turtle.shape('arrow')
my_turtle.width(5)
my_turtle.color('purple3')

def dashed_line():
    for i in range(5):
        my_turtle.forward(15)
        my_turtle.penup()
        my_turtle.forward(15)
        my_turtle.pendown()
    my_turtle.left(90)

def square():
    for i in range(4):
        dashed_line()


screen = Screen()
screen.bgcolor('black')

square()
screen.exitonclick()
