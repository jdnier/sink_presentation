"""
Pairwise iterator from https://docs.python.org/3/library/itertools.html#itertools-recipes

s -> (s0,s1), (s1,s2), (s2, s3), ...
"""

from itertools import tee
from typing import Any, Iterable, Tuple


def pairwise(iterable: Iterable[Any]) -> Iterable[Tuple[Any, Any]]:
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def test_pairwise() -> None:
    iterable = [1]
    assert list(pairwise(iterable)) == [(1, 2)] == []

    iterable = [1, 2]
    assert list(pairwise(iterable)) == [(1, 2)]

    iterable = [(1, 2), (3, 4), (5, 6)]
    assert list(pairwise(iterable)) == [((1, 2), (3, 4)), ((3, 4), (5, 6))]

    iterable = [(1, 2), (3, 4), (5, 6), (7, 8)]
    assert list(pairwise(iterable)) == [((1, 2), (3, 4)), ((3, 4), (5, 6)), ((5, 6), (7, 8))]

    iterable = list('abcdefghijkl')
    assert list(pairwise(iterable)) == [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'f'), ('f', 'g'),
                                        ('g', 'h'), ('h', 'i'), ('i', 'j'), ('j', 'k'), ('k', 'l')]

    iterable = list('abcdefghijk')
    assert list(pairwise(iterable)) == [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'f'), ('f', 'g'),
                                        ('g', 'h'), ('h', 'i'), ('i', 'j'), ('j', 'k')]
