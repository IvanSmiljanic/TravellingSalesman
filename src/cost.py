import math as m

def cost(solution, model):

    sum = 0

    for i in range(len(solution) - 1):

        sum += m.sqrt((model.getNode(solution[i]).x - model.getNode(solution[i+1]).x) ** 2 + (model.getNode(solution[i]).y - model.getNode(solution[i + 1]).y) ** 2)

    sum += m.sqrt((model.getNode(solution[len(solution) - 1]).x - model.getNode(solution[0]).x) ** 2 + (model.getNode(solution[len(solution) - 1]).y - model.getNode(solution[0]).y) ** 2)

    return sum