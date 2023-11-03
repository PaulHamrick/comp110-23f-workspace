"""Summing the elements of a list using different loops."""

__author__ = "730556372"


def w_sum(vals: list[float]) -> float:
    """Using a while loop to sum the floats."""
    vals_length: int = len(vals)
    idx: int = 0
    vals_sum: float = 0.0
    while (idx < vals_length):
        vals_sum += vals[idx]
        idx += 1
    return vals_sum


def f_sum(vals: list[float]) -> float:
    """Using a for loop on elements of the list to sum the floats."""
    vals_sum: float = 0.0
    for val in vals:
        vals_sum += val
    return vals_sum


def f_range_sum(vals: list[float]) -> float:
    """Using a for loop on indices of the list to sum the floats."""
    vals_length: int = len(vals)
    vals_sum: float = 0.0
    for idx in range(0, vals_length):
        vals_sum += vals[idx]
    return vals_sum
