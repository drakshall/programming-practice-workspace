import time

class Worker:
    def __init__(self, timeRemaining, productivity, nutrition):
        self.timeRemaining = timeRemaining
        self.productivity = productivity
        self.nutrition = nutrition


testSubject = Worker(600,5,20)

while True:
    