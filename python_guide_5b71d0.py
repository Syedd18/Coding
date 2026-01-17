# Fractal Generation Tutorial: Exploring Recursion with the Sierpinski Triangle

# Learning Objective:
# This tutorial will guide you through generating a beautiful fractal pattern,
# the Sierpinski Triangle, using Python. You will learn how recursion works
# by observing how a complex shape is built from simple, repeating rules.
# We will also touch upon basic graphical rendering to visualize the fractal.

# --- Key Concepts: ---
# 1. Recursion: A function that calls itself. Think of it as breaking down
#    a big problem into smaller, identical sub-problems.
# 2. Base Case: The condition that stops a recursive function from calling
#    itself indefinitely. Without it, you get an infinite loop (or a crash!).
# 3. Graphical Rendering: Drawing shapes on a screen. We'll use the `turtle`
#    module for this, which is great for beginners as it mimics drawing with a pen.

import turtle

# --- 1. Setting up the Turtle Graphics Environment ---

# Create a screen object to control our drawing window.
screen = turtle.Screen()
# Set the background color of the screen.
screen.bgcolor("white")
# Set the title of the window.
screen.title("Sierpinski Triangle Fractal")

# Create a turtle object, which is our "pen" to draw with.
pen = turtle.Turtle()
# Make the turtle draw faster by turning off screen updates during drawing.
# We'll update the screen manually at the end.
screen.tracer(0)
# Hide the turtle icon itself so it doesn't clutter the drawing.
pen.hideturtle()
# Set the drawing speed to the fastest.
pen.speed(0)
# Set the color of the pen.
pen.pencolor("blue")
# Set the initial position of the turtle. This is the bottom-left corner
# of our triangle. We offset it slightly to center the fractal.
pen.penup() # Lift the pen so it doesn't draw while moving to the start.
pen.goto(-200, -150)
pen.pendown() # Put the pen down to start drawing.

# --- 2. The Recursive Function: `sierpinski` ---

def sierpinski(length, level):
    """
    Recursively draws the Sierpinski Triangle.

    Args:
        length (int): The length of the side of the current triangle.
        level (int): The current recursion depth. This determines how many
                     times we subdivide the triangle.
    """
    # --- The Base Case: When to stop recursing ---
    # If the level is 0, we've reached the smallest triangle we want to draw.
    # In this case, we just draw a single filled triangle.
    if level == 0:
        # Begin filling the shape with color.
        pen.begin_fill()
        # Draw a triangle by moving forward and turning.
        for _ in range(3):
            pen.forward(length)
            pen.left(120) # Turn left 120 degrees for a triangle.
        # Stop filling the shape.
        pen.end_fill()
        # Return to prevent further recursive calls for this branch.
        return

    # --- The Recursive Step: Breaking down the problem ---
    # If level > 0, we need to subdivide the current triangle into smaller ones.
    # We do this by drawing three smaller Sierpinski triangles at the corners
    # of the current triangle.

    # 1. Draw the bottom-left smaller Sierpinski triangle.
    #    It has half the length and one level less.
    sierpinski(length / 2, level - 1)

    # 2. Move the pen to the position for the bottom-right smaller triangle.
    #    We move forward by 'length / 2' and then to the right.
    pen.forward(length / 2)
    sierpinski(length / 2, level - 1)

    # 3. Move the pen to the position for the top smaller triangle.
    #    We need to move back, turn, and move again to reach the starting
    #    point of the top triangle.
    pen.backward(length / 2) # Move back to the center of the base.
    pen.left(60)             # Turn 60 degrees to face the top corner.
    pen.forward(length / 2)  # Move to the starting point of the top triangle.
    sierpinski(length / 2, level - 1)

    # 4. Return the pen to its original position and orientation for this level.
    #    This is crucial for the next step in the parent recursive call.
    pen.right(60)            # Turn back 60 degrees.
    pen.backward(length / 2) # Move back to the starting point of this triangle.

# --- 3. Example Usage ---

# Define the size of the initial triangle (the base length).
initial_length = 400
# Define the recursion level (how many times to subdivide).
# Higher levels create more detail but take longer to draw.
recursion_level = 4

# Set the fill color for the triangles.
pen.fillcolor("red")

# Call the sierpinski function to start drawing the fractal.
# This is the initial call that kicks off the recursion.
sierpinski(initial_length, recursion_level)

# --- 4. Finalizing the Display ---

# Update the screen to show everything that has been drawn.
screen.update()

# Keep the window open until it's manually closed.
screen.mainloop()

# --- How to Learn More: ---
# 1. Change `initial_length` and `recursion_level` to see how they affect the output.
# 2. Experiment with different `pencolor` and `fillcolor` values.
# 3. Try drawing other fractals! The Koch snowflake is another good one to explore
#    with recursion. You'll need to adapt the movement and turning logic.
# 4. Think about other recursive problems: calculating factorials, traversing
#    tree structures, or even searching algorithms.
# 5. To understand the "why" of the movements in the recursive step:
#    Trace the pen's path for `level = 1` and then `level = 2` mentally or on paper.
#    This will solidify how the sub-triangles are positioned correctly.