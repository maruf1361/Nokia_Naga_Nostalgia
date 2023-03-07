from turtle import Turtle

COORDS = [(0, 0), (-20, 0), (-40, 0)]
DIR = 20

class Snake:
    def __init__(self):
        self.turtle_list = []
        for index in range(3):
            self.new_turtle = Turtle("square")
            self.new_turtle.color("White")
            self.new_turtle.penup()
            self.new_turtle.goto(COORDS[index])
            self.turtle_list.append(self.new_turtle)

    def move(self):
        for i in range(len(self.turtle_list) - 1, 0, -1):
            x = self.turtle_list[i - 1].xcor()
            y = self.turtle_list[i - 1].ycor()
            self.turtle_list[i].goto(x, y)
        self.turtle_list[0].forward(DIR)

    def up(self):
        if self.turtle_list[0].heading() != 270:
            self.turtle_list[0].setheading(90)
    def down(self):
        if self.turtle_list[0].heading() != 90:
            self.turtle_list[0].setheading(270)
    def right(self):
        if self.turtle_list[0].heading() != 180:
            self.turtle_list[0].setheading(0)
    def left(self):
        if self.turtle_list[0].heading() != 0:
            self.turtle_list[0].setheading(180)