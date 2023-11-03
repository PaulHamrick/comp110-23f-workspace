from turtle import Screen, Turtle, colormode, done
screen = Screen()
colormode(255)

leo: Turtle = Turtle()

leo.penup()
leo.goto(-150,-120)
screen.screensize(400, 400)
leo.pendown()
snow: list[int] = [211, 223, 249]
darker_snow: list[int] = [200, 212, 238]
leo.color(darker_snow)
leo.speed(10)

leo.begin_fill()

i: int = 0

while (i < 3):
    leo.forward(-100)
    leo.left(120)
    i = i + 1

leo.end_fill()
leo.goto(400,0)
leo.hideturtle()


done()