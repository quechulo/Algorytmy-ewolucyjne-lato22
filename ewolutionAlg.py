from generateData import generateItems, generatePopulation, calcValue, calcWeight
import numpy as np

N = 32
population_reps = 5


if __name__ == "__main__":
    items = generateItems(N)
    print(items)
    W_max = np.round(np.sum(items, axis=0)[0] * 0.3, 1)  # max weight of knapsack
    print(W_max)
    population = generatePopulation(items, population_reps, W_max)
    print(population)
