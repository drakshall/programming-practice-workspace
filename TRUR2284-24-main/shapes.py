# shapes.py
# Code to generate a set of ASCII art shapes

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

class Screen:
    def __init__(self, width: int, height :int):
        assert width > 0
        assert height > 0
        self.width = width
        self.height = height
        self.cells = [[' ' for _ in range(width)] for _ in range(height)]

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.cells]) + '\n'
    
    def plot(self,x,y):
        if x < self.width and x >= 0 and y < self.height and y >=0:
                    self.cells[y][x] = '*'

    
class Shape:
    def draw_at(self, screen, x, y):
        pass

class Rectangle(Shape):
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def draw(self, screen):
        for i in range(self.width):
            for j in range(self.height):
                screen.plot(self.x + i,self.y + j)
                    
                    
class Shapes:
    """The Shapes class servess as a facade for the whole system.
    It contains a screen and a list of shapes that can be drawn on the screen.
    And provides methods call by the UI to add shapes and draw them on the screen."""

    def __init__(self):
        self.screen = Screen(40, 20)
        self.shapes = []
        self.width = self.screen.width
        self.height = self.screen.height

    def render(self):
        for shape in self.shapes:
            shape.draw(self.screen)

    def draw(self):
        self.render()
        print(self.screen,end="")

    def get_cells(self):
        lines = []
        for row in self.screen.cells:
            lines.append(''.join(row))
        return lines
    
    def add_shape(self, shape_name, w, h, x, y):
        if shape_name == 'rectangle':
            self.shapes.append(Rectangle(w, h, x, y))
        else:
            print("Unknown shape")


# Return a line on n-stars
# return an empty string for n<1

def stars(n):
    if n < 1:
        return ""
    s = ""
    for i in range(0,n):
        s += "*"
    return s