from turtle import Screen
from spaceship import Spaceship
from invader import Invader
from texts import Scoreboard, TextGameOver, TextNewGame
import time
import os

from utils import Direction


class SpaceInvadersGame:
    def __init__(self):
        self._screen = Screen()
        self._screen.setup(width=800, height=600)
        self._screen.bgcolor("black")
        self._screen.title("Space Invaders")
        self._screen.tracer(0)

        self._screen.register_shape("spaceship.gif")

        for invader_gif_filename in os.listdir("assets/img/invader_frames"):
            self._screen.register_shape(
                f"assets/img/invader_frames/{invader_gif_filename}"
            )

    def run(self):
        self.clear_screen()
        self._screen.listen()
        self._loop_count = 0

        self._spaceship = Spaceship(shape="spaceship.gif")
        self._scoreboard = Scoreboard()

        self._invaders = []
        self._invaders_count = 0        
        self._invaders_last_move = 0
        self._invaders_current_move_direction = Direction.RIGHT
        self._invaders_move_distance = 15
        
        self.generate_invaders(40)
        self.set_keys_listeners()

        self._game_is_on = True
        while self._game_is_on:
            self._screen.update()
            time.sleep(0.025)  # Reduce sleep duration for smoother performance
            self._spaceship.move_bullets()
            self.move_invaders()
            self.check_collisions()

            if self._game_is_on:
              # Change invader shape every 25 loops
              if self._loop_count % 25 == 0 and self._invaders_count > 0:
                  for row in self._invaders:
                      for invader in row:
                          # Invader is hidden when it is hit by a bullet
                          if invader is not None:
                              invader.change_shape()
                  self._loop_count = 0

              if self._invaders_count == 0:
                  # Increase the move distance of the invaders and generate a new row of invaders (harder level)
                  self._invaders_move_distance += 5
                  self.generate_invaders(40)

              self._loop_count += 1
        
        self.game_over()

    def clear_screen(self):
        for turtle in self._screen.turtles():
            turtle.hideturtle()
            turtle.clear()
            turtle.penup()
            turtle.goto(0, 0)

    def generate_invaders(self, count: int):
        self._invaders = []
        for n in range(count):
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

            invader = Invader(
                starting_position=start_position,
                move_distance=self._invaders_move_distance,
            )

            # Create a new row of invaders every 10 invaders
            if len(self._invaders) <= n // 10:
                self._invaders.append([])

            # Add the invader to the last row
            self._invaders[n // 10].append(invader)
            self._invaders_count += 1
        self._invaders_last_move = 0

    def set_keys_listeners(self):
        self._screen.listen()
        self._screen.onkeypress(self._spaceship.move_up, "Up")
        self._screen.onkeypress(self._spaceship.move_down, "Down")
        self._screen.onkeypress(self._spaceship.move_left, "Left")
        self._screen.onkeypress(self._spaceship.move_right, "Right")
        self._screen.onkeypress(self._spaceship.shoot, "space")

    def move_invaders(self):
        if self._invaders_last_move == 10 and self._invaders_count > 0:
            invader_in_the_edge = None
            reached_edge = False

            if self._invaders_current_move_direction == Direction.RIGHT:
                # Check if the last invader in the row is at the right edge of the screen
                for row in self._invaders:
                    if row[-1] is not None:
                        invader_in_the_edge = row[-1]
                        break

                if invader_in_the_edge is None:
                    invader_in_the_edge = self.get_invader_in_edge()

                if invader_in_the_edge.xcor() >= 380:
                    self._invaders_current_move_direction = Direction.LEFT
                    reached_edge = True

            elif self._invaders_current_move_direction == Direction.LEFT:
                # Check if the last invader in the row is at the left edge of the screen
                for row in self._invaders:
                    if row[0] is not None:
                        invader_in_the_edge = row[0]
                        break

                if invader_in_the_edge is None:
                    invader_in_the_edge = self.get_invader_in_edge()

                if invader_in_the_edge.xcor() <= -380:
                    self._invaders_current_move_direction = Direction.RIGHT
                    reached_edge = True

            for row in self._invaders:
                for invader in row:
                    if invader is not None:
                        invader.move(self._invaders_current_move_direction)

                        # Move invaders down if one of them reach the edge
                        if reached_edge:
                            invader.move(Direction.DOWN)

            self._invaders_last_move = 0
        else:
            self._invaders_last_move += 1

    def get_invader_in_edge(self):
        edge_invader_row = None
        edge_invader_idx = None

        if self._invaders_count == 0:
            return None

        if self._invaders_current_move_direction == Direction.RIGHT:
            max_x_cor = -800

            for row_idx, row in enumerate(self._invaders):
                for invader_idx, invader in enumerate(row):
                    if invader is not None and invader.xcor() > max_x_cor:
                        max_x_cor = invader.xcor()
                        edge_invader_row = row_idx
                        edge_invader_idx = invader_idx

        elif self._invaders_current_move_direction == Direction.LEFT:
            min_x_cor = 800
            for row_idx, row in enumerate(self._invaders):
                for invader_idx, invader in enumerate(row):
                    if invader is not None and invader.xcor() < min_x_cor:
                        min_x_cor = invader.xcor()
                        edge_invader_row = row_idx
                        edge_invader_idx = invader_idx

        return self._invaders[edge_invader_row][edge_invader_idx]

    def check_collisions(self):
        if self._invaders_count == 0:
            return

        for bullet in self._spaceship.bullets:
            for row in self._invaders:
                for idx, invader in enumerate(row):
                    if invader is not None and self.is_invader_in_area(
                        invader, bullet.xcor(), bullet.ycor()
                    ):
                        invader.hideturtle()
                        bullet.hideturtle()
                        self._spaceship.bullets.remove(bullet)
                        del bullet
                        row[idx] = None
                        self._invaders_count -= 1
                        self._scoreboard.increase_score()
                        break

        for row in self._invaders:
            for idx, invader in enumerate(row):
                if invader is not None and self.is_invader_in_area(
                    invader=invader,
                    x_cor=self._spaceship.xcor(),
                    y_cor=self._spaceship.ycor(),
                    x_cor_offset=25,
                    y_cor_offset=18,
                ):
                    self._game_is_on = False
                    break

    def is_invader_in_area(
        self,
        invader: Invader,
        x_cor: int,
        y_cor: int,
        x_cor_offset: int = 0,
        y_cor_offset: int = 0,
    ):
        invader_x_cor = invader.xcor()
        invader_y_cor = invader.ycor()

        # Check if the invader is in an specific area
        if x_cor_offset != 0 and y_cor_offset != 0:
            return (
                (invader_x_cor - 18) <= (x_cor - x_cor_offset) <= (invader_x_cor + 18)
                and (invader_y_cor - 16)
                <= (y_cor - y_cor_offset)
                <= (invader_y_cor + 16)
            ) or (
                (invader_x_cor - 18) <= (x_cor + x_cor_offset) <= (invader_x_cor + 18)
                and (invader_y_cor - 16)
                <= (y_cor + y_cor_offset)
                <= (invader_y_cor + 16)
            )
        else:
            # The invaders are a rectangle with width 37 and height 32
            
            return (invader_x_cor - 18) <= x_cor <= (invader_x_cor + 18) and (
                invader_y_cor - 16
            ) <= y_cor <= (invader_y_cor + 16)

    def game_over(self):
        self._game_is_on = False

        TextGameOver().show()
        self._screen.update()

        time.sleep(2)
        
        TextNewGame().show()
        self._screen.update()

        self._screen.onkeypress(self.run, "space")
        self._screen.exitonclick()
    

if __name__ == "__main__":
    space_invaders = SpaceInvadersGame()
    space_invaders.run()
