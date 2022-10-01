from turtle import Turtle , Screen
import time
from main_classes import Snake 
from food import Food
from scoreboard import Scoreboard

#Setting up Screen

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

#Holding snake with keys

snake = Snake()
food = Food()
scoreboard = Scoreboard()

#Controlling  the snake with keys

screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down ,"Down")
screen.onkey(snake.left , "Left")
screen.onkey(snake.right , "Right")

# Moving the snake 

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# Collision detection with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

#COllision with Wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on = False
        scoreboard.game_over()

# Collision with Tail
    for segment in snake.segments[1:]:  #Slicing
        if snake.head.distance(segment)<10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()
