# NEEDED PACKAGES -------------------------------------------------------------
from abc import ABC
from dataclasses import dataclass


# CLASSES ---------------------------------------------------------------------
@dataclass
class BaseChoice(ABC):

    symbol: str = None
    wins: None = None
    loses: None = None


@dataclass
class Rock(BaseChoice):

    def __post_init__(self):
        super().__init__()
        self.symbol = '''
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        '''
        self.wins = Scissors
        self.loses = Paper


@dataclass
class Paper(BaseChoice):

    def __post_init__(self):
        super().__init__()
        self.symbol = '''
            _______
        ---'   ____)____
                    ______)
                    _______)
                    _______)
        ---.__________)
        '''
        self.wins = Rock
        self.loses = Scissors


@dataclass
class Scissors(BaseChoice):

    def __post_init__(self):
        super().__init__()
        self.symbol = '''
            _______
        ---'   ____)____
                    ______)
                __________)
                (____)
        ---.__(___)
        '''
        self.wins = Paper
        self.loses = Rock
