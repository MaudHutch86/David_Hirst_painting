import random
import turtle as turtle_mode
from turtle import Screen

t = turtle_mode.Turtle()

# colors = colorgram.extract('Batik.jpeg', 12)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
turtle_mode.colormode(255)
t.penup()
t.hideturtle()
color_list = [(48, 128, 74), (62, 96, 128), (129, 99, 57), (135, 77, 106), (191, 153, 101), (167, 157, 39),
              (195, 128, 154), (186, 93, 126), (73, 158, 94), (122, 170, 130), (19, 100, 47), (20, 53, 80)]


screen = Screen()
# screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)

t.setheading(225)
t.forward(300)
t.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    color = random.choice(color_list)
    t.dot(20, color)
    t.forward(50)
    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

screen.exitonclick()
