from turtle import Screen


class Prompt:

    def __init__(self):
        super().__init__()
        self.screen = Screen()

    def get_player_name(self):
        return self.screen.textinput("Player's Name", "Please enter your name:")

    def play_again(self):
        return self.screen.textinput("GAME OVER", "Play again? Y/N")
