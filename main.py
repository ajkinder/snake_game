# Snake
# Snake - the Game = developed in Python
# Author: Alexander Kinder

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

WALL = 290
DISTANCE_TO_FOOD_FOR_SCORE = 15

screen = Screen()
screen.setup(width=600, height=600)  # Setup screen
screen.bgcolor("black")  # Set Screen Color
screen.tracer(0)  # Turn off tracer, rquires pdate
screen.title("Crazy Snake")  # Set Screen Title

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while (game_is_on):
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < DISTANCE_TO_FOOD_FOR_SCORE:
        print("Ate food")  # for debugging purposes
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > WALL or snake.head.xcor() < -WALL or snake.head.ycor() > WALL or snake.head.ycor() < -WALL:
        snake.reset()  # Reset the snake.
        scoreboard.reset()  # Reset game.

    # Detect Collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()  # Reset the snake.
            scoreboard.reset()  # Reset game

screen.exitonclick()