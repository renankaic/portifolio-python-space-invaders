from turtle import Turtle

from utils import Direction

SHAPE = "assets/img/invader_frames/invader-1.gif"


class Invader(Turtle):
    def __init__(
        self,
        starting_position: tuple[int, int],
        move_distance: int,
        shape=SHAPE,
        undobuffersize=1000,
        visible=True,
    ):
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.color("red")
        self.goto(starting_position)
        self.setheading(270)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.speed("fastest")
        self.move_distance = move_distance
        self._bullets = []        

    def move(self, direction: Direction):
        if direction == Direction.RIGHT:
            self.setx(self.xcor() + self.move_distance)
        elif direction == Direction.LEFT:
            self.setx(self.xcor() - self.move_distance)
        elif direction == Direction.DOWN:
            self.sety(self.ycor() - self.move_distance)
    
    def change_shape(self):
        if self.shape() == "assets/img/invader_frames/invader-1.gif":
            self.shape("assets/img/invader_frames/invader-2.gif")
        elif self.shape() == "assets/img/invader_frames/invader-2.gif":
            self.shape("assets/img/invader_frames/invader-3.gif")
        elif self.shape() == "assets/img/invader_frames/invader-3.gif":
            self.shape("assets/img/invader_frames/invader-4.gif")
        elif self.shape() == "assets/img/invader_frames/invader-4.gif":
            self.shape("assets/img/invader_frames/invader-5.gif")
        elif self.shape() == "assets/img/invader_frames/invader-5.gif":
            self.shape("assets/img/invader_frames/invader-6.gif")
        elif self.shape() == "assets/img/invader_frames/invader-6.gif":
            self.shape("assets/img/invader_frames/invader-1.gif")

