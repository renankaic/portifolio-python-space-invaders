from turtle import Screen
from spaceship import Spaceship
from invader import Invader
import time
import os

from utils import Direction

class SpaceInvadersGame():
    def __init__(self):
        self._screen = Screen()
        self._screen.setup(width=800, height=600)
        self._screen.bgcolor('black')
        self._screen.title('Space Invaders')                
        self._screen.tracer(0)

        self._screen.register_shape('spaceship.gif')
        self._spaceship = Spaceship(shape='spaceship.gif')
        self.set_keys_listeners()

        self._invaders = []
        self._invaders_last_move = 0
        self._invaders_current_move_direction = Direction.RIGHT

        for invader_gif_filename in os.listdir('assets/img/invader_frames'):
          self._screen.register_shape(f'assets/img/invader_frames/{invader_gif_filename}')

    def run(self):
        self._screen.listen()
        self._game_is_on = True
        self._loop_count = 0 

        # Create 40 invaders        
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

            invader = Invader(starting_position=start_position)

            # Create a new row of invaders every 10 invaders
            if len(self._invaders) <= n // 10:
                self._invaders.append([])

            # Add the invader to the last row
            self._invaders[n // 10].append(invader)
        
        while self._game_is_on:
            self._screen.update()
            time.sleep(0.025)  # Reduce sleep duration for smoother performance
            self._spaceship.move_bullets()
            self.check_bullet_collision()
            self.move_invaders()

            # Change invader shape every 25 loops
            if self._loop_count % 25 == 0:
                for row in self._invaders:
                    for invader in row:
                        # Invader is hidden when it is hit by a bullet
                        if invader is not None:
                          invader.change_shape()
                self._loop_count = 0

            self._loop_count += 1
        
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
                    if invader is not None:
                      invader.move(self._invaders_current_move_direction)

                      # Move invaders down if they reach the edge
                      if reached_edge:
                          invader.move(Direction.DOWN)
                
            self._invaders_last_move = 0
        else:
            self._invaders_last_move += 1
    
    def check_bullet_collision(self):
       for bullet in self._spaceship.bullets:
          if bullet.ycor() > -100:
             for row in self._invaders:
                for idx, invader in enumerate(row):
                    if invader is not None and self.is_invader_in_area(invader, bullet.xcor(), bullet.ycor()):
                        invader.hideturtle()                        
                        bullet.hideturtle()
                        self._spaceship.bullets.remove(bullet)
                        del bullet
                        row[idx] = None
                        break
              
    
    def is_invader_in_area(self, invader: Invader, x_cor, y_cor):
        invader_x_cor = invader.xcor()
        invader_y_cor = invader.ycor()
        
        # Check if the bullet is in the invader's area
        # The invader's are is a rectangle with width 37 and height 32
        return (invader_x_cor - 18) <= x_cor <= (invader_x_cor + 18) and (invader_y_cor - 16) <= y_cor <= (invader_y_cor + 16)
            

if __name__ == '__main__':
    space_invaders = SpaceInvadersGame()
    space_invaders.run()