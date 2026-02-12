import random

class Triangle:
    def __init__(self, edge_length, start_x, start_y, depth, colourgen):

        self.edge_length = edge_length
        self.start_x = start_x
        self.start_y = start_y
        self.depth = depth
        self.colourgen = colourgen
    
    def __triangle(self, turtle, length, depth):
        if depth == 0:
            return
        # improve flexibility by not hard coding array size
        turtle.color(self.colourgen.next())

        for x in range(depth):
            for i in range(3):
                turtle.forward(length)
                turtle.left(120)
                self.__triangle(turtle,length/2,depth-1)
            return
        
    def draw(self, turtle):
        turtle.speed(0)
        turtle.penup()
        turtle.goto(self.start_x,self.start_y)
        turtle.pendown()
        self.__triangle(turtle,self.edge_length,self.depth)

class ColourGenerator:
    
    def next(self) -> str:
        pass

class SingleColourGenerator(ColourGenerator):
    def __init__(self, colour):
        self.colour = colour

    def next(self) -> str:
        return self.colour
    
class SequenceColourGenerator(ColourGenerator):
    def __init__(self, colours):
        self.colours = colours
        self.index = 0

    def next(self) -> str:
        colour = self.colours[self.index]
        self.index = (self.index + 1) % len(self.colours)
        return colour
    
class RandomColourGenerator(ColourGenerator):
    def __init__(self, colours):
        self.colours = colours

    def next(self) -> str:
        return random.choice(self.colours)