import math as m

import config as c
import random as r

class Node:

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def __repr__(self):

        return f"({self.x}, {self.y})"

class Edge:

    def __init__(self, n1, n2):

        self.n1 = n1
        self.n2 = n2

    def __repr__(self):

        return f"({self.n1}, {self.n2})"

class Model:

    def __init__(self):

        self.width = c.MODEL_WIDTH
        self.height = c.MODEL_HEIGHT
        self.count = c.MODEL_NODE_COUNT

        self.nodes = []
        self.edges = []

        self.distance = 0

        self.populateRandomly()

        self.calculateDistance()

    def getNode(self, n):

        return self.nodes[n]

    def getEdge(self, n):

        return self.edges[n]

    def stateFromSolution(self, solution):

        self.edges = []

        for i in range(len(solution) - 1):

            self.edges.append(Edge(self.nodes[solution[i]], self.nodes[solution[i+1]]))

        self.edges.append(Edge(self.nodes[solution[-1]], self.nodes[solution[0]]))

        self.calculateDistance()

    def calculateDistance(self):

        self.distance = 0

        for edge in self.edges:

            self.distance += m.sqrt((edge.n1.x - edge.n2.x) ** 2 + (edge.n1.y - edge.n2.y) ** 2)

    def populateRandomly(self):

        for i in range(self.count):

            self.nodes.append(Node(r.random() * self.width, r.random() * self.height))