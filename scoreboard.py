from turtle import Turtle

# constants
FONT14 = ('Arial', 14, 'normal')
FONT22 = ('Arial', 22, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.reset_format()
        self.score = 0
        self.high_score = self.read_file()
        self.user = ""

    def reset_format(self):
        self.color("white")
        self.up()
        self.hideturtle()

    # display the player's score at the top of the screen
    def show_score(self, player):
        self.user = player
        self.clear()
        self.goto(-280, 280)
        self.write(arg=f"{player}'s Score: {self.score}",
                   align="left",
                   font=FONT14)
        self.goto(280, 280)
        self.write(arg=f"High Score: {self.high_score}",
                   align="right",
                   font=FONT14)

    # display the "game over" text at the center of the screen
    def game_over(self):
        # self.clear()
        self.update_high_score()
        self.score = 0
        # self.show_score(self.user)
        self.home()
        self.write(arg="GAME OVER",
                   align="center",
                   font=FONT14)

    def update_high_score(self):
        if self.score > self.high_score:
            self.update_file()
            self.high_score = self.read_file()
            self.show_score(self.user)
            self.goto(0, 150)
            self.write(arg=f"NEW HIGH SCORE !!",
                       align="center",
                       font=FONT22)

    def update_file(self):
        with open("high_score.txt", mode="w") as file:
            file.write(f"{self.score}")

    def read_file(self):
        with open("high_score.txt") as file:
            return int(file.read())
