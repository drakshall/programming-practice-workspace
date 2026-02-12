import random

#import ipyturtle3 as turtle
#from ipyturtle3 import hold_canvas
#myCanvas=Turtle.Canvas(width=800,height=800)
#turtle.display(myCanvas)
#myTS=Turtle.TurtleScreen(myCanvas)
#bob=Turtle.turtle()
#myTS=Turtle.getscreen(bob)
#myTS.clear()

# Modified code to work outside Juypter labs
from turtle import Turtle
bob = Turtle()
bob.getscreen().setup(width=600, height=600, startx=0, starty=0)

colours = ["blue","red","magenta","black","yellow"]

start_x = -250
start_y = -250
start_length = 500
bob.speed(0)
bob.penup()
bob.goto(start_x,start_y)
bob.pendown()
def triangle(turtle,start,stop):
    if stop == 0:
        return
    # improve flexibility by not hard coding array size
    colour = colours[random.randint(0,len(colours)-1)]
    turtle.color(colour)

    for x in range(stop):
        for i in range(3):
            turtle.forward(start)
            turtle.left(120)
            triangle(turtle,start/2,stop-1)
        return

triangle(bob,start_length,6)
bob.getscreen().mainloop()
