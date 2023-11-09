"""Creating a class of points."""
from __future__ import annotations


class Point:
    """Creating a point in the Cartesian plane."""
    x: float
    y: float
    
    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """My constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Scaling my point."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Creating a new scaled point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __str__(self) -> str:
        """Writing the point as a string."""
        point_string: str = f"x: {self.x}; y: {self.y}"
        return point_string
    
    def __mul__(self, factor: int | float) -> Point:
        """Creating a new scaled point with the * operator."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __add__(self, addend: int | float) -> Point:
        """Creating a new point with something added to the x and y coordinates."""
        new_point: Point = Point(self.x + addend, self.y + addend)
        return new_point


        