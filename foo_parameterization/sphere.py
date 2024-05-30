import math


class Sphere:

    def __init__(self, radius):
        self.radius = None
        self.set_radius(radius)  # Use the setter to validate radius

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive.")
        self.radius = radius
    
    def foo_et_al_parameterization(self):
        return 4 / 3 * math.pi * self.radius ** 3
