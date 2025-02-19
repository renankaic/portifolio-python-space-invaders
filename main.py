from turtle import Screen
from spaceship import Spaceship
import time

class SpaceInvadersGame():
    def __init__(self):
        self._screen = Screen()
        self._screen.setup(width=800, height=600)
        self._screen.bgcolor('black')
        self._screen.title('Space Invaders')
        self._screen.register_shape('spaceship.gif')
        self._screen.tracer(0)

        self._spaceship = Spaceship()
        self.set_keys_listeners()

    def run(self):
        self._screen.listen()
        self._game_is_on = True
        
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