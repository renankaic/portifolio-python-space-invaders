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

        self._bullets = []

    def move(self, direction):
        if direction == "up" and self.ycor() < 150:
            self.forward(MOVE_DISTANCE)
        elif direction == "down" and self.ycor() > -270:
            self.backward(MOVE_DISTANCE)
        elif direction == "left" and self.xcor() > -380:
            self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())
        elif direction == "right" and self.xcor() < 380:
            self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())

    def shoot(self):
        bullet = Turtle('classic')
        bullet.color("yellow") 
        bullet.penup()
        bullet.setheading(90)
        bullet.shapesize(stretch_wid=0.5, stretch_len=0.5)
        bullet.goto(self.xcor(), self.ycor())
        bullet.speed("fastest")
        self._bullets.append(bullet)

    @property
    def bullets(self):
        return self._bullets
    
    def move_bullets(self):
        for bullet in self._bullets:
            bullet.forward(25)
            if bullet.ycor() > 300:
                self._bullets.remove(bullet)
                bullet.hideturtle()
                del bullet