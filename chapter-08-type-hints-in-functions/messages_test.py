import pytest

from messages import show_count


@pytest.mark.parametrize('qty, expected', [(1, '1 part'), (2, '2 parts')])
def test_show_count(qty, expected):
    got = show_count(qty, 'part')
    assert got == expected


def test_show_count_zero():
    got = show_count(0, 'part')
    assert got == 'no parts'
