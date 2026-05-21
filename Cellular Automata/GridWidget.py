# gridwidget.py
import numpy as np
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.clock import Clock
from PetriDish import applyRule

class GridWidget(Widget):
    def __init__(self, rows=80, cols=80, cellSize=10, **kwargs):
        super().__init__(**kwargs)
        self.rows = rows
        self.cols = cols
        self.cellSize = cellSize
        self.grid = np.random.choice([0, 1], size=(rows, cols), p=[0.5, 0.5])
        self.running = False
        self.ruleName = "Class 4"
        self.bind(pos=self.redraw, size=self.redraw)
        Clock.schedule_once(self.redraw, 0)

    def redraw(self, *args):
        self.canvas.clear()
        with self.canvas:
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.grid[i, j] == 1:
                        Color(1, 1, 1, 1)
                    else:
                        Color(0, 0, 0, 1)
                    x = self.x + j * self.cellSize
                    y = self.y + self.rows * self.cellSize - (i+1) * self.cellSize
                    Rectangle(pos=(x, y), size=(self.cellSize, self.cellSize))

    def _computeNext(self):
        self.grid = applyRule(self.grid, self.ruleName)
        self.redraw()

    def updateGeneration(self, dt=None):
        if not self.running:
            return
        self._computeNext()

    def startSimulation(self):
        self.running = True
        Clock.schedule_interval(self.updateGeneration, 1.0 / 10.0)

    def stopSimulation(self):
        self.running = False
        Clock.unschedule(self.updateGeneration)

    def step(self):
        self._computeNext()

    def randomize(self):
        self.grid = np.random.choice([0, 1], size=(self.rows, self.cols), p=[0.5, 0.5])
        self.redraw()

    def setRule(self, ruleName):
        self.ruleName = ruleName
        self.randomize()