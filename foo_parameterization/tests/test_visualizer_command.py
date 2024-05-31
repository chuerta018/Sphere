"""
This module contains tests for the visualizer command, as an example for future developers. They can also add into it.
"""

import unittest
from unittest.mock import patch
import argparse
import numpy as np
from foo_parameterization.main import main
from foo_parameterization.commands.visualizer import visualize_sphere

class TestVisualizer(unittest.TestCase):

    @patch('foo_parameterization.commands.visualizer.plt.show')
    def test_visualize_sphere(self, mock_show):
        # Ensure no exceptions are raised during visualization
        try:
            visualize_sphere(5)
        except Exception as e:
            self.fail(f"visualize_sphere raised {e.__class__.__name__} unexpectedly!")

    @patch('foo_parameterization.commands.visualizer.plt.show')
    def test_main_without_visualize(self, mock_show):
        with patch('argparse.ArgumentParser.parse_args',
                   return_value=argparse.Namespace(radius=5, visualize=False)):
            volume = main()
            self.assertEqual(volume, (4.0 / 3.0) * np.pi * (5 ** 3))

    @patch('foo_parameterization.commands.visualizer.plt.show')
    def test_main_with_visualize(self, mock_show):
        with patch('argparse.ArgumentParser.parse_args',
                   return_value=argparse.Namespace(radius=5, visualize=True)):
            volume = main()
            self.assertEqual(volume, (4.0 / 3.0) * np.pi * (5 ** 3))

if __name__ == '__main__':
    unittest.main()

