# At the end of chapter 5

from dataclasses import dataclass


@dataclass
class Spam:
    repeat: int  # instance attribute


@dataclass
class SpamNinetyNine:
    repeat: int = 99  # instance attribute
