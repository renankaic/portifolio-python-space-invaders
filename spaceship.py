from turtle import Turtle
STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 25

class Spaceship(Turtle):
    def __init__(self):
        super().__init__(shape='spaceship.gif', undobuffersize=1000, visible=True)
        self.penup()
        self.color("white")
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.speed("fastest")

        self._bullets = []

    def move_up(self):
        if self.ycor() < 150:
            self.forward(MOVE_DISTANCE)

    def move_down(self):
        if self.ycor() > -270:
            self.backward(MOVE_DISTANCE)

    def move_left(self):
        if self.xcor() > -380:
            self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())

    def move_right(self):
        if self.xcor() < 380:
            self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())

    def shoot(self):
        if len(self._bullets) > 7:
            return
        
        bullet = Turtle('classic')
        bullet.color("yellow") 
        bullet.penup()
        bullet.setheading(90)
        bullet.shapesize(stretch_wid=0.5, stretch_len=0.5)
        bullet.goto(self.xcor(), self.ycor())
        bullet.speed("fast")
        self._bullets.append(bullet)

    @property
    def bullets(self):
        return self._bullets
    
    def move_bullets(self):
        for bullet in self._bullets:
            bullet.forward(20)
            if bullet.ycor() > 300:
                self._bullets.remove(bullet)
                bullet.hideturtle()
                del bullet