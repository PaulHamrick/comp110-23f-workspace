import turtle
import random
t = turtle()

screenSize = t.screensize() #returns (width, height)

# Main code
while True:
    ranPts = randint(2, 5) * 2 + 1
    ranSize = randint(10, 50)
    ranCol = (random(), random(), random())
    ranX = randint(50-screenSize[0], screenSize[0] - 100)
    ranY = randint(50-screenSize[1], screenSize[1] - 100)
    draw_star(ranPts, ranSize, ranCol, ranX, ranY)