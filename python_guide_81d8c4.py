# Learning Objective:
# This tutorial will teach you how to visualize and explore fractal patterns
# using recursion and Python's Turtle graphics. We will focus on understanding
# how a simple recursive function can create complex and beautiful geometric shapes.
# By the end, you'll be able to:
# - Understand the concept of recursion.
# - Implement a basic recursive function in Python.
# - Use the Turtle module to draw geometric patterns.
# - Generate and modify a classic fractal: the Sierpinski Triangle.

import turtle

# --- Configuration ---
# Define screen dimensions for the Turtle graphics window.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700

# Define drawing speed. 0 is fastest, 1 is slowest, 10 is fast.
# We'll use a moderate speed for clear visualization.
DRAWING_SPEED = 6

# Define initial colors for the fractal.
# You can experiment with different color palettes!
PRIMARY_COLOR = "blue"
SECONDARY_COLOR = "red"
TERTIARY_COLOR = "green"
BACKGROUND_COLOR = "white"

# --- Fractal Generation Function ---

def draw_sierpinski(t, order, size):
    """
    Recursively draws the Sierpinski Triangle.

    Args:
        t (turtle.Turtle): The turtle object to draw with.
        order (int): The current depth of recursion. This determines
                     the complexity of the fractal.
        size (int): The length of the base of the current triangle.
    """
    # Base case of the recursion:
    # If the order is 0, we draw a single filled triangle.
    # This is the smallest unit of our fractal.
    if order == 0:
        t.begin_fill()
        for _ in range(3): # A triangle has 3 sides
            t.forward(size)
            t.left(120) # Turn left by 120 degrees for each corner
        t.end_fill()
        return # Stop recursion for this branch

    # Recursive step:
    # If the order is greater than 0, we divide the current triangle
    # into three smaller triangles and recursively call the function
    # for each of them.
    else:
        # Each smaller triangle will have half the size of the current one.
        half_size = size / 2

        # Draw the bottom-left triangle
        draw_sierpinski(t, order - 1, half_size)

        # Move the turtle to the starting position for the bottom-right triangle.
        # We move forward by half_size to position it to the right of the first.
        t.forward(half_size)
        draw_sierpinski(t, order - 1, half_size)

        # Move the turtle to the starting position for the top triangle.
        # First, move back to the center of the base of the original triangle.
        t.backward(half_size)
        # Then, move left by half_size and forward by half_size (effectively
        # moving up and left to the apex of the original triangle's base).
        t.left(60) # Turn to face upwards
        t.forward(half_size)
        t.right(60) # Turn back to the original orientation
        draw_sierpinski(t, order - 1, half_size)

        # After drawing the top triangle, we need to reposition the turtle
        # back to the original starting point of the current `draw_sierpinski` call
        # so that the parent recursive calls can continue drawing correctly.
        t.left(60) # Turn back down
        t.backward(half_size)
        t.right(60) # Turn back to original orientation for moving right

# --- Setup and Drawing ---

def setup_screen():
    """Sets up the Turtle graphics screen."""
    screen = turtle.Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor(BACKGROUND_COLOR)
    screen.title("Sierpinski Triangle Fractal Explorer")
    return screen

def setup_turtle():
    """Sets up the Turtle object for drawing."""
    t = turtle.Turtle()
    t.speed(DRAWING_SPEED)  # Set the drawing speed
    t.penup()               # Don't draw lines when moving initially
    t.hideturtle()          # Hide the turtle icon while drawing for a cleaner look
    return t

def main():
    """Main function to set up and draw the Sierpinski Triangle."""
    screen = setup_screen()
    t = setup_turtle()

    # Define the initial parameters for the fractal.
    # 'fractal_order' controls the complexity (higher is more complex).
    # 'initial_size' determines the overall size of the fractal.
    fractal_order = 4 # You can change this to see different levels of detail
    initial_size = 300 # You can change this to scale the fractal

    # Calculate the starting position to center the fractal on the screen.
    # We want to start drawing from the bottom-left corner of the bounding box.
    start_x = -initial_size / 2
    start_y = -initial_size * (3**0.5) / 4 # Approximate height adjustment for centering

    # Move the turtle to the starting position.
    t.goto(start_x, start_y)
    t.pendown() # Put the pen down to start drawing

    # Set the fill color for the initial triangle.
    t.fillcolor(PRIMARY_COLOR)
    t.pencolor(PRIMARY_COLOR)

    # Start the recursive drawing process.
    print(f"Drawing Sierpinski Triangle with order {fractal_order} and size {initial_size}...")
    draw_sierpinski(t, fractal_order, initial_size)
    print("Drawing complete!")

    # Keep the window open until it's manually closed.
    screen.mainloop()

# --- Example Usage ---
if __name__ == "__main__":
    # This block ensures that main() is called only when the script is executed directly,
    # not when imported as a module.
    main()