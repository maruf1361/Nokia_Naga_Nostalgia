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
