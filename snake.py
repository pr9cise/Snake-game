from turtle import Turtle


class Snake:

    def __init__(self):
        self.turtle_list = []
        self.game_state = True
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            new_turtle = Turtle()
            self.turtle_list.append(new_turtle)
            self.turtle_list[i].shape("square")
            self.turtle_list[i].color("white")
            self.turtle_list[i].up()
            self.turtle_list[i].forward(-20 * i)

    def move(self):
        for i in range(len(self.turtle_list) - 1, 0, -1):
            self.turtle_list[i].goto(self.turtle_list[i - 1].pos())
        self.turtle_list[0].forward(20)

    def up(self):
        if self.turtle_list[0].heading() == 270.0:
            self.game_state = False
        else:
            self.turtle_list[0].setheading(90)

    def down(self):
        if self.turtle_list[0].heading() == 90.0:
            self.game_state = False
        self.turtle_list[0].setheading(270)

    def right(self):
        if self.turtle_list[0].heading() == 180.0:
            self.game_state = False
        self.turtle_list[0].setheading(0)

    def left(self):
        if self.turtle_list[0].heading() == 0.0:
            self.game_state = False
        self.turtle_list[0].setheading(180)

    def new_segment(self, pos):
        new_turtle = Turtle()
        new_turtle.shape("square")
        new_turtle.color("white")
        new_turtle.up()
        new_turtle.goto(pos)
        self.turtle_list.append(new_turtle)

    def extend(self):
        self.new_segment(self.turtle_list[-1].pos())

    def reset(self):
        for i in self.turtle_list:
            i.setpos(1000, 1000)
        self.turtle_list.clear()
        self.create_snake()