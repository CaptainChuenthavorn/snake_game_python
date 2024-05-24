from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        # self.write()
        self.penup()
        self.hideturtle()
        self.color("White")
        self.pensize(30)
        self.goto(0, 310)
        self.write(f"Score : {self.score}", False, align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.write(f"Score : {self.score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)
