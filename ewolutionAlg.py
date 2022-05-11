from generateData import generatePopulation
import numpy as np

N = 32


if __name__ == "__main__":
    pop = generatePopulation(N)
    W = np.round(np.sum(pop, axis=0)[0] * 0.3, 1)  # max weight of knapsack



