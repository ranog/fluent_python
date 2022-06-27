from collections.abc import Iterable
from typing import Counter


def mode(data: Iterable[float]) -> float:
    pairs = Counter(data).most_common(1)
    if len(pairs) == 0:
        raise ValueError('no mode for empty data')
    return pairs[0][0]


print(mode([1, 1, 2, 3, 3, 3, 3, 4]))
