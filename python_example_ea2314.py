# Gravitational Dance of Planets Simulation Tutorial

# Learning Objective:
# This tutorial demonstrates how to simulate and visualize the
# gravitational interaction between celestial bodies using Python.
# We will focus on the fundamental concept of Newton's Law of
# Universal Gravitation and how to numerically integrate motion
# over time to observe orbital mechanics.

# Import necessary libraries
import numpy as np  # For numerical operations, especially arrays
import matplotlib.pyplot as plt  # For plotting and visualization
import matplotlib.animation as animation # For creating animations

# --- Constants ---
G = 6.67430e-11  # Gravitational constant (N * m^2 / kg^2)
# We use a scaled-down value for G for visualization purposes
# to make the simulation visually intuitive without extremely large numbers.
# In a real astrophysical simulation, you'd use the actual value.
G_VIS = 1e1  # Visual scaling factor for gravitational force

# --- Simulation Parameters ---
dt = 1.0  # Time step (in arbitrary units, e.g., days)
total_time = 365 * 5  # Total simulation time (e.g., 5 years)
num_steps = int(total_time / dt)  # Number of simulation steps

# --- Celestial Body Class ---
# This class represents a celestial body (planet, star, etc.)
# and stores its physical properties and state.
class CelestialBody:
    def __init__(self, name, mass, position, velocity, color):
        self.name = name
        self.mass = mass  # Mass of the body
        self.position = np.array(position, dtype=float)  # [x, y] coordinates
        self.velocity = np.array(velocity, dtype=float)  # [vx, vy] velocity components
        self.color = color # For visualization

    def update_position(self, acceleration, dt):
        # Update velocity based on acceleration
        # v(t+dt) = v(t) + a(t) * dt
        self.velocity += acceleration * dt
        # Update position based on new velocity
        # r(t+dt) = r(t) + v(t+dt) * dt
        self.position += self.velocity * dt

# --- Physics Functions ---

def calculate_gravitational_force(body1, body2):
    # Calculate the vector pointing from body1 to body2
    r_vec = body2.position - body1.position
    # Calculate the distance between the two bodies
    r_mag = np.linalg.norm(r_vec)

    # Avoid division by zero if bodies are at the same position
    if r_mag == 0:
        return np.array([0.0, 0.0])

    # Calculate the unit vector pointing from body1 to body2
    r_hat = r_vec / r_mag

    # Calculate the magnitude of the gravitational force using Newton's Law:
    # F = G * (m1 * m2) / r^2
    force_magnitude = G_VIS * (body1.mass * body2.mass) / (r_mag**2)

    # Calculate the force vector
    force_vec = force_magnitude * r_hat
    return force_vec

def calculate_net_force_and_acceleration(body, all_bodies):
    # Initialize net force vector to zero
    net_force = np.array([0.0, 0.0])

    # Iterate through all other bodies to sum up gravitational forces
    for other_body in all_bodies:
        # A body does not exert a force on itself
        if body != other_body:
            # Calculate the force exerted by other_body on 'body'
            # F_on_body_by_other = G * (m_body * m_other) / r^2 * r_hat
            # Note: Newton's third law states F_on_body_by_other = -F_on_other_by_body
            # So we calculate the force of 'other_body' on 'body'.
            force_on_body = calculate_gravitational_force(other_body, body)
            net_force += force_on_body

    # Calculate acceleration using Newton's second law: F = m*a => a = F/m
    acceleration = net_force / body.mass
    return acceleration

# --- Simulation Setup ---

# Define the celestial bodies for our simulation
# Example: A sun and a planet
sun = CelestialBody(name="Sun", mass=1.989e30, position=[0, 0], velocity=[0, 0], color='yellow')
earth = CelestialBody(name="Earth", mass=5.972e24, position=[1.496e11, 0], velocity=[0, 2.978e4], color='blue')
mars = CelestialBody(name="Mars", mass=6.417e23, position=[2.279e11, 0], velocity=[0, 2.407e4], color='red')

# Store all bodies in a list for easy iteration
all_bodies = [sun, earth, mars]

# Store historical positions for plotting
history = {body.name: [] for body in all_bodies}

# --- Simulation Loop ---

print("Starting simulation...")
for step in range(num_steps):
    # Store current positions for visualization
    for body in all_bodies:
        history[body.name].append(body.position.copy()) # .copy() is important!

    # Calculate accelerations for all bodies based on current positions
    accelerations = {}
    for body in all_bodies:
        accelerations[body.name] = calculate_net_force_and_acceleration(body, all_bodies)

    # Update positions and velocities for all bodies
    for body in all_bodies:
        body.update_position(accelerations[body.name], dt)

    # Optional: Print progress
    if step % (num_steps // 10) == 0:
        print(f"Progress: {step/num_steps*100:.0f}%")

print("Simulation finished.")

# --- Visualization ---

# Convert history lists to numpy arrays for easier plotting
for body_name in history:
    history[body_name] = np.array(history[body_name])

# Setup the plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor('black') # Black background for space
ax.set_aspect('equal', adjustable='box') # Ensure aspect ratio is equal

# Set plot limits based on the extent of the orbits
max_range = 0
for body_name in history:
    max_range = max(max_range, np.max(np.abs(history[body_name])))
ax.set_xlim(-max_range * 1.2, max_range * 1.2)
ax.set_ylim(-max_range * 1.2, max_range * 1.2)

ax.set_title("Planetary Orbits Simulation")
ax.set_xlabel("X Position (arbitrary units)")
ax.set_ylabel("Y Position (arbitrary units)")

# Plot the initial positions of the bodies
scatter_plots = {}
for body in all_bodies:
    scatter_plots[body.name] = ax.scatter(history[body.name][0, 0], history[body.name][0, 1], color=body.color, label=body.name, s=body.mass/1e26) # Size proportional to mass
    ax.plot(history[body.name][:, 0], history[body.name][:, 1], color=body.color, linestyle='--', alpha=0.5) # Plot orbits as dashed lines

ax.legend()

# Animation function to update the plot at each time step
def update(frame):
    for body in all_bodies:
        # Update the position of the scatter plot for each body
        scatter_plots[body.name].set_offsets(history[body.name][frame])
    return list(scatter_plots.values())

# Create the animation
# interval: Delay between frames in milliseconds
# blit: Optimizes drawing by only redrawing the parts that have changed
ani = animation.FuncAnimation(fig, update, frames=num_steps, interval=20, blit=True)

plt.show()

# --- Example Usage ---
# The example usage is the setup of bodies and the simulation loop above.
# You can modify the initial positions, velocities, masses, and simulation
# parameters (dt, total_time) to observe different orbital behaviors.
#
# For instance, to see a binary star system:
# star1 = CelestialBody(name="Star1", mass=2e30, position=[-1e10, 0], velocity=[0, 1e4], color='orange')
# star2 = CelestialBody(name="Star2", mass=2e30, position=[1e10, 0], velocity=[0, -1e4], color='red')
# all_bodies = [star1, star2]
# ... and then run the simulation and visualization parts.