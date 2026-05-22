import numpy as np
import time
import matplotlib.pyplot as plt
from PetriDish import applyRule


def runTest(ruleName, steps=200, gridSize=50):
# Runs a simulation for the given rule and records then returns the grid history.
# Steps control how long the simulation is run for.
    grid = np.random.choice([0, 1], size=(gridSize, gridSize), p=[0.5, 0.5])
# Randomises start conditions with each cell having a 50% chance of being alive.
    history = [grid.copy()]
    for _ in range(steps):
        grid = applyRule(grid, ruleName)
        history.append(grid.copy())
    return history


def testUniformity(ruleName, steps, gridSize):
    start = time.time()
# Tests whether rules cause random starting conditions to converge into a uniform state,
# either all alive or dead.
    print(f"\n=== Testing Uniformity of {ruleName} rule ===")
    history = runTest(ruleName, steps, gridSize)
    final = history[-1]
    unique = np.unique(final)
# Checks if elements in the final grid matrix are uniform.
    if len(unique) == 1:
        for i, grid in enumerate(history):
            if np.all(grid == final):
                end = time.time()
                print(f"Time elapsed: {end - start:.2f} seconds")
                if all(np.all(history[j] == final) for j in range(i, len(history))):
# Checks that from i onward, all grids are identical
                    print(f"Became stable at generation {i}.")
                else:
                    print(f"Reached uniform state at generation {i} but did not stay stable.")
                break
    else:
        end = time.time()
        print(f"Time elapsed: {end - start:.2f} seconds")
        print(f"Not uniform after {steps} steps. still has {len(unique)} values.")


def testRepetition(ruleName, steps, gridSize):
    start = time.time()
# Tests whether random conditions result in oscillating behaviour, such as that typical of class 2 behaviour.
    print(f"\n=== Testing Repetition of {ruleName} rule ===")
    history = runTest(ruleName, steps, gridSize)
    periodDetected = None
    for period in range(2, (steps//2)):
        for offset in range(1, len(history) - period):
            if np.array_equal(history[offset], history[offset + period]):
                consistent = True
                maxChecks = min(9, (len(history) - 1 - offset) // period - 1)
                for check in range(1, maxChecks + 1):
                    if not np.array_equal(history[offset + check*period], history[offset + (check+1)*period]):
                        consistent = False
                        break
# Takes the range of suspected oscillation and adds that range to the current generation's history index to
# find the next expected instance of that oscillation and checks if it matches prior oscillations, checks
# the cycle as many times as possible in the test's generation history to maximise validity.
                if consistent:
                    periodDetected = period
                    startOffset = offset
                    break
        if periodDetected:
            break
    if periodDetected:
        end = time.time()
        print(f"Time elapsed: {end - start:.2f} seconds")
        print(f"Detected periodic behaviour with period = {periodDetected}.")
        print(f"Cycle begins at generation {startOffset} and repeats every {periodDetected} steps.")
    else:
        end = time.time()
        print(f"Time elapsed: {end - start:.2f} seconds")
        print(f"No clear period detected within {steps} generations.")


def testSensitivity(ruleName, steps, gridSize):
# Tests the sensitivity of a rule to its starting conditions.
    start = time.time()
    print(f"\n=== Testing Sensitivity of {ruleName} rule ===")
    grid1 = np.random.choice([0, 1], size=(gridSize, gridSize), p=[0.5, 0.5])
    grid2 = grid1.copy()
    i, j = np.random.randint(0, gridSize, 2)
    grid2[i, j] = 1 - grid2[i, j]
# Generates two grids with identical starting conditions and inverts a single random cell in the
# second grid to produce a single bit difference in starting conditions.
    for _ in range(steps):
        grid1 = applyRule(grid1, ruleName)
        grid2 = applyRule(grid2, ruleName)

    diff = np.sum(grid1 != grid2) / (gridSize * gridSize)
    end = time.time()
    print(f"Time elapsed: {end - start:.2f} seconds")
    print(f"After {steps} steps, a single bit initial difference leads to {diff * 100:.1f}% divergence.")


def testDensity(ruleName, steps, gridSize):
# Method that computes and plots a graph of the density of living cells in each generation of a test.

    history = runTest(ruleName, steps, gridSize)
    densities = [np.mean(grid) for grid in history]   
    generations = range(len(history))
    print(f"\n=== Testing Density of {ruleName} Rule ===")
    plt.figure(figsize=(15, 5))
    plt.plot(generations, densities, linewidth=0.8, color='blue')
    plt.xlabel("Generation")
    plt.ylabel("Live cell density (fraction)")
    plt.title(f"Density over time – {ruleName}")
    plt.grid(True, alpha=0.3)
    plt.ylim(0, 1)
    plt.show()
    
    print(f"Mean density: {np.mean(densities):.3f}")
    print(f"Std deviation: {np.std(densities):.3f}")
    print(f"Min: {np.min(densities):.3f}, Max: {np.max(densities):.3f}")

testUniformity("Class 1", 50, 50)
testDensity("Class 1", 50, 50)