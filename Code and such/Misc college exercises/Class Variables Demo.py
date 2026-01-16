class Point:
    x = 0
    y = 0
    message = "This is a point"

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.test = 99

p1 = Point(20, 30)


print (Point.message)
print (p1.x, ",", p1.y)
print ("now changing some vars...")
p1.message = "this is now an object specific message, look the original is still there if i call it"
print (p1.message)
print (Point.message)