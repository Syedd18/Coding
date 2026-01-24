# Learning Objective:
# This tutorial will teach you how to visually tell a simple story using data
# and basic charts in Python. We'll focus on using the `matplotlib` library
# to create a bar chart that represents the growth of something over time.
# This will help you understand how to present data in an understandable and
# engaging way.

# First, we need to import the necessary library.
# `matplotlib.pyplot` is a collection of functions that make matplotlib work like MATLAB.
# It's commonly imported with the alias `plt` for brevity.
import matplotlib.pyplot as plt

# Let's define some data that will tell our story.
# Imagine this data represents the number of users joining a new app each month.
# We have two lists: one for the months (our x-axis) and one for the number of users (our y-axis).
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
users = [100, 150, 220, 300, 400, 550, 700, 850, 1000, 1200, 1400, 1600]

# Now, let's create our chart.
# `plt.figure()` creates a new figure, which is like a blank canvas for our plot.
# We can optionally specify `figsize` to control the size of the figure in inches.
plt.figure(figsize=(10, 6))

# `plt.bar()` is the function to create a bar chart.
# The first argument is the x-coordinates of the bars (our months).
# The second argument is the height of the bars (our user counts).
plt.bar(months, users, color='skyblue')

# We need to add labels to our chart to make it understandable.
# `plt.xlabel()` sets the label for the x-axis.
plt.xlabel("Month")
# `plt.ylabel()` sets the label for the y-axis.
plt.ylabel("Number of New Users")

# A title helps explain what the chart is all about.
# `plt.title()` sets the title of the chart.
plt.title("Monthly App User Growth Over a Year")

# To make the x-axis labels (months) easier to read if they overlap,
# we can rotate them.
plt.xticks(rotation=45, ha='right') # 'ha' means horizontal alignment

# `plt.tight_layout()` automatically adjusts plot parameters for a tight layout,
# preventing labels from overlapping.
plt.tight_layout()

# Finally, `plt.show()` displays the plot.
# This function is essential to render the chart on your screen.
# plt.show() # Uncomment this line to display the plot when running the script.

# --- Example Usage ---
# To see the story this data tells, uncomment the `plt.show()` line
# at the end of the script and run this Python file.
# You will see a bar chart showing a steady increase in app users
# throughout the year, visually representing growth.

# You can experiment by changing the `users` list to represent different scenarios,
# like a product launch with initial high growth followed by a plateau,
# or a seasonal product with peaks and dips.

# For instance, try changing 'users' to:
# users_fluctuating = [100, 120, 110, 150, 180, 160, 200, 230, 210, 250, 240, 260]
# and then re-run the script (after changing the `plt.title()` to reflect the new data).

# This simple example demonstrates how bar charts can effectively
# visualize trends and communicate stories hidden within data.
# The journey from raw numbers to a visual representation is a key skill in data analysis.