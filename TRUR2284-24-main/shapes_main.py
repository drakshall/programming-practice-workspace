"""A program to print ascii art of geometric shapes.

To run the program, run the following command:
    python shapes_main.py

The program will repeatidle ask the user for a shape
and a size until the user enters 'quit'.

Allowed shapes are:
- square
- empty_square
"""

from shapes import *

if __name__ == '__main__':
    shapes = Shapes()
    while True:
        shape = input("Enter a shape (rectangle) or 'quit': ")
        if shape == 'quit':
            break
        width = int(input("Enter the width: "))
        height = int(input("Enter the height: "))
        x = int(input("Enter the x posn: "))
        y = int(input("Enter the y posn: "))
        if shape == 'rectangle':
            shapes.add_shape('rectangle', width, height, x, y)
            shapes.draw()
        else:
            print("Unknown shape")
