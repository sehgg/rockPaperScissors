# NEEDED PACKAGES -------------------------------------------------------------
from gamingmodes import PlayerVsPlayer, PlayerVsComputer


# GLOBALS ---------------------------------------------------------------------
LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'


# CLASSES ---------------------------------------------------------------------
class App():

    def __init__(self):

        self.logo = ""
        self.select_gaming_mode()
        self.play()

    def select_gaming_mode(self):

        aux = int(input("Select gaming mode (1 - Player vs. Player | 2 - Player vs. Computer)"))

        if aux == 1:
            self.game = PlayerVsPlayer()
        elif aux == 2:
            self.game = PlayerVsComputer()
        else:
            print("Unsupported setting please restart the game")

    def play(self):

        game_on = True
        while game_on:
            self.game.select_choices()
            self.game.select_winner()

            aux = input("Do you want to play another round? (y/n): ")

            if aux.lower() == "n":
                game_on = False
            else:
                self.clear_screen()

    def clear_screen(self):

        for i in range(0, 19):
            print(LINE_UP, end=LINE_CLEAR)


# RUN -------------------------------------------------------------------------
if __name__ == "__main__":
    game = App()
