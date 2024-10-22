import turtle
import random
import math

# Setup the turtle window
window = turtle.Screen()
window.setup(width=600, height=600)
window.setworldcoordinates(-1.5, -1.5, 1.5, 1.5)

# Create a turtle for drawing the axes and labels
axes = turtle.Turtle()
axes.speed(0)
axes.hideturtle()

# Draw X and Y axes
axes.penup()
axes.goto(-1.5, 0)
axes.pendown()
axes.goto(1.5, 0)

axes.penup()
axes.goto(0, -1.5)
axes.pendown()
axes.goto(0, 1.5)

# Function to draw points at specified coordinates
def draw_axis_points():
    points = [-1, 0, 1]
    for x in points:
        axes.penup()
        axes.goto(x, -0.00)  # Position slightly below the axis
        axes.dot(5, "black")  # Draw point on X-axis
        axes.goto(-0.00, x)  # Position slightly left of the axis
        axes.dot(5, "black")  # Draw point on Y-axis

# Draw points on -1, 0, 1 for both axes
draw_axis_points()

# Add labels for X and Y axes at -1, 0, 1
axes.penup()
axes.goto(1, -0.0)  # Adjust position for label visibility
axes.write("1", align="center", font=("Arial", 12, "normal"))

axes.goto(-1, -0.0)  # X = -1 label
axes.write("-1", align="center", font=("Arial", 12, "normal"))

axes.goto(0.1, -0.0)  # X = 0 label (at the origin)
axes.write("0", align="center", font=("Arial", 12, "normal"))

axes.goto(0.0, 1)  # Y = 1 label
axes.write("1", align="center", font=("Arial", 12, "normal"))

axes.goto(0.0, -1)  # Y = -1 label
axes.write("-1", align="center", font=("Arial", 12, "normal"))

# Write axis labels
axes.penup()
axes.goto(1.6, 0)  # Position for 'x' label
axes.write("x", align="center", font=("Arial", 12, "normal"))

axes.goto(0.0, 1.6)  # Position for 'y' label
axes.write("y", align="center", font=("Arial", 12, "normal"))

# Initialize the turtle for drawing points
drawer = turtle.Turtle()
drawer.speed(0)
drawer.penup()

# Function to draw a point at (x, y) with a specific color
def draw_point(x, y, color):
    drawer.goto(x, y)
    drawer.dot(3, color)  # Dot size set to 3 for better visibility

# Monte Carlo simulation and visualization
def visualize_monte_carlo(n):
    counter = 0
    for _ in range(n):
        a = random.uniform(-1, 1)  # Generate 'a' from -1 to 1
        b = random.uniform(-1, 1)  # Generate 'b' from -1 to 1
        distance = math.sqrt(a ** 2 + b ** 2)

        if distance <= 1:
            draw_point(a, b, "red")   # Inside the circle -> red
            counter += 1
        else:
            draw_point(a, b, "green") # Outside the circle -> green

# Run the visualization
n = int(input("Please enter the number of points to generate: "))
visualize_monte_carlo(n)

# Keep the window open
turtle.done()
