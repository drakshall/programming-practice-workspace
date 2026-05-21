import numpy as np

def MooreNeighbourCount(grid):
    return (np.roll(grid, ( 1,  1), (0, 1)) +
            np.roll(grid, ( 1,  0), (0, 1)) +
            np.roll(grid, ( 1, -1), (0, 1)) +
            np.roll(grid, ( 0,  1), (0, 1)) +
            np.roll(grid, ( 0, -1), (0, 1)) +
            np.roll(grid, (-1,  1), (0, 1)) +
            np.roll(grid, (-1,  0), (0, 1)) +
            np.roll(grid, (-1, -1), (0, 1)))
# Returns a 2D array with every element corresponding to a cell in the actual
# grid, each of these elements contains the number of live cells adjacent to
# the corresponding cell in the actual grid.


def applyRule(grid, ruleName):
    neighbours = MooreNeighbourCount(grid)
    newGrid = np.zeros_like(grid)

    if ruleName == "Class 1":
        newGrid = (neighbours >= 4).astype(np.uint8)
# Compares the neighbour count value associated with every cell in the grid to 
# see if they are 4 or greater, if so the cell is set to 1 (alive), and if not
# it is set to 0 (dead).

    elif ruleName == "Class 2":
        newGrid = grid.copy()
        newGrid[neighbours == 3] = 1 - newGrid[neighbours == 3]
# Selects cells with 3 neighbours and flips the values of those cells,
# (1 - 0 = 1 and 1 - 1 = 0).
# Also copies the grid into a new variable for consistency with implementation
# of other rules, not strictly necessary for this kind of operation.

    elif ruleName == "Class 3":
        lookupTable = np.array([0, 1, 1, 1, 0, 0, 0, 0, 0], dtype=np.uint8)
        newGrid = lookupTable[neighbours]
# Takes the neighbour count of each cell and uses that value as an index in this
# lookup table to determine whether their value is set to 1 (alive) or 0 (dead).

    elif ruleName == "Class 4":
        birth = (grid == 0) & (neighbours == 3)
        survive = (grid == 1) & ((neighbours == 2) | (neighbours == 3))
        newGrid = (birth | survive).astype(np.uint8)
# Brings a dead cell to life if it has 3 neighbours and kills a living cell
# if it has fewer or greater than 2 or 3 neighbours, Conway's game of life.
    return newGrid
