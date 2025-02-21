# from turtle import Turtle, Screen
# import random
# timmy = Turtle()
# screen = Screen()
# timmy.shape('turtle')
# timmy.color('black')
# direction = [0, 90, 180, 270]
#
#
# # timmy.pensize(5)
# timmy.speed('fastest')
# heading = 0
# def spirograph(gap_size):
#     for i in range(int(round(360/gap_size))):
#         timmy.color(random.random(), random.random(), random.random())
#         timmy.circle(100)
#         timmy.setheading(timmy.heading() + gap_size)
# def hirst():
#
# spirograph(10)
# screen.exitonclick()
# import colorgram
# colors = colorgram.extract("DAMIEN-HIRST-Zirconyl-Chloride-2008-Household-gloss-on-canvas-84-inches-diameter-e1328195059823.jpg", 30)
# coloring = []
# for color in colors:
#     coloring.append((color.rgb[0], color.rgb[1], color.rgb[2]))
# print(coloring)
from turtle import Turtle, Screen, colormode
import random
new_colors = [(208, 158, 96), (234, 213, 101), (41, 104, 144), (149, 78, 57), (130, 168, 194), (202, 137, 162), (148, 65, 83), (24, 40, 55), (204, 90, 68), (169, 159, 55), (139, 180, 152), (193, 89, 121), (59, 117, 93), (26, 44, 36), (223, 171, 187), (63, 46, 34), (91, 154, 104), (44, 161, 182), (237, 212, 7), (226, 175, 167), (13, 96, 75), (41, 59, 99), (179, 189, 213), (99, 125, 168), (65, 33, 43), (104, 43, 59)]
timmy = Turtle()
screen = Screen()
colormode(255)
timmy.speed('fastest')
def make_dots(size, distance):
    for _ in range(distance):
        timmy.color(random.choice(new_colors))
        timmy.dot(size)
        timmy.forward(50)

y_in = -150
for i in range(10):
    timmy.penup()
    timmy.setpos(-150, y_in)
    make_dots(15, 10)
    y_in += 50

screen.exitonclick()