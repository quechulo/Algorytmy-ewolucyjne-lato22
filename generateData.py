import numpy as np

INDEX = 305862
np.random.seed(INDEX)  # lowest index


def generatePopulation(N):
    pop = []
    pop_weights = np.random.uniform(0.1, 1, (N, 1))
    pop_p = np.random.uniform(1, 100, (N, 1))

    for i in range(0, N):
        pop_weights[i][0] = np.round(pop_weights[i][0], 1)
        pop_p[i][0] = np.round(pop_p[i][0])
        chap = [pop_weights[i][0], pop_p[i][0]]
        pop.append(chap)
    # print(pop)
    return pop

if __name__ == "__main__":
    generatePopulation(32)