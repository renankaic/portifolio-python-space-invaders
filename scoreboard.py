from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
HIGHSCORE_FILENAME = "highscore.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.load_high_score()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.update_scoreboard()

    def load_high_score(self):
        try:
            with open(HIGHSCORE_FILENAME, mode="r") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            self.high_score = 0
            

    def save_high_score(self):
        with open(HIGHSCORE_FILENAME, mode="w") as file:
            file.write(str(self.high_score))
