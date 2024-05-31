import matplotlib.pyplot as plt
import numpy as np
"""
This is a sample of how  a developer can include multiple commands to the package. 
Here is a visualizer command that will plot a sphere with a given radius.

To run this command, you can use the following command: --visualize

Example: foo-parameterization 50 --visualize
"""

def visualize_sphere(radius):
    fig = plt.figure()
    # Render a 3D surface plot
    ax = fig.add_subplot(projection='3d')

    # Create the angles around Z and from north and south poles
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)

    # Calculate X Y Z Cords using radius given.
    x = radius * np.outer(np.cos(u), np.sin(v))
    y = radius * np.outer(np.sin(u), np.sin(v))
    z = radius * np.outer(np.ones(np.size(u)), np.cos(v))

    # Plot the surface
    ax.plot_surface(x, y, z)

    # Set an equal aspect ratio
    ax.set_aspect('auto')

    plt.show()
    # References: https://matplotlib.org/stable/gallery/mplot3d/surface3d_2.html#sphx-glr-gallery-mplot3d-surface3d-2-py