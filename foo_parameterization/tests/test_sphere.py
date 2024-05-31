"""
This is a sample of how  a developer can include rigours testing onto multiple commands to the package.
In this case, we are testing the Sphere class from the sphere module.
"""

import unittest
import numpy as np
from foo_parameterization.sphere import Sphere

class TestSphere(unittest.TestCase):

    def test_valid_radius(self):
        sphere = Sphere(5)
        self.assertEqual(sphere.get_radius(), 5)

    def test_set_valid_radius(self):
        sphere = Sphere(1)
        sphere.set_radius(10)
        self.assertEqual(sphere.get_radius(), 10)

    def test_invalid_radius(self):
        with self.assertRaises(ValueError):
            Sphere(-1)

    def test_set_invalid_radius(self):
        sphere = Sphere(1)
        with self.assertRaises(ValueError):
            sphere.set_radius(-5)

    def test_volume_calculation(self):
        sphere = Sphere(3)
        expected_volume = (4.0 / 3.0) * np.pi * (3 ** 3)
        self.assertAlmostEqual(sphere.foo_et_al_parameterization(), expected_volume, places=6)

if __name__ == '__main__':
    unittest.main()