from turtle import Screen
from spaceship import Spaceship
from invader import Invader
import time

from utils import Direction

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
        self._invaders_last_move = 0
        self._invaders_current_move_direction = Direction.RIGHT
       

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
            if len(self._invaders) <= n // 10:
                self._invaders.append([])
            self._invaders[n // 10].append(invader)
        
        while self._game_is_on:
            self._screen.update()
            time.sleep(0.025)  # Reduce sleep duration for smoother performance
            self._spaceship.move_bullets()
            self.move_invaders()
        
        self._screen.exitonclick()
   
    def set_keys_listeners(self):        
        self._screen.listen()
        self._screen.onkeypress(self._spaceship.move_up, "Up")
        self._screen.onkeypress(self._spaceship.move_down, "Down")
        self._screen.onkeypress(self._spaceship.move_left, "Left")
        self._screen.onkeypress(self._spaceship.move_right, "Right")
        self._screen.onkeypress(self._spaceship.shoot, "space")

    def move_invaders(self):
        if self._invaders_last_move == 10:
            row_with_last_invader = None
            reached_edge = False

            if self._invaders_current_move_direction == Direction.RIGHT:
              # Check if the last invader in the row is at the right edge of the screen
              for row in self._invaders:
                if row[-1] is not None:
                    row_with_last_invader = row
                    break
                            
              if row_with_last_invader is not None:
                if row_with_last_invader[-1].xcor() >= 380:
                  self._invaders_current_move_direction = Direction.LEFT
                  reached_edge = True

            elif self._invaders_current_move_direction == Direction.LEFT:
              # Check if the last invader in the row is at the left edge of the screen
              for row in self._invaders:
                if row[0] is not None:
                    row_with_last_invader = row
                    break
                            
              if row_with_last_invader is not None:
                if row_with_last_invader[0].xcor() <= -380:
                  self._invaders_current_move_direction = Direction.RIGHT
                  reached_edge = True

            for row in self._invaders:
                for invader in row:
                    invader.move(self._invaders_current_move_direction)
                    if reached_edge:
                        invader.move(Direction.DOWN)
                
            self._invaders_last_move = 0
        else:
            self._invaders_last_move += 1


if __name__ == '__main__':
    space_invaders = SpaceInvadersGame()
    space_invaders.run()