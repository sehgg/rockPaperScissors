# NEEDED CLASSES --------------------------------------------------------------
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

import random

from choices import BaseChoice, Rock, Paper, Scissors


# CLASSES ---------------------------------------------------------------------
@dataclass
class BasePlayer(ABC):

    name: str = field(default="name")
    choice: BaseChoice = field(default=None)
    possible_choices: dict = field(
        default_factory=lambda: {"1": Rock(), "2": Paper(), "3": Scissors()},
    )

    @abstractmethod
    def select_choice(self):
        pass


@dataclass
class ManualPlayer(BasePlayer):

    def select_choice(self):
        self.choice = self.possible_choices[
            input("Select choice (1-Rock | 2-Paper | 3-Scissors): ")
        ]


@dataclass
class ComputerPlayer(BasePlayer):

    def __post_init__(self):
        super().__init__(name="Computer")

    def select_choice(self):
        self.choice = self.possible_choices[random.choice("1 2 3".split())]
