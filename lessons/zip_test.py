"""Testing my zip function."""

__author__ = "730556372"

from lessons.zip import zip


def test_diff() -> None:
    """Zip of a list of strings and a list of some integers with different lengths should be empty."""
    assert zip(["apple"], [1, 3, 7]) == {}


def test_short_list() -> None:
    """Checking zip of two short lists of strings and integers respectively with the same length is what it ought to be."""
    assert zip(["cravat", "crevasse"], [0, 7]) == {'cravat': 0, 'crevasse': 7}


def test_long_list() -> None:
    """Checking zip of two long lists of strings and integers respectively with the same length is what it ought to be."""
    assert zip(["lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit"], [0, 1, 2, 3, 4, 5, 6, 7]) == {'lorem': 0, 'ipsum': 1, 'dolor': 2, 'sit': 3, 'amet': 4, 'consectetur': 5, 'adipiscing': 6, 'elit': 7}