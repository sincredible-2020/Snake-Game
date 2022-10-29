import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.bgcolor('black')
wn.title("Snake Game")
wn.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


wn.listen()
wn.onkey(key="Up", fun=snake.upwards)
wn.onkey(key="Down", fun=snake.downwards)
wn.onkey(key="Right", fun=snake.right)
wn.onkey(key="Left", fun=snake.left)

is_game_on = True
while is_game_on:
    wn.update()
    time.sleep(0.1)

    snake.movement()

    if snake.head.distance(food) < 15:
        food.random_position()
        scoreboard.update_score()
        snake.extend()

    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:-1]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

wn.exitonclick()
