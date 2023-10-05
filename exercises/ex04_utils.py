"""EX04 - Recreating some Python tools from scratch."""

__author__ = "730556372"


def all(some_integers: list[int], check_int: int) -> bool:
    """Checking if all the integers in a list are equal to a particular integer."""
    list_length: int = len(some_integers)
    if list_length == 0:  # Checking if the list is empty
        return False
    list_idx: int = 0
    while (list_idx < list_length):  # Looping through indices to check if there is 
        # an integer in the list not equal to the particular integer
        if some_integers[list_idx] != check_int:
            return False
        list_idx += 1
    return True


def max(integer_list: list[int]) -> int:
    """Getting the greatest number from a list."""
    list_length: int = len(integer_list)
    if list_length == 0:
        raise ValueError("max() arg is an empty List")
    
    list_max: int = integer_list[0]  # Initializing the maximum
    list_idx: int = 1  # We can start the index at 1 
    # since there is no sense in comparing the first element of the list to itself

    while (list_idx < list_length):  # The loop will not run if the list has one element
        if integer_list[list_idx] > list_max:
            list_max = integer_list[list_idx]  # Updating the maximum
        list_idx += 1
    return list_max


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Figuring out if two lists are the same."""
    if len(first_list) != len(second_list):  # Making sure the lengths are the same
        return False
    
    list_length: int = len(first_list)
    idx: int = 0
    while (idx < list_length):  # Looping through indices to check if they are equal
        if first_list[idx] != second_list[idx]:
            return False
        idx += 1
    return True
