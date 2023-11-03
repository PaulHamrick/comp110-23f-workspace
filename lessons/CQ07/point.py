"""Creating a class of points."""
from __future__ import annotations


class Point:
    """Creating a point in the Cartesian plane."""
    x: float
    y: float
    
    def __init__(self, x_init: float, y_init: float):
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

        