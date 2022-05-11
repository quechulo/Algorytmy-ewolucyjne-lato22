from generateData import generateItems, generatePopulation
import numpy as np

N = 32



if __name__ == "__main__":
    pop = generateItems(N)
    print(pop)
    W = np.round(np.sum(pop, axis=0)[0] * 0.3, 1)  # max weight of knapsack
    print(W)


