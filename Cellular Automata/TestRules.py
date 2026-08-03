
import numpy as np
import pytest
from Controller import GridWidget
from unittest.mock import Mock, patch
from PetriDish import MooreNeighbourCount, applyRule
import time
import matplotlib.pyplot as plt


#======================================= Simulation analysis testing (3&4 NON DETERMINISTIC) =======================================#


# def _runTest(ruleName, steps=200, gridSize=50):
# # Internal method that runs a simulation for the given rule and records then returns the grid history.
#     grid = np.random.choice([0, 1], size=(gridSize, gridSize), p=[0.5, 0.5])
# # Randomises start conditions with each cell having a 50% chance of being alive.
#     history = [grid.copy()]
#     for _ in range(steps):
#         grid = applyRule(grid, ruleName)
#         history.append(grid.copy())
#     return history


# def testUniformity(ruleName, steps, gridSize):
#     start = time.time()
# # Tests whether rules cause random starting conditions to converge into a uniform state,
# # either all alive or dead.
#     print(f"\n=== Testing Uniformity of {ruleName} rule ===")
#     history = _runTest(ruleName, steps, gridSize)
#     final = history[-1]
#     unique = np.unique(final)
# # Checks if elements in the final grid matrix are uniform.
#     if len(unique) == 1:
#         for i, grid in enumerate(history):
#             if np.all(grid == final):
#                 end = time.time()
#                 print(f"Time elapsed: {end - start:.2f} seconds")
#                 if all(np.all(history[j] == final) for j in range(i, len(history))):
# # Checks that from i onward, all grids are identical
#                     print(f"Became stable at generation {i}.")
#                 else:
#                     print(f"Reached uniform state at generation {i} but did not stay stable.")
#                 break
#     else:
#         end = time.time()
#         print(f"Time elapsed: {end - start:.2f} seconds")
#         print(f"Not uniform after {steps} steps. still has {len(unique)} values.")


# def testRepetition(ruleName, steps, gridSize):
#     start = time.time()
# # Tests whether random conditions result in oscillating behaviour, such as that typical of class 2 behaviour.
#     print(f"\n=== Testing Repetition of {ruleName} rule ===")
#     history = _runTest(ruleName, steps, gridSize)
#     periodDetected = None
#     for period in range(2, (steps//2)):
#         for offset in range(1, len(history) - period):
#             if np.array_equal(history[offset], history[offset + period]):
#                 consistent = True
#                 maxChecks = min(9, (len(history) - 1 - offset) // period - 1)
#                 for check in range(1, maxChecks + 1):
#                     if not np.array_equal(history[offset + check*period], history[offset + (check+1)*period]):
#                         consistent = False
#                         break
# # Takes the range of suspected oscillation and adds that range to the current generation's history index to
# # find the next expected instance of that oscillation and checks if it matches prior oscillations, checks
# # the cycle as many times as possible in the test's generation history to maximise validity.
#                 if consistent:
#                     periodDetected = period
#                     startOffset = offset
#                     break
#         if periodDetected:
#             break
#     if periodDetected:
#         end = time.time()
#         print(f"Time elapsed: {end - start:.2f} seconds")
#         print(f"Detected periodic behaviour with period = {periodDetected}.")
#         print(f"Cycle begins at generation {startOffset} and repeats every {periodDetected} steps.")
#     else:
#         end = time.time()
#         print(f"Time elapsed: {end - start:.2f} seconds")
#         print(f"No clear period detected within {steps} generations.")


# def testSensitivity(ruleName, steps, gridSize):
# # Tests the sensitivity of a rule to its starting conditions.
#     start = time.time()
#     print(f"\n=== Testing Sensitivity of {ruleName} rule ===")
#     grid1 = np.random.choice([0, 1], size=(gridSize, gridSize), p=[0.5, 0.5])
#     grid2 = grid1.copy()
#     i, j = np.random.randint(0, gridSize, 2)
#     grid2[i, j] = 1 - grid2[i, j]
# # Generates two grids with identical starting conditions and inverts a single random cell in the
# # second grid to produce a single bit difference in starting conditions.
#     for _ in range(steps):
#         grid1 = applyRule(grid1, ruleName)
#         grid2 = applyRule(grid2, ruleName)

#     diff = np.sum(grid1 != grid2) / (gridSize * gridSize)
#     end = time.time()
#     print(f"Time elapsed: {end - start:.2f} seconds")
#     print(f"After {steps} steps, a single bit initial difference leads to {diff * 100:.1f}% divergence.")


# def testDensity(ruleName, steps, gridSize):
# # Method that computes and plots a graph of the density of living cells in each generation of a test.

#     history = _runTest(ruleName, steps, gridSize)
#     densities = [np.mean(grid) for grid in history]   
#     generations = range(len(history))
#     print(f"\n=== Testing Density of {ruleName} Rule ===")
#     plt.figure(figsize=(8, 5))
#     plt.plot(generations, densities, linewidth=0.8, color='blue')
#     plt.xlabel("Generation")
#     plt.ylabel("Live cell density (fraction)")
#     plt.title(f"Density over time – {ruleName}")
#     plt.grid(True, alpha=0.3)
#     plt.ylim(0, 1)
#     plt.show()
    
#     print(f"Mean density: {np.mean(densities):.3f}")
#     print(f"Std deviation: {np.std(densities):.3f}")
#     print(f"Min: {np.min(densities):.3f}, Max: {np.max(densities):.3f}")

# classes = ["Class 1","Class 2","Class 3","Class 4"]
# testDensity("Class 4", 1000, 50)
# testDensity("Class 3", 1000, 50)
# testDensity("Class 1", 25, 50)
# testDensity("Class 2", 200, 50)


#======================================= Unit testing =======================================#


def testGridStateIntegrity():
# Objective 1 - Verifies that the grid is drawn correctly and that cells only represent binary values.
    rows, cols = 5, 7
    gridWidget = GridWidget(targetRows=rows, targetCols=cols)
    
    assert gridWidget.grid.shape == (rows, cols)
    # Criterion 1: 100% match specified dimensions.
    
    uniqueValues = np.unique(gridWidget.grid)
    assert np.all(np.isin(gridWidget.grid, [0, 1]))
    # Criterion 2: 0% cells outside (0, 1).
    
    assert set(uniqueValues).issubset({0, 1})
    # Criterion 3: np.unique() returns (0, 1).
    
    gridWidget.setGridSize(10, 10)
    assert gridWidget.grid.shape == (10, 10)
    assert np.all(np.isin(gridWidget.grid, [0, 1]))
    # Tests resize method as well.


def testMooreNeighbourhoodAccuracy():
# Objective 2 - Verify neighbour counting for all cells including edges/corners.
    
    grid = np.array([
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0]
    ], dtype=np.uint8)
    # Known 5x5 pattern (checkerboard).
    
    expectedManual = np.array([
        [4, 3, 5, 3, 4],
        [3, 4, 4, 4, 3],
        [5, 4, 4, 4, 5],
        [3, 4, 4, 4, 3],
        [4, 3, 5, 3, 4]
    ], dtype=np.uint8)
    # Manually computed neighbour matrix for this pattern with periodic boundaries.
    
    result = MooreNeighbourCount(grid)

    assert np.array_equal(result, expectedManual)
    # Criterion 1: 100% bitwise accuracy 
    
    assert result[0, 0] == 4  # Top-left corner.
    assert result[0, 1] == 3  # Top edge.
    assert result[0, 4] == 4  # Top-Right corner.
    assert result[1, 0] == 3  # Left edge.
    assert result[2, 4] == 5  # Right edge.
    assert result[4, 4] == 4  # Bottom-right corner.
    assert result[4, 2] == 5  # Bottom edge.
    assert result[4, 0] == 4  # Bottom-left corner.
    # Criterion 2: Edge/corner cells produce expected count without exceptions.


@pytest.mark.parametrize("ruleName", ["Class 1", "Class 2", "Class 3", "Class 4"])
# Parametrised so that one obj3 test failing doesnt result in every obj3 test failing
def testRuleApplicationLogic(ruleName):
# Objective 3 - Verify deterministic output for 10 static input grids per rule.
    
    np.random.seed(42)
    testInputs = []
    for _ in range(10):
        grid = np.random.choice([0, 1], size=(5, 5), p=[0.5, 0.5]).astype(np.uint8)
        testInputs.append(grid)
    # Generates 10 static input grids (seed for reproducibility).
    
    expectedList = []
    for grid in testInputs:
        neighbours = MooreNeighbourCount(grid)
        if ruleName == "Class 1":
            exp = (neighbours >= 4).astype(np.uint8)
        elif ruleName == "Class 2":
            exp = grid.copy()
            exp[neighbours == 3] = 1 - exp[neighbours == 3]
        elif ruleName == "Class 3":
            lookup = np.array([0, 1, 1, 1, 0, 0, 0, 0, 0], dtype=np.uint8)
            exp = lookup[neighbours]
        elif ruleName == "Class 4":
            birth = (grid == 0) & (neighbours == 3)
            survive = (grid == 1) & ((neighbours == 2) | (neighbours == 3))
            exp = (birth | survive).astype(np.uint8)
        expectedList.append(exp)
    # Pre-calculates outputs using the expected logic.
    
    for i, inputGrid in enumerate(testInputs):
        result = applyRule(inputGrid, ruleName)
        assert np.array_equal(result, expectedList[i]), f"Failed for rule {ruleName} on input {i}"
    # Runs the actual applyRule and asserts against the pre-calculated expecteds.


#======================================= UI Integration & acceptence testing =======================================#


@pytest.fixture
# Fixture decorator to create a clean GridWidget for each UI test.
def gridWidget():
    widget = GridWidget(targetRows=5, targetCols=5)
    widget.running = False
    return widget


def testRuleSwitching(gridWidget):
# Objective 4 - Verify UI preset selection updates ruleName and resets grid.
    initialGrid = gridWidget.grid.copy()
    numSwitches = 25
    rules = ["Class 1", "Class 2", "Class 3", "Class 4"]
    
    for _ in range(numSwitches):
        for rule in rules:
            gridWidget.setRule(rule)
            # Simulates UI selection (calls setRule).
            
            assert gridWidget.ruleName == rule
            # Criterion 1: ruleName variable updates.
            
            assert np.any(gridWidget.grid != initialGrid), f"Grid did not change on rule switch to {rule}"
            initialGrid = gridWidget.grid.copy()
            # Criterion 2: Grid is reset/randomised (bitwise accuracy < 100%).
            # With a 5x5 grid, the chance of identical random grid is 1/2^25 (~0.000003%).


def testPauseResume(gridWidget):
# Objective 5 - Verify pause halts generation and resume restores exact state.
    gridWidget.startSimulation()
    assert gridWidget.running is True
    # Starts simulation.
    
    gridWidget.stopSimulation()
    assert gridWidget.running is False
    # Immediately stops (pause).

    pausedGrid = gridWidget.grid.copy()
    # Stores the grid state at pause.
    
    gridWidget.startSimulation()
    assert gridWidget.running is True
    # Resumes simulation.
    
    gridWidget.stopSimulation()
    # Immediately stops again to check if the state remained identical during the transition.
    
    assert np.array_equal(gridWidget.grid, pausedGrid)
    # Criterion: State is identical to when it was paused (no clock tick occurred).


def testSingleStep(gridWidget):
# Objective 6 - Verify that single step increments once and remains paused.
    gridWidget.running = False
    # Ensures it starts paused.
    initialGrid = gridWidget.grid.copy()
    
    numSteps = 50
    for _ in range(numSteps):
        gridWidget.step()
        assert gridWidget.running is False, "Simulation resumed running after single step"
        # Criterion: Verifies that the simulation stays paused.
    assert gridWidget.running is False



def testResetRandomise(gridWidget):
# Objective 7 - Verify that reset wipes state and reinitialises to a new random config.
    gridWidget.running = False
    
    passes = 0
    trials = 100
    
    for _ in range(trials):
        gridWidget.grid = np.random.choice([0, 1], size=(5, 5), p=[0.5, 0.5]).astype(np.uint8)
        initialGrid = gridWidget.grid.copy()
        # Sets a known initial grid
        
        gridWidget.randomise()
        # Simulate pressing the 'Randomise' button
        
        if np.any(gridWidget.grid != initialGrid):
            passes += 1
        # Criterion: Bitwise accuracy < 1 (99% pass rate).
        # With 5x5, the chance of identical is 1/2^25, so statistically 100% of trials will pass.
    
    assert passes >= trials * 0.99, f"Only {passes}/{trials} passes for Hamming distance > 0"
    # Succeeds if at least 99 out of 100 trials passed.


def testModelViewSynchronisation(gridWidget):
# Objective 8 - Verify Kivy canvas rendering matches the underlying grid matrix.
    
    testGrid = np.array([
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1]
    ], dtype=np.uint8)
    # Defines non-random test grid.

    gridWidget.targetRows, gridWidget.targetCols = 3, 3
    gridWidget.grid = testGrid
    # Assigns it to the widget.
    
    with patch('Controller.Rectangle') as mockRectangle, \
         patch('Controller.Color') as mockColor:
    # Mock objects used to record the arguments applied for the sake of analysis without any additional external complexities.

        gridWidget.redraw()
        
        assert mockRectangle.call_count == 9, f"Expected 9 rectangles, got {mockRectangle.call_count}"
        # Verify the correct number of rectangles were drawn (3x3 = 9).

        assert mockColor.call_count == 9, f"Expected 9 Color calls, got {mockColor.call_count}"
        # Verify the correct number of Color calls (one per cell = 9).
        
        expectedColors = []
        for i in range(gridWidget.targetRows):
            for j in range(gridWidget.targetCols):
                if gridWidget.grid[i, j] == 1:
                    expectedColors.append((1, 1, 1, 1))  
                    # White for live.
                else:
                    expectedColors.append((0, 0, 0, 1))  
                    # Black for dead.
        # Verify each Color call had the correct RGBA arguments.
        
        actualCalls = [call[0] for call in mockColor.call_args_list]
        # Get the actual arguments that mockColor was called with, each call is a tuple of args
        
        for i, (expectedColor, actualCall) in enumerate(zip(expectedColors, actualCalls)):
            assert actualCall == expectedColor, \
                f"Cell {i}: Expected Color{expectedColor}, got Color{actualCall}"
        # Assert every call matches the expected color

pytest.main([__file__, "-v", "--tb=short", "-s"])

