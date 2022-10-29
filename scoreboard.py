from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = 0
        self.color('White')
        self.hideturtle()
        self.up()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-60, 270)
        self.write(f"Score = {self.score} ", align="center", font=("Arial", 18, "normal"))
        self.goto(60, 270)
        self.write(f", Highest = {self.highest_score} ", align="center", font=("Arial", 18, "normal"))

    #def game_over(self):
        #self.goto(0, 0)
        #self.write("Game Over.", align="center", font=("Arial", 22, "normal"))

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
        self.score = 0
        self.update_scoreboard()
