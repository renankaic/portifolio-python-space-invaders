from turtle import Turtle


class Scoreboard(Turtle):
    ALIGNMENT = "center"
    FONT = ("Courier", 24, "normal")
    HIGHSCORE_FILENAME = "highscore.txt"

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
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=self.ALIGNMENT, font=self.FONT)
    
    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.update_scoreboard()
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.update_scoreboard()

    def load_high_score(self):
        try:
            with open(self.HIGHSCORE_FILENAME, mode="r") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            self.high_score = 0

    def save_high_score(self):
        with open(self.HIGHSCORE_FILENAME, mode="w") as file:
            file.write(str(self.high_score))


class TextGameOver(Turtle):
    ALIGNMENT = "center"
    FONT = ("Courier", 48, "normal")

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 0)


    def show(self):
        self.clear()
        self.write(f"GAME OVER!", align=self.ALIGNMENT, font=self.FONT)


class TextNewGame(Turtle):
    ALIGNMENT = "center"
    FONT = ("Courier", 36, "normal")

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, -100)

    def show(self):
        self.clear()
        self.write(f"Press space to restart...", align=self.ALIGNMENT, font=self.FONT)