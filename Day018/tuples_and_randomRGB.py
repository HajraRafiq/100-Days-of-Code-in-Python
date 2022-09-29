# colors are represented in Tuple
# tuples are same like lists but immutable i.e. it is unchangeable
import turtle as t
import random

terry = t.Turtle()
t.colormode(255)
terry.width(10)
screen = t.Screen()
terry.speed("fastest")


# colors = ["red","brown","turquoise","purple3","green","blue" , "orange" , "purple" ,"pink" , "magenta"]
directions = [0,90,180,270]

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color
    

for i in range(300):
    terry.color(random_color())
    terry.forward(30)
    terry.setheading(random.choice(directions))