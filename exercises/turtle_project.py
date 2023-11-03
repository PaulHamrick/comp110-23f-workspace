"""EX05 - Drawing something in Python.

I broke up complex functions: see what I did to make the full penguin function on lines 215-263.
For above and beyond:
I used the circle method to define the eye on lines 129-138, though I got that idea from EdStem, and I used random in lines 235-255 to make the penguins face right or left.
"""

__author__ = "730556372"

from turtle import Turtle, colormode, done
import random


def main() -> None:
    """Where the full body of the code resides."""
    colormode(255)
    perry: Turtle = Turtle()
    sky_line(perry, 200, 150)
    snow_fill(perry, 200, 150)
    # I wanted to add some shadow to the ice, but I couldn't figure out how to make a gradient.
    idx: int = 0
    while (idx < 6):  # Making six penguins with random locations
        penguin_size: float = random.uniform(100, 200)
        penguin_x: float = random.uniform(-300, 300)
        penguin_y: float = random.uniform(-350, 50)
        penguin(perry, penguin_x, penguin_y, penguin_size)
        idx += 1
    perry.hideturtle()
    done()


def line(achilles: Turtle, x1: float, y1: float, x2: float, y2: float) -> None:
    """Using goto to make a line."""
    achilles.penup()
    achilles.goto(x1, y1)
    achilles.pendown()
    achilles.goto(x2, y2)


def changeTurtleColor(achilles: Turtle, rgb_color: list[int]) -> None:
    """Changing turtle color using a list with three integers."""
    achilles.color(rgb_color[0], rgb_color[1], rgb_color[2])


#  All colors following, save white, were extracted by applying https://imagecolorpicker.com/color-code/c8d4ee 
#  to a picture of penguins in Antarctica
DARK_SNOW: list[int] = [167, 198, 228]
LIGHT_SNOW: list[int] = [200, 212, 238]
SKY: list[int] = [215, 225, 250]
PENGUIN_WHITE: list[int] = [189, 195, 203]
PENGUIN_BLACK: list[int] = [22, 20, 37]
PENGUIN_EYE_WHITE: list[int] = [174, 177, 195]
PENGUIN_PINK: list[int] = [151, 121, 147]
PENGUIN_BEAK_COLOR: list[int] = [69, 48, 68]
PENGUIN_BEAK_GREY: list[int] = [98, 112, 136]
BLACK: list[int] = [0, 0, 0]


def sky_line(achilles: Turtle, y1: float, y2: float) -> None:
    """Making a sky line."""
    changeTurtleColor(achilles, SKY)
    achilles.begin_fill()  # Filling in the top with a skyline
    line(achilles, -400, y1, 400, y2)
    achilles.goto(400, 400)
    achilles.goto(-400, 400)
    achilles.goto(-400, y1)
    achilles.end_fill()


def snow_fill(achilles: Turtle, y1: float, y2: float) -> None:
    """Making the preliminary snow."""
    changeTurtleColor(achilles, DARK_SNOW)
    achilles.begin_fill()  # Making the first layer of snow
    line(achilles, -400, y1, 400, y2)
    achilles.goto(400, y2 - 100)
    achilles.goto(-100, (5 * y1 + 3 * y2) / 8 - 75)
    achilles.goto(-175, (23 * y1 + 9 * y2) / 32 - 40)
    achilles.goto(-225, (25 * y1 + 7 * y2) / 32 - 100)
    achilles.goto(-400, y1 - 100)
    achilles.goto(-400, y1)
    achilles.end_fill()
    changeTurtleColor(achilles, LIGHT_SNOW)
    achilles.begin_fill()  # Making the second layer of snow
    line(achilles, 400, y2 - 100, -100, (5 * y1 + 3 * y2) / 8 - 75)
    achilles.goto(-175, (23 * y1 + 9 * y2) / 32 - 40)
    achilles.goto(-225, (25 * y1 + 7 * y2) / 32 - 100)
    achilles.goto(-400, y1 - 100)
    achilles.goto(-400, -400)
    achilles.goto(400, -400)
    achilles.goto(400, y2 - 100)
    achilles.end_fill()


def penguin_wing_left(achilles: Turtle, x1: float, y1: float, height: float, length: float, slant: float) -> None:
    """Making a left penguin wing."""
    achilles.begin_fill()
    changeTurtleColor(achilles, PENGUIN_BLACK)  # Making the outline in black
    line(achilles, x1, y1, x1, y1 + height)
    achilles.goto(x1 - length / 2, y1 + height)
    achilles.goto(x1 - length, y1 - slant)
    achilles.goto(x1 - length / 4, y1)
    achilles.goto(x1, y1)
    changeTurtleColor(achilles, PENGUIN_PINK)
    achilles.end_fill()


def penguin_wing_right(achilles: Turtle, x1: float, y1: float, height: float, length: float, slant: float) -> None:
    """Making a right penguin wing."""
    # Repeating the code for a left penguin wing
    achilles.begin_fill()
    changeTurtleColor(achilles, PENGUIN_BLACK)
    line(achilles, x1, y1, x1, y1 + height)
    achilles.goto(x1 + length / 2, y1 + height)
    achilles.goto(x1 + length, y1 - slant)
    achilles.goto(x1 + length / 4, y1)
    achilles.goto(x1, y1)
    changeTurtleColor(achilles, PENGUIN_PINK)
    achilles.end_fill()


def my_circle(achilles: Turtle, x1: float, y1: float, size: float) -> None:
    """Setting up a circle function to work the way I want."""
    achilles.penup()
    achilles.goto(x1, y1 - size)  # Moving to the right point for circle to work
    achilles.pendown()
    achilles.circle(size)
    

def penguin_eye(achilles: Turtle, x1: float, y1: float, size: float) -> None:
    """Making a penguin's eye."""
    achilles.begin_fill()
    changeTurtleColor(achilles, PENGUIN_EYE_WHITE)
    my_circle(achilles, x1, y1, size)  # The full eye
    achilles.end_fill()
    achilles.begin_fill()
    changeTurtleColor(achilles, PENGUIN_BLACK)
    my_circle(achilles, x1, y1, size / 3)  # The iris
    achilles.end_fill()


def penguin_beak_left(achilles: Turtle, x1: float, y1: float, size: float) -> None:
    """Making a penguin's beak facing left."""
    changeTurtleColor(achilles, PENGUIN_BEAK_COLOR)
    achilles.begin_fill()  # The outline of the main beak
    line(achilles, x1, y1, x1 - size, y1 + size / 3)
    achilles.goto(x1 - 4 * size / 3, y1 + size / 9)
    achilles.goto(x1 - size, y1 - size / 3)
    achilles.goto(x1, y1)
    achilles.end_fill()
    changeTurtleColor(achilles, PENGUIN_BEAK_GREY)
    achilles.begin_fill()  # The little white part below the beak
    achilles.goto(x1 - size, y1 - size / 3)
    achilles.goto(x1 - 4 * size / 5, y1 - size / 2)
    achilles.goto(x1 - 2 * size / 5, y1 - size / 2)
    achilles.goto(x1 - 2 * size / 5, y1 - size / 5)
    achilles.goto(x1, y1)
    achilles.end_fill()


def penguin_beak_right(achilles: Turtle, x1: float, y1: float, size: float) -> None:
    """Making a penguin's beak facing right."""
    # A mirror version of penguin_beak_left
    changeTurtleColor(achilles, PENGUIN_BEAK_COLOR)
    achilles.begin_fill()  # The outline of the main beak
    line(achilles, x1, y1, x1 + size, y1 + size / 3)
    achilles.goto(x1 + 4 * size / 3, y1 + size / 9)
    achilles.goto(x1 + size, y1 - size / 3)
    achilles.goto(x1, y1)
    achilles.end_fill()
    changeTurtleColor(achilles, PENGUIN_BEAK_GREY)
    achilles.begin_fill()  # The little white part below the beak
    achilles.goto(x1 + size, y1 - size / 3)
    achilles.goto(x1 + 4 * size / 5, y1 - size / 2)
    achilles.goto(x1 + 2 * size / 5, y1 - size / 2)
    achilles.goto(x1 + 2 * size / 5, y1 - size / 5)
    achilles.goto(x1, y1)
    achilles.end_fill()


def penguin_head_left(achilles: Turtle, x1: float, y1: float, size: float) -> None:
    """Making a penguin's head facing left."""
    changeTurtleColor(achilles, PENGUIN_BLACK)
    achilles.begin_fill()  # Main head shape
    line(achilles, x1, y1, x1 - 5 * size / 26, y1 + 5 * size / 13)  # These constants could very well be changed a bit, 
    # but I'm hesitant to assign them randomly
    achilles.goto(x1 - 5 * size / 26, y1 + 10 * size / 13)
    achilles.goto(x1 + size / 10, y1 + size)
    achilles.goto(x1 + 3 * size / 5, y1 + 10 * size / 13)
    achilles.goto(x1 + 4 * size / 5, y1)
    achilles.goto(x1 + 4 * size / 9, y1 + 4 * size / 13)
    achilles.goto(x1, y1)
    achilles.end_fill()
    penguin_eye(achilles, x1 + size / 3, y1 + 8 * size / 13, size / 15)  # Here is the eye
    penguin_beak_left(achilles, x1 + 6 * size / 26, y1 + 8 * size / 13, 6 * size / 13)  # Here is the beak


def penguin_head_right(achilles: Turtle, x1: float, y1: float, size: float) -> None:
    """Making a penguin's head facing right."""
    # The same code, but mirrored.
    changeTurtleColor(achilles, PENGUIN_BLACK)
    achilles.begin_fill()  # Main head shape
    line(achilles, x1, y1, x1 + 5 * size / 26, y1 + 5 * size / 13)  # These constants could very well be changed a bit, 
    # but I'm hesitant to assign them randomly
    achilles.goto(x1 + 5 * size / 26, y1 + 10 * size / 13)
    achilles.goto(x1 - size / 10, y1 + size)
    achilles.goto(x1 - 3 * size / 5, y1 + 10 * size / 13)
    achilles.goto(x1 - 4 * size / 5, y1)
    achilles.goto(x1 - 4 * size / 9, y1 + 4 * size / 13)
    achilles.goto(x1, y1)
    achilles.end_fill()
    penguin_eye(achilles, x1 - size / 3, y1 + 8 * size / 13, size / 15)  # Here is the eye
    penguin_beak_right(achilles, x1 - 6 * size / 26, y1 + 8 * size / 13, 6 * size / 13)


def penguin(achilles: Turtle, x1: float, y1: float, size: float) -> None:
    """Making a full penguin."""
    achilles.begin_fill()  # Main body
    changeTurtleColor(achilles, BLACK)
    line(achilles, x1, y1, x1 - 2 * size / 15, y1)
    achilles.goto(x1 - 2 * size / 15, y1 - size / 40)
    achilles.goto(x1 - size / 6, y1 - size / 40)
    achilles.goto(x1 - size / 5, y1 + size / 4)
    achilles.goto(x1 - size / 5, y1 + 2 * size / 3)
    achilles.goto(x1 - 3 * size / 40, y1 + 5 * size / 6)
    achilles.goto(x1 + 3 * size / 40, y1 + 5 * size / 6)
    achilles.goto(x1 + size / 5, y1 + 2 * size / 3)
    achilles.goto(x1 + size / 5, y1 + size / 4)
    achilles.goto(x1 + size / 6, y1 - size / 40)
    achilles.goto(x1 + 2 * size / 15, y1 - size / 40)
    achilles.goto(x1 + 2 * size / 15, y1)
    achilles.goto(x1, y1)
    changeTurtleColor(achilles, PENGUIN_WHITE)
    achilles.end_fill()
    # Adding the head and the white filling underneath it depending on if the head is facing right or left
    left_or_right_int: int = random.randint(0, 1)
    if left_or_right_int == 0:
        achilles.begin_fill()
        changeTurtleColor(achilles, BLACK)
        line(achilles, x1 - 3 * size / 40, y1 + 5 * size / 6, x1 - 3 * size / 40 - size / 65, y1 + 5 * size / 6 + 5 * size / 78)
        changeTurtleColor(achilles, PENGUIN_WHITE)
        achilles.goto(x1 - 3 * size / 40 - size / 65 + 149 * size / 1404, y1 + 5 * size / 6 + 2 * size / 39)
        achilles.goto(x1 + 3 * size / 40, y1 + 5 * size / 6)
        achilles.goto(x1 - 3 * size / 40, y1 + 5 * size / 6)
        achilles.end_fill()
        penguin_head_left(achilles, x1 - 3 * size / 40 + size / 60, y1 + 5 * size / 6, size / 6)
    else:
        achilles.begin_fill()
        changeTurtleColor(achilles, BLACK)
        line(achilles, x1 + 3 * size / 40, y1 + 5 * size / 6, x1 + 3 * size / 40 + size / 65, y1 + 5 * size / 6 + 5 * size / 78)
        changeTurtleColor(achilles, PENGUIN_WHITE)
        achilles.goto(x1 + 3 * size / 40 + size / 65 - 149 * size / 1404, y1 + 5 * size / 6 + 2 * size / 39)
        achilles.goto(x1 - 3 * size / 40, y1 + 5 * size / 6)
        achilles.goto(x1 + 3 * size / 40, y1 + 5 * size / 6)
        achilles.end_fill()
        penguin_head_right(achilles, x1 + 3 * size / 40 - size / 60, y1 + 5 * size / 6, size / 6)
    idx: int = 0
    while idx < 2:  # Adding the penguin wings with a randomly chosen slant
        wing_slant: float = random.uniform(0, size / 3)
        if idx == 0:
            penguin_wing_left(achilles, x1 - size / 5, y1 + size / 2, size / 10, size / 3 - wing_slant, wing_slant)
        else:
            penguin_wing_right(achilles, x1 + size / 5, y1 + size / 2, size / 10, size / 3 - wing_slant, wing_slant)
        idx += 1


if __name__ == "__main__":
    main()