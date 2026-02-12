from turtle import Turtle
from Triangle import *

bob = Turtle()
bob.getscreen().setup(width=600, height=600, startx=0, starty=0)

colours = ["blue","red","magenta","black","yellow"]

Triangle(100, -250, 150, 2, SequenceColourGenerator(["pink","green"])).draw(bob)


tri = Triangle(250, 0, 0, 4, RandomColourGenerator(colours))
tri.draw(bob)
bob.left(90)
tri.draw(bob)
bob.left(90)
tri.draw(bob)
bob.left(90)
tri.draw(bob)
bob.left(90)

tri2 = Triangle(250, -250, -250, 1, SingleColourGenerator("green"))
tri2.draw(bob)


bob.getscreen().mainloop()