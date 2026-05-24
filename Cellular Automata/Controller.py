# Defines the custom Kivy widget that draws the grid and controls the simulation as
# well as the button methods to control the simulation through the UI

import numpy as np
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.clock import Clock
from PetriDish import applyRule
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.config import Config
Config.set('graphics', 'fullscreen', 'auto')


class UIRoot(FloatLayout):
    pass
class UIApp(App):
    def build(self):
        return UIRoot()
# Classes define the app root and orchestrate the running of the program.


class GridWidget(Widget):
    def __init__(self, targetRows=81, targetCols=160, **kwargs):
# Size of grid in number of cells and visual size of cells in pixels.
        super().__init__(**kwargs)
        self.targetRows = targetRows
        self.targetCols = targetCols
        self.cellSize = 10
        self.grid = np.random.choice([0, 1], size=(targetRows, targetCols), p=[0.5, 0.5])
# Sets each cells starting state with a 50% probability of being either alive or dead.
        self.running = False
        self.ruleName = "Class 4"
        self.bind(pos=self.redraw, size=self._updateGridSize)
# Forces the grid to resize the grid when the widget is resized because the redraw
# method relies on widget size values to draw properly.
        Clock.schedule_once(self._updateGridSize, 0)
        Clock.schedule_once(self.redraw, 0)
# Ensures starting grid renders properly once relevant parameters are set.


    def redraw(self, *args):
        self.canvas.clear()
        totalWidth = self.targetCols * self.cellSize
        totalHeight = self.targetRows * self.cellSize
# Calculate the total size of the grid in pixels
        offsetX = (self.width - totalWidth) / 2
        offsetY = (self.height - totalHeight) / 2
# Offsets to centre the grid horizontally and vertically
        with self.canvas:
            for i in range(self.targetRows):
                for j in range(self.targetCols):
                    if self.grid[i, j] == 1:
                        Color(1, 1, 1, 1)
                    else:
                        Color(0, 0, 0, 1)
                    x = self.x + offsetX + j * self.cellSize
                    y = self.y + offsetY + self.targetRows * self.cellSize - (i + 1) * self.cellSize
                    Rectangle(pos=(x, y), size=(self.cellSize, self.cellSize))
# Clears the widget canvas and redraws the cell rectangles based on the currently defined.
# grid, called whenever the grid composition or widget geometry changes.

    def _updateGridSize(self, *args):
        availWidth = self.width
        availHeight = self.height
        cellByWidth = availWidth / self.targetCols
        cellByHeight = availHeight / self.targetRows
        self.cellSize = min(cellByWidth, cellByHeight)
        self.redraw()
# Called when the widget's size changes (window resize, fullscreen toggle).
# Computes the optimal cell size so that the square grid fills the available
# area while preserving the target number of rows and columns.

    def _computeNext(self):
        self.grid = applyRule(self.grid, self.ruleName)
        self.redraw()
# Calls applyRule method for the current grid state from the PetriDish file based on the
# selected class of automaton and updates the displayed grid with the returned matrix.
# Internal method used by both real time and single step button methods.

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
        self.grid = np.random.choice([0, 1], size=(self.targetRows, self.targetCols), p=[0.5, 0.5])
        self.redraw()
# Same as the randomisation in initialisation, generates new starting conditions
# whenever a new rule is set or when the randomise button is pressed.

    def setGridSize(self, newCols, newRows):
        newCols = max(1, newCols)
        newRows = max(1, newRows)
        if newCols == self.targetCols and newRows == self.targetRows:
            return
        self.targetCols = newCols
        self.targetRows = newRows
        self.grid = np.random.choice([0, 1], size=(self.targetRows, self.targetCols), p=[0.5, 0.5])
        self._updateGridSize()
        self.redraw()
# Called whenever the height & width text boxes are modified and randomises + redraws

    def setRule(self, ruleName):
        self.ruleName = ruleName
        self.randomise()
# Sets the current rule to whatever is selected in the Kivy dropdown box.


if __name__ == '__main__':
    UIApp().run()
