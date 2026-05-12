class ShapeType:

    def __init__(self, bodyColour = "white", outlineColour = "black", outlineType = "solid"):
        self.bodyColour = bodyColour
        self.outlineColour = outlineColour
        self.outlineType = outlineType

class CircleShapeType(ShapeType):

    def __init__(self, name,):
            super().__init__()
            self.name = "circle"


    def RenderCircle(self):
         pass #pyturtleinstructions

class SquareShapeType(ShapeType):

class TriangleShapeType(ShapeType):
     
class ShapeInstance

class ShapeFactory:
    def __init__(self):
        self.types = {
            'c' : CircleShapeType(),
            's' : SquareShapeType(),
            't' : TriangleShapeType(),
        }

    def ConstructInstance(self, )