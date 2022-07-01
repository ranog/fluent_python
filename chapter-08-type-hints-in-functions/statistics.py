from collections.abc import Iterable
from decimal import Decimal
from fractions import Fraction
from typing import Counter, TypeVar

NumberT = TypeVar('NumberT', float, Decimal, Fraction)


def mode(data: Iterable[NumberT]) -> float:
    pairs = Counter(data).most_common(1)
    if len(pairs) == 0:
        raise ValueError('no mode for empty data')
    return pairs[0][0]


print(mode([1, 1, 2, 3, 3, 3, 3, 4]))
print(mode(["red", "blue", "blue", "red", "green", "red", "red"]))
