# Name : Amanjot Singh
# Date : 29 February, 2024
# Description : Creating a program for testing the program that calclulates of shapes.

import unittest
from Lab3 import ShapesAreaCalculator

class TestShapesAreaCalculator(unittest.TestCase):
    def TestCases(self):
        self.calculator = ShapesAreaCalculator()

    def test_area_of_circle(self):
        self.assertAlmostEqual(self.calculator.area_of_circle(2), 12.57, places=2)
        self.assertAlmostEqual(self.calculator.area_of_circle(5), 78.54, places=2)
        self.assertAlmostEqual(self.calculator.area_of_circle(10), 314.16, places=2)

    def test_area_of_trapezium(self):
        self.assertAlmostEqual(self.calculator.area_of_trapezium(5, 3, 2), 8.0, places=2)
        self.assertAlmostEqual(self.calculator.area_of_trapezium(2, 3, 5), 12.5, places=2)

    def test_area_of_ellipse(self):
        self.assertAlmostEqual(self.calculator.area_of_ellipse(3, 5), 47.12, places=2)
        self.assertAlmostEqual(self.calculator.area_of_ellipse(5, 3), 47.12, places=2)


    def test_area_of_rhombus(self):
        self.assertAlmostEqual(self.calculator.area_of_rhombus(3, 4), 6.0, places=2)
        self.assertAlmostEqual(self.calculator.area_of_rhombus(2, 4), 4.0, places=2)
        self.assertAlmostEqual(self.calculator.area_of_rhombus(4, 7), 14, places=2)

if __name__ == "__main__":
    unittest.main()
