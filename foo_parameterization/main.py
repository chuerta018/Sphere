""" 
Users can import commands as shown with the visualizer into the software package.

"""

import argparse
from foo_parameterization.sphere import Sphere
from foo_parameterization.commands import visualize_sphere

def parse_arguments():
    parser = argparse.ArgumentParser(description='Calculate the volume of a sphere and optionally visualize it.')
    parser.add_argument('radius', type=float, help='Radius of the sphere')
    parser.add_argument('--visualize', action='store_true', help='Show the 3D visualization of the sphere')
    return parser.parse_args()

def main():
    args = parse_arguments()
    radius = args.radius
    visualize = args.visualize

    try:
        my_sphere = Sphere(radius)
        volume = my_sphere.foo_et_al_parameterization()
        print(f"The volume of the sphere is: {volume}")

        if visualize:
            visualize_sphere(radius)

        return volume

    except ValueError as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    main()
