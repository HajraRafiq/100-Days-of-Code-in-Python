import turtle as t
import random

terry = t.Turtle()
t.colormode(255)
terry.shape('arrow')
screen = t.Screen()
screen.bgcolor('black')

terry.speed("fastest")
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color

def draw_spirograph(size_of_gap):

    for i in range(int(360/size_of_gap)):
        terry.color(random_color())
        terry.circle(100)
        terry.setheading(terry.heading()+size_of_gap)

draw_spirograph(5)


screen.exitonclick()