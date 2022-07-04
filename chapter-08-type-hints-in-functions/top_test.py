from collections.abc import Iterator
from typing import TYPE_CHECKING

import pytest

from top import top


def test_top_tuples() -> None:
    fruit = 'mango pear apple kiwi banana'.split()
    series: Iterator[tuple[int, str]] = ((len(s), s) for s in fruit)
    length = 3
    expected = [(6, 'banana'), (5, 'mango'), (5, 'apple')]
    result = top(series=series, length=length)
    if TYPE_CHECKING:
        reveal_type(series)     # NOQA
        reveal_type(expected)   # NOQA
        reveal_type(result)     # NOQA
    assert result == expected


def test_top_objects_error() -> None:
    series = [object() for _ in range(4)]
    if TYPE_CHECKING:
        reveal_type(series)     # NOQA
    with pytest.raises(TypeError) as excinfo:
        top(series=series, length=3)
    assert "'<' not supported" in str(excinfo.value)
