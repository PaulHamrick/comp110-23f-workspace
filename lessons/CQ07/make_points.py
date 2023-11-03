"""Testing point.py."""
from lessons.CQ07.point import Point


origin: Point = Point(0, 0)
origin.x = 50
origin.scale_by(0.5)
print(origin.x)
