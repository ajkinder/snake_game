# Snake
# Snake - the Game = developed in Python
# Author: Alexander Kinder

from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)  # Setup screen
screen.bgcolor("black")  # Set Screen Color
screen.tracer(0)  # Turn off tracer, rquires pdate
screen.title("Crazy Snake")  # Set Screen Title

snake = Snake()

game_is_on = True
while (game_is_on):
    screen.update()
    time.sleep(0.1)

    snake.move()



