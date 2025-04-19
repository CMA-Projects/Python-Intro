import turtle

# Set up screen
screen = turtle.Screen()
screen.bgcolor("white")

# Set up turtle
t = turtle.Turtle()
t.color("forest green")
t.speed(0)
t.left(90)  # Point upwards
t.penup()
t.goto(0, -250)  # Start at the bottom center
t.pendown()

# Recursive tree function
def draw_tree(branch_length, t):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_tree(branch_length - 15, t)
        t.left(40)
        draw_tree(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)

# Draw the tree
draw_tree(100, t)

# Done
t.hideturtle()
turtle.done()
