import turtle
import colorsys

# Setup
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)  # Fastest
t.width(2)
t.hideturtle()

# Settings
num_circles = 100
hue = 0
radius = 150

# Use HSL colors for smooth gradients
for i in range(num_circles):
    t.color(colorsys.hsv_to_rgb(hue, 1, 1))  # RGB from HSV
    t.circle(radius)
    t.left(360 / num_circles)
    hue += 1 / num_circles

turtle.done()
