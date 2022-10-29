import turtle

IN_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in IN_POSITIONS:
            self.add_segment(position)

    def movement(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def add_segment(self, position):
        snake_body = turtle.Turtle('square')
        snake_body.color('white')
        snake_body.up()
        snake_body.goto(position)
        self.segments.append(snake_body)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def upwards(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def downwards(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
