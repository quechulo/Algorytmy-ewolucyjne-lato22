from generateData import generateItems, generatePopulation, calcValue
import numpy as np

N = 32



def adjustValues(population):
    for el in population:
        el[0] = calcValue(el[1], items)
    return population


def doTournament(population, s):
    idxs = []
    population = adjustValues(population)
    population.sort()
    # print(population)

    while(len(idxs) != s):
        idx = np.random.randint(0, len(population))
        if idx not in idxs:
            idxs.append(idx)
    # print(idxs)
    bestValue = 0

    for id in idxs:
        if population[id][0] >= bestValue:
            bestValue = population[id][0]
            winner = id
    for id in idxs:
        population[id] = population[winner].copy()
    # print(population)
    return population


def binaryMutation(pop, p_bar):
    numOfItems = len(pop[0][1])
    # print(numOfItems)

    for el in pop:
        p = np.random.rand()
        if p >= p_bar:
            rep = np.zeros(numOfItems, dtype=int).tolist()
            for i in range(0, numOfItems):
                rep[i] = (el[1][i] + 1) % 2
            el[1] = rep
    # print(pop)
    return pop


def findOpt(population, numOfGen, tournamentSize, p_bar):
    for _ in range(0, numOfGen):
        population = doTournament(population, tournamentSize).copy()
        population = binaryMutation(population, p_bar).copy()
        population = adjustValues(population)
    return population

if __name__ == "__main__":
    global items
    items = generateItems(N)
    print(items)

    population_reps = 100
    numOfGen = 500
    tournamentSize = 2
    p_bar = 0.4

    W_max = np.round(np.sum(items, axis=0)[0] * 0.3, 1)  # max weight of knapsack
    print(W_max)
    population = generatePopulation(items, population_reps, W_max)

    population = findOpt(population, numOfGen, tournamentSize, p_bar)
    bestOne = 0
    bestKnapsack = []
    for el in population:
        actual = el[0]
        if actual > bestOne:
            bestOne = actual
            bestKnapsack = el[1]
        print(el[0]) # 659.0 best ever
    print('#########  BEST  #########')
    print(bestOne)
    print(bestKnapsack)


