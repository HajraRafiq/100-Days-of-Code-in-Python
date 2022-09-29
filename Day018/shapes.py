from turtle import Turtle , Screen
import random

terry = Turtle()
terry.width(3)
screen = Screen()
screen.bgcolor('black')

colors = ["red","brown","turquoise","purple3","green","blue" , "orange" , "purple" ,"pink" , "magenta"]

def draw_shape(num_of_sides):

    for i in range(num_of_sides):
        angle = 360/num_of_sides
        terry.forward(100)
        terry.right(angle)

for shape_side_n in range(3,11):
    terry.color(random.choice(colors))
    draw_shape(shape_side_n)



screen.exitonclick()