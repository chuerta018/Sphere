import argparse
import matplotlib.pyplot as plt
import numpy as np
from .sphere import Sphere


def parse_arguments():
    parser = argparse.ArgumentParser(description='Plot a sphere and print the volume with a given radius.')
    parser.add_argument('radius', type=float, help='Radius of the sphere')
    return parser.parse_args()


def main():
    args = parse_arguments()
    radius = args.radius

    try:

        my_sphere = Sphere(radius)
        volume = my_sphere.foo_et_al_parameterization()
        print(f"The volume of the sphere is: {volume}")

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

    except ValueError as e:
        print(f"Error: {e}")
    # References: https://matplotlib.org/stable/gallery/mplot3d/surface3d_2.html#sphx-glr-gallery-mplot3d-surface3d-2-py


if __name__ == '__main__':
    main()
