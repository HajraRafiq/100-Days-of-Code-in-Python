# Working on Turtle 

import turtle

new_turtle = turtle.Turtle() # created object from module turtle and Class Turtle inside the turtle module
new_turtle.shape('turtle')
new_turtle.color('blue')
new_turtle.forward(100)

print(new_turtle)

# Accessing Attributes

screen = turtle.Screen() # here Screen in the attribute inside object 

print(screen.canvheight) # canvas height is also an attribute
screen.exitonclick()