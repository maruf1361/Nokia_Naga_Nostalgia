from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height= 600)
screen.bgcolor("black")

turtle_list = []
screen.tracer(0)
snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.5)

screen.exitonclick()
