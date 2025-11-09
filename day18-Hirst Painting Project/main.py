# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("horizontal-blog-images-1-4.jpg", 10)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(223, 155, 90), (214, 240, 228), (240, 206, 90), (104, 170, 203), (36, 109, 149), (199, 227, 239), (113, 193, 161), (153, 61, 94), (208, 78, 109)]

import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.penup()


for turtle in range(10):
    for i in range (10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
        tim.dot(20, random.choice(color_list))

    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.setheading(360)

screen = t.Screen()
screen.exitonclick()
