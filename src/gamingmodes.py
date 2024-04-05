# NEEDED PACKAGES -------------------------------------------------------------
from player import BasePlayer, ManualPlayer, ComputerPlayer


# CLASSES ---------------------------------------------------------------------
class BaseGamingMode():

    player1: BasePlayer
    player2: BasePlayer

    def select_choices(self):

        self.player1.select_choice()
        self.player2.select_choice()

    def select_winner(self):

        if self.player1.choice.wins is type(self.player2.choice):
            self.print_choices()
            print(f"{self.player1.name} wins")
        elif self.player1.choice.loses is type(self.player2.choice):
            self.print_choices()
            print(f"{self.player2.name} wins")
        else:
            self.print_choices()
            print("Draw")

    def print_choices(self):
        print(self.player1.choice.symbol)
        print(self.player2.choice.symbol)


class PlayerVsPlayer(BaseGamingMode):

    def __init__(self):

        self.player1 = ManualPlayer(name=input("Enter Player1 name: "))
        self.player2 = ManualPlayer(name=input("Enter Player2 name: "))


class PlayerVsComputer(BaseGamingMode):

    def __init__(self):

        self.player1 = ManualPlayer(name=input("Enter Players name: "))
        self.player2 = ComputerPlayer()
