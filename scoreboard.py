from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"SCORE : {self.score}",align= ALIGNMENT,font= FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align= ALIGNMENT, font= FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
