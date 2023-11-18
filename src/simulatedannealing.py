import random as r
import copy
import config as c
import math as m
from cost import cost
import time
from singleton import Singleton

def randomNeighbour(solution):

    newSolution = copy.copy(solution)

    r1 = r.randint(0, len(solution) - 1)
    r2 = r.randint(0, len(solution) - 1)

    temp = newSolution[r1]
    newSolution[r1] = newSolution[r2]
    newSolution[r2] = temp

    return newSolution

def simulatedAnnealing(model):

    currentSolution = [i for i in range(model.count)]

    model.stateFromSolution(currentSolution)

    t = c.INITIAL_TEMPERATURE

    while t > .0001 and Singleton.running:

        neighbour = randomNeighbour(currentSolution)

        costN = cost(neighbour, model)
        costC = cost(currentSolution, model)

        if costN >= costC:

            if m.e ** ((costC - costN) / t) > .5:

                currentSolution = neighbour
                model.stateFromSolution(currentSolution)

        else:

            currentSolution = neighbour
            model.stateFromSolution(currentSolution)

        t *= c.SCHEDULE_CONST