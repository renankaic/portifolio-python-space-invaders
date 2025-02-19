from turtle import Screen
from spaceship import Spaceship
from invader import Invader
import time

class SpaceInvadersGame():
    def __init__(self):
        self._screen = Screen()
        self._screen.setup(width=800, height=600)
        self._screen.bgcolor('black')
        self._screen.title('Space Invaders')
        self._screen.register_shape('spaceship.gif')
        self._screen.register_shape('invader.gif')
        self._screen.tracer(0)

        self._spaceship = Spaceship(shape='spaceship.gif')
        self.set_keys_listeners()

        self._invaders = []
       

    def run(self):
        self._screen.listen()
        self._game_is_on = True

        for n in range (40):
            if n < 10:
                start_position = (-330 + n * 50, 250)
            elif n < 20:
                n -= 10
                start_position = (-330 + n * 50, 200)
            elif n < 30:
                n -= 20
                start_position = (-330 + n * 50, 150)
            else:
                n -= 30
                start_position = (-330 + n * 50, 100)

            invader = Invader(start_position)
            self._invaders.append(invader)
        
        while self._game_is_on:
            self._screen.update()
            time.sleep(0.025)  # Reduce sleep duration for smoother performance
            self._spaceship.move_bullets()
        
        self._screen.exitonclick()

    def set_keys_listeners(self):        
        self._screen.listen()
        self._screen.onkeypress(self._spaceship.move_up, "Up")
        self._screen.onkeypress(self._spaceship.move_down, "Down")
        self._screen.onkeypress(self._spaceship.move_left, "Left")
        self._screen.onkeypress(self._spaceship.move_right, "Right")
        self._screen.onkeypress(self._spaceship.shoot, "space")

if __name__ == '__main__':
    space_invaders = SpaceInvadersGame()
    space_invaders.run()