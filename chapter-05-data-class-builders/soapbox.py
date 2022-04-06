# At the end of chapter 5

from dataclasses import dataclass
from typing import ClassVar


@dataclass
class SpamInstanceAttribute:
    repeat: int  # instance attribute


@dataclass
class SpamNinetyNineInstanceAttribute:
    repeat: int = 99  # instance attribute


@dataclass
class SpamClassAttribute:
    repeat = 99  # class attribute!


@dataclass
class SpamPseudoType:
    repeat: ClassVar[int] = 99  # aarcht (unpythonic)!
