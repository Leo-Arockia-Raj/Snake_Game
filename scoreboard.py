from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(arg=f"Score : {self.score} High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.print_score()

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
            self.score = 0
            self.print_score()
