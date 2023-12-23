from turtle import Turtle

FONT = ("Courier", 24, "normal")
HOME_POSITION = (0,230)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(HOME_POSITION)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=("Arial", 30, "normal"))

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.penup()
        self.level += 1
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 50, "normal"))

