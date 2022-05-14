from generateData import generateItems, generatePopulation, calcValue
import numpy as np
import time

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


def binaryMutation(pop, p_bar, p_gen_type=.6):
    numOfItems = len(pop[0][1])
    # print(numOfItems)
    for el in pop:
        p = np.random.rand()
        if p >= p_bar:
            rep = np.zeros(numOfItems, dtype=int).tolist()
            for i in range(0, numOfItems):
                pp = np.random.rand()
                if pp >= p_gen_type:
                    rep[i] = 1
                    el[1][i] = rep[i] ^ el[1][i]
    # print(pop)
    return pop
    ## HARDCORE VERSION ##
    # for el in pop:
    #     p = np.random.rand()
    #     if p >= p_bar:
    #         rep = np.zeros(numOfItems, dtype=int).tolist()
    #         for i in range(0, numOfItems):
    #             rep[i] = (el[1][i] + 1) % 2
    #         el[1] = rep
    # print(pop)
    # return pop

def findBest(population):
    bestOne = 0
    bestKnapsack = []
    for el in population:
        actual = el[0]
        if actual > bestOne:
            bestOne = actual
            bestKnapsack = el[1]
    return [bestOne, bestKnapsack]

def findOpt(population, numOfGen, tournamentSize, p_bar, p_gen_type):
    theBest = [0, np.zeros(len(population[0][1]), dtype=int).tolist()]
    for _ in range(0, numOfGen):
        population = doTournament(population, tournamentSize).copy()
        population = binaryMutation(population, p_bar, p_gen_type).copy()
        population = adjustValues(population)
        best = findBest(population)
        if best[0] > theBest[0]:
            theBest = best
            # print(theBest)
    return theBest

if __name__ == "__main__":
    global items
    items = generateItems(N)
    print(items)

    population_reps = 100
    numOfGen = 500
    tournamentSize = 2
    p_bar = 0.6 # p-nstwo zdarzenia mutacji
    p_gen_type = 0.4 # p-nstwo bardziej zroznicowanego genotypu

    W_max = np.round(np.sum(items, axis=0)[0] * 0.3, 1)  # max weight of knapsack
    print(W_max)
    population = generatePopulation(items, population_reps, W_max)
    population = adjustValues(population)
    print('first population:')
    print(population)

    best = []
    best = findOpt(population, numOfGen, tournamentSize, p_bar, p_gen_type)
    print(best)
    print("best value:", best[0])
    print("best knapsack:", best[1])



