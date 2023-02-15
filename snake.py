from turtle import Turtle

STARTING_POSITION = ((0, 0), (-20, 0), (-40, 0))
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segment_list = []
        self.creating_snake()

    def creating_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segment_list.append(segment)

    def put_snake_away(self):
        for segment in self.segment_list:
            segment.goto(1000, 1000)
        self.segment_list.clear()
        self.creating_snake()

    def add_food_segment(self):
        self.add_segment(self.segment_list[-1].position())

    def move(self):
        for segment_num in range(len(self.segment_list) - 1, 0, -1):
            x_pos = self.segment_list[segment_num - 1].xcor()
            y_pos = self.segment_list[segment_num - 1].ycor()
            direction = self.segment_list[segment_num - 1].heading()
            self.segment_list[segment_num].goto(x_pos, y_pos)
            self.segment_list[segment_num].setheading(direction)
        self.segment_list[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segment_list[0].heading() != 270:
            self.segment_list[0].setheading(90)

    def down(self):
        if self.segment_list[0].heading() != 90:
            self.segment_list[0].setheading(270)

    def turn_left(self):
        if self.segment_list[0].heading() != 0:
            self.segment_list[0].setheading(180)

    def turn_right(self):
        if self.segment_list[0].heading() != 180:
            self.segment_list[0].setheading(0)
