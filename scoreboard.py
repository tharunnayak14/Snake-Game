from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data") as file:
            self.HighScore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score = {self.score} | High Score = {self.HighScore}", True, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.goto(0, 270)

        self.update_scoreboard()

    def reset(self):
        if self.score > self.HighScore:
            self.HighScore = self.score
            with open("data", mode="w") as file:
                file.write(f"{self.HighScore}")
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", True, align=ALIGNMENT, font=FONT)
