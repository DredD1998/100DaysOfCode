# import colorgram
import turtle as t
import random

# rgb_colors = []
# colors = colorgram.extract("The Hirst Painting Project/image.jpg",30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)


t.colormode(255)
turtle = t.Turtle()
turtle.penup()
turtle.hideturtle()
color_list = [(138, 78, 52), (49, 26, 23), (41, 78, 183), (226, 237, 248), (196, 158, 118), (80, 234, 202), (66, 200, 226), (237, 169, 164), (240, 16, 16), (174, 178, 231), (224, 19, 119), (27, 40, 156), (81, 80, 213), (238, 227, 5), (248, 236, 31), (63, 233, 242), (222, 248, 240), (225, 138, 205), (238, 156, 218), (19, 150, 23), (222, 78, 50), (11, 226, 238), (6, 245, 223), (10, 79, 111), (239, 41, 154), (249, 223, 239), (18, 20, 44), (39, 213, 68), (195, 15, 11)]

turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
number_of_dots = 110
for i in range(1,number_of_dots+1):
    turtle.dot(20,random.choice(color_list))
    turtle.forward(50)

    if i % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)

