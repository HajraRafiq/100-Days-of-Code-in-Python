from turtle import Turtle , Screen

my_turtle = Turtle()
my_turtle.shape('arrow')

my_turtle.color('purple3')

for i in range(4):
    my_turtle.forward(200)
    my_turtle.left(90)



screen = Screen()
screen.bgcolor('black')
screen.exitonclick()