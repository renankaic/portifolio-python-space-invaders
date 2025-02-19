from turtle import Turtle

MOVE_DISTANCE = 15
SHAPE = 'invader.gif'

class Invader(Turtle):
    def __init__(self, starting_position: tuple[int, int], shape = SHAPE, undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.color("red")
        self.goto(starting_position)
        self.setheading(270)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.speed("fastest")
        self._bullets = []
    

