"""Testing a screen class with TDD.

List of tests:
- A Screen class can be created with a specified width and height. 
- The screen is initialized with a blank screen (all cells are spaces). 
- The Shape class has a single method `draw_at(screen, x, y)` that draws the shape on the screen at the specified position.
- The default implementation of `draw_at` in the Shape class does nothing.
- The Rectangle class is a subclass of Shape and has a constructor that takes a width and height.
- The Rectangle class implements the draw_at method by drawing a rectangle of stars on the screen.
- When the cells to be drawn are outside the screen, the draw_at method should not draw them.
- A Shapes class can be created that contains a Screen and a list of shapes.
- The Shapes class has a method `draw()` that draws all shapes on the screen.
- The Shapes class has a method `add_shape(shape_name,size,x,y)` that creates a shape 
"""

import unittest
from shapes import *

class TestScreen(unittest.TestCase):
    def test_create_screen(self):
        screen = Screen(5, 4)
        self.assertEqual(screen.width, 5)
        self.assertEqual(screen.height, 4)
        self.assertEqual(str(screen), (" " * 5 + "\n") * 4)

    
