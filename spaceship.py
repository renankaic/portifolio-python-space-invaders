from turtle import Turtle
STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 20

class Spaceship(Turtle):
    def __init__(self):
        super().__init__(shape='spaceship.gif', undobuffersize=1000, visible=True)
        self.penup()
        self.color("white")
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.speed("fast")

    def move(self, direction):
        if direction == "up":
            self.forward(MOVE_DISTANCE)
        elif direction == "down":
            self.backward(MOVE_DISTANCE)
        elif direction == "left":
            self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())
        elif direction == "right":
            self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())
