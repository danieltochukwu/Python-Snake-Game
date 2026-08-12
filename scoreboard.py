from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the score display"""
        self.clear()
        self.write(f"Daniel's Game Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increase score by 1"""
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        """Display game over message"""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)