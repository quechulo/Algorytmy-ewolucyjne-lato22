from generateData import generateItems, generatePopulation, calcValue, calcWeight
import numpy as np

N = 32
population_reps = 5


def doTournament(population, s):
    idxs = []
    population.sort()
    # print(population)

    while(len(idxs) != s):
        idx = np.random.randint(0, len(population))
        if idx not in idxs:
            idxs.append(idx)
    # print(idxs)
    bestValue = 0

    for id in idxs:
        if population[id][0] > bestValue:
            bestValue = population[id][0]
            winner = id
    for id in idxs:
        population[id] = population[winner]
    # print(population)
    return population



if __name__ == "__main__":
    items = generateItems(N)
    print(items)
    W_max = np.round(np.sum(items, axis=0)[0] * 0.3, 1)  # max weight of knapsack
    print(W_max)
    population = generatePopulation(items, population_reps, W_max)

    population = doTournament(population, 2)
