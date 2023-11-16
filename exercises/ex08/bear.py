"""File to define Bear class."""


__author__ = "730556372"


class Bear:
    """Simulating a bear."""

    age: int
    hunger_score: int
    
    def __init__(self):
        """Initializing the age and hunger score."""
        self.age = 0
        self.hunger_score = 0
    
    def one_day(self):
        """Updating bear."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        """Eating fish."""
        self.hunger_score += num_fish