import turtle
import random


class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('yellow')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed(0)
        self.spawn()

    def spawn(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x=x, y=y)
