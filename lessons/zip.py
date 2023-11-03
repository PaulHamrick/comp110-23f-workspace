"""Combining two lists into a dictionary."""

__author__ = "730556372"


def zip(strings: list[str], ints: list[int]) -> dict[str, int]:
    """Zipping together a list of strings and a list of integers."""
    if len(strings) != len(ints):  # Making sure the zip function can be applied
        return {}
    new_dictionary: dict[str, int] = {}
    idx: int = 0
    while idx < len(strings):
        new_dictionary[strings[idx]] = ints[idx]
        idx += 1
    return new_dictionary
    