from generateData import generatePopulation
import numpy as np



if __name__ == "__main__":
    pop = generatePopulation(32)
    W = np.round(np.sum(pop, axis=0)[0] * 0.3, 1)

    print(W)

