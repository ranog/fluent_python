from collections.abc import Iterable
from typing import TypeVar

from comparable import SupportsLessThan


LT = TypeVar('LT', bound=SupportsLessThan)


def top(series: Iterable[LT], length: int) -> list[LT]:
    ordered = sorted(series, reverse=True)
    return ordered[:length]


print(top([4, 1, 5, 2, 6, 7, 3], 3))

l1 = 'mango pear apple kiwi banana'.split()
print(top(l1, 3))

l2 = [(len(s), s) for s in l1]
print(l2)
print(top(l2, 3))

l3 = [object() for _ in range(4)]
print(l3)
print(sorted(l3))
