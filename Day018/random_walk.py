from turtle import Turtle , Screen
import random

terry = Turtle()
terry.width(10)
screen = Screen()
terry.speed("fastest")


colors = ["red","brown","turquoise","purple3","green","blue" , "orange" , "purple" ,"pink" , "magenta"]
directions = [0,90,180,270]

for i in range(300):
    terry.color(random.choice(colors))
    terry.forward(30)
    terry.setheading(random.choice(directions))