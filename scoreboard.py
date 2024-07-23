from turtle import Turtle

HIGH_SCORE_PATH = "high_score_file.txt"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.number = 0
        with open(HIGH_SCORE_PATH, mode="r") as file:
            file_data = file.read()
            self.high_score = int(file_data)
        self.up()
        self.goto(0, 270)
        self.color("white")
        self.font = ("Courier", 20, "bold")
        self.align = "center"
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.number} High Score: {self.high_score}", align=self.align, font=self.font)

    def reset(self):
        if self.number > self.high_score:
            self.high_score = self.number
            with open(HIGH_SCORE_PATH, mode="w") as file:
                file.write(str(self.high_score))
        self.number = 0
        self.update_scoreboard()

    def score_increase(self):
        self.number += 1
        self.update_scoreboard()
