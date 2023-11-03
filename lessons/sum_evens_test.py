"""Testing my summation function."""

from lessons.sum_evens import sum_evens_in_list

def test_empty_sum() -> None:
    """sum_evens_in_list of empty list should be 0"""
    assert sum_evens_in_list([]) == 0