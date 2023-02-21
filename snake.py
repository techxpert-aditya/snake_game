import turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20


class Snake:

    # create a snake body
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.moving_speed = 0.1

    def create_snake(self):

        for position in STARTING_POSITIONS:
            self.add_segments(position)

    def add_segments(self, position):
        tbody = turtle.Turtle(shape='circle')
        tbody.penup()
        tbody.color('white')
        tbody.goto(position)
        self.segments.append(tbody)

    def extends(self):
        self.add_segments(self.segments[-1].position())

    # move the snake

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[index - 1].xcor()
            new_y = self.segments[index - 1].ycor()
            self.segments[index].goto(x=new_x, y=new_y)
        self.segments[0].forward(MOVING_DISTANCE)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.moving_speed = 0.1

    # functions that can turn the snake direction

    def turn_up(self):
        if self.head.heading() == 270:
            return
        self.head.setheading(90)

    def turn_down(self):
        if self.head.heading() == 90:
            return
        self.head.setheading(270)

    def turn_left(self):
        if self.head.heading() == 0:
            return
        self.head.setheading(180)

    def turn_right(self):
        if self.head.heading() == 180:
            return
        self.head.setheading(0)
