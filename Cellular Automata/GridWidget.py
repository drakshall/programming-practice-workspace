# Defines the custom Kivy widget that draws the grid and controls the simulation.

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
# Controls size of grid in number of cells.
        self.cellSize = cellSize
# Controls visual size of cells in pixels.
        self.grid = np.random.choice([0, 1], size=(rows, cols), p=[0.5, 0.5])
# Sets each cells starting state with a 50% probability of being either alive or dead.
        self.running = False
# Boolean controls when real time simulation is enabled
        self.ruleName = "Class 4"
        self.bind(pos=self.redraw, size=self.redraw)
# Forces the grid to redraw when the window is moved or resized because the redraw
# method relies on widget size values to draw properly.
        Clock.schedule_once(self.redraw, 0)
# Ensures starting grid renders properly once relevant parameters are set.

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
# Clears the canvas and redraws the cell rectangles based on the current grid.
# Called whenever the grid composition or widget geometry changes.

    def _computeNext(self):
        self.grid = applyRule(self.grid, self.ruleName)
        self.redraw()
# Calls update method from the PetriDish file and updates the grid with returned matrix.
# Internal method used by both real time and single step methods.

    def updateGeneration(self, dt=None):
        if not self.running:
            return
        self._computeNext()
# Calls computeNext method when real time simulation is enabled.

    def startSimulation(self):
        self.running = True
        Clock.schedule_interval(self.updateGeneration, 0.1)
# Defines the time interval of the updateGeneration call and starts the clock for
# real time generation, called on kivy toggle button press.

    def stopSimulation(self):
        self.running = False
        Clock.unschedule(self.updateGeneration)
# Called when real time generation button un-toggles.

    def step(self):
        self._computeNext()
# Called on generation step button press.

    def randomise(self):
        self.grid = np.random.choice([0, 1], size=(self.rows, self.cols), p=[0.5, 0.5])
        self.redraw()
# Same as the randomisation in initialisation, generates new starting conditions
# whenever a new rule is set or when the randomise button is pressed.

    def setRule(self, ruleName):
        self.ruleName = ruleName
        self.randomise()
# Sets the current rule to whatever is selected in the Kivy dropdown box.

