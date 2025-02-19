from turtle import Screen
from functools import partial
import time

from spaceship import Spaceship

class SpaceInvadersGame():
    def __init__(self):
        self._screen = Screen()
        self._screen.setup(width=800, height=600)
        self._screen.bgcolor('black')
        self._screen.title('Space Invaders')
        self._screen.register_shape('spaceship.gif')
        self._screen.tracer(0)

        self._spaceship = Spaceship()

         # Listen to key events
        self._screen.listen()
        self._screen.onkeypress(partial(self._spaceship.move, "up"), "Up")
        self._screen.onkeypress(partial(self._spaceship.move, "down"), "Down")
        self._screen.onkeypress(partial(self._spaceship.move, "left"), "Left")
        self._screen.onkeypress(partial(self._spaceship.move, "right"), "Right")

    def run(self):
        self._screen.listen()
        self._game_is_on = True
        
        while self._game_is_on:
            self._screen.update()
            
        
        self._screen.exitonclick()


if __name__ == '__main__':
    space_invaders = SpaceInvadersGame()
    space_invaders.run()