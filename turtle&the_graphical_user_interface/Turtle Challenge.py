import turtle as t
import random

# turtle = t.Turtle()
# for _ in range(15):
#     t.forward(10)
#     t.penup()
#     t.forward(10)
#     t.pendown()


# turtle = t.Turtle()
# colours = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen"]
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         turtle.forward(100)
#         turtle.right(angle)

# for shape_side in range(3,11):
#     turtle.color(random.choice(colours))
#     draw_shape(shape_side)


# turtle = t.Turtle()
# t.colormode(255)


# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color


# directions = [0, 90, 180, 270]
# turtle.pensize(20)
# turtle.speed("fastest")


# for _ in range(500):
#     turtle.color(random_color())
#     turtle.forward(30)
#     turtle.setheading(random.choice(directions))





turtle = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

turtle.speed("fastest")


def draw_spirograph(size_of_gap):

    for _ in range(int(360 / size_of_gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)

draw_spirograph(5)