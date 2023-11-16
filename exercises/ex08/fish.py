"""File to define Fish class."""


__author__ = "730556372"


class Fish:
    """Simulating a fish."""

    age: int
    
    def __init__(self):
        """Initializing the age."""
        self.age = 0
    
    def one_day(self):
        """Updating fish."""
        self.age += 1