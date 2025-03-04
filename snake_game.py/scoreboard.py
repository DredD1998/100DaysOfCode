from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial",15,"normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("snake_game.py/data.txt") as file:
            self.high_score = int(file.read())

        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)
        self.hideturtle()
        self.update_scoreboard()
     

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",align=ALIGNMENT,font=FONT)



    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake_game.py/data.txt","w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over",align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
