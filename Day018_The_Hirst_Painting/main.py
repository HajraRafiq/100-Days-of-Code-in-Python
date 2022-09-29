# import colorgram
import turtle as t
import random
# colors = colorgram.extract('hirst.jpg',30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g=color.rgb.g
#     b = color.rgb.b
#     new_color= (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

t.colormode(255)

color = [(33, 3, 238), (61, 3, 60), (250, 126, 2), (3, 251, 4), (243, 135, 31), (245, 3, 0), (251, 250, 29), (206, 5, 70), 
(26, 242, 29), (55, 7, 252), (254, 254, 0), (151, 56, 85), (102, 75, 227), (215, 6, 90), (215, 53, 83), (97, 245, 98), 
(191, 144, 178), (254, 7, 4), (160, 159, 254), (230, 53, 48), (228, 158, 217), (201, 40, 33), (254, 157, 152), (95, 48, 195), (158, 121, 245)]


bob = t.Turtle()
bob.penup()
bob.speed('fastest')
bob.hideturtle()
bob.setheading(225)
bob.forward(300)
bob.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    bob.dot(20, random.choice(color))
    bob.forward(50)

    if dot_count % 10 == 0:
        bob.setheading(90)
        bob.forward(50)
        bob.setheading(180)
        bob.forward(500)
        bob.setheading(0)


screen = t.Screen()
screen.exitonclick()