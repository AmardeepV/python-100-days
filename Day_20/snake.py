from turtle import *

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    '''
    Docstring for Snake
    '''

    def __init__(self):
        self.new_segments = []
        self.generate_turtle()
        self.head = self.new_segments[0]

    def generate_turtle(self):
        '''
        Docstring for generate_turtle

        :param self: Description
        '''
        for pos in START_POS:
            self.add_segments(pos)

    def add_segments(self, position):
        snake_seg = Turtle("square")
        snake_seg.color("white")
        snake_seg.penup()
        snake_seg.goto(position)
        self.new_segments.append(snake_seg)

    def extend_snake(self):
        self.add_segments(self.new_segments[-1].position())

    def move_turtle(self):
        '''
        Docstring for move_turtle

        :param self: Description
        '''
        for seg in range(len(self.new_segments)-1, 0, -1):
            seg_x = self.new_segments[seg-1].xcor()
            seg_y = self.new_segments[seg-1].ycor()
            self.new_segments[seg].goto(seg_x, seg_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
