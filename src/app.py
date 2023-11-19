import pygame as pg
import config as c
import threading as th

from model import Model
from simulatedannealing import simulatedAnnealing
from singleton import Singleton

class App:

    running = True

    def __init__(self):

        pg.init()

        self.screen = pg.display.set_mode(c.RESOLUTION, pg.RESIZABLE)

        self.model = Model()

        self.distFont = pg.font.SysFont("Arial", 40, True)

        sA = th.Thread(target=simulatedAnnealing, args=(self.model,))

        sA.start()

        clock = pg.time.Clock()

        while Singleton.running:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    Singleton.running = False

            self.renderFrame()

            pg.display.update()

            clock.tick(60)

    def renderFrame(self):

        if len(self.model.nodes) == self.model.count:

            self.screen.fill((255, 255, 255))

            self.renderGraph()
            self.renderModel()

    def renderGraph(self):

        screenSize = self.screen.get_size()

        x1 = c.GRAPH_PADDING
        y1 = screenSize[1] - c.GRAPH_PADDING - c.GRAPH_LINE_WIDTH
        w1 = screenSize[0] - (c.GRAPH_PADDING * 2) - c.GRAPH_LINE_WIDTH
        h1 = c.GRAPH_LINE_WIDTH

        x2 = screenSize[0] - c.GRAPH_PADDING - c.GRAPH_LINE_WIDTH
        y2 = c.GRAPH_PADDING
        w2 = c.GRAPH_LINE_WIDTH
        h2 = screenSize[1] - (c.GRAPH_PADDING * 2)

        x3 = c.GRAPH_PADDING + c.GRAPH_LINE_WIDTH
        y3 = c.GRAPH_PADDING
        w3 = w1
        h3 = h1

        x4 = c.GRAPH_PADDING
        y4 = c.GRAPH_PADDING
        w4 = w2
        h4 = h2

        pg.draw.rect(self.screen, c.GRAPH_COLOUR, (x1, y1, w1, h1))
        pg.draw.rect(self.screen, c.GRAPH_COLOUR, (x2, y2, w2, h2))
        pg.draw.rect(self.screen, c.GRAPH_COLOUR, (x3, y3, w3, h3))
        pg.draw.rect(self.screen, c.GRAPH_COLOUR, (x4, y4, w4, h4))

        originX = c.GRAPH_PADDING + c.GRAPH_LINE_WIDTH
        originY = screenSize[1] - c.GRAPH_PADDING - c.GRAPH_LINE_WIDTH

        graphWidth = screenSize[0] - (2 * (c.GRAPH_PADDING + c.GRAPH_LINE_WIDTH))
        graphHeight = screenSize[1] - (2 * (c.GRAPH_PADDING + c.GRAPH_LINE_WIDTH))

        n = c.GRAPH_NOTCH_SPACING
        while (n < self.model.width):

            offset = c.GRAPH_LINE_WIDTH / 2

            x1 = originX + ((n / self.model.width) * graphWidth) - offset
            y1 = originY - c.GRAPH_NOTCH_LENGTH

            x2 = x1
            y2 = c.GRAPH_PADDING + c.GRAPH_LINE_WIDTH

            pg.draw.rect(self.screen, c.GRAPH_COLOUR, (x1, y1, c.GRAPH_LINE_WIDTH, c.GRAPH_NOTCH_LENGTH))
            pg.draw.rect(self.screen, c.GRAPH_COLOUR, (x2, y2, c.GRAPH_LINE_WIDTH, c.GRAPH_NOTCH_LENGTH))

            n += c.GRAPH_NOTCH_SPACING

        n = c.GRAPH_NOTCH_SPACING
        while (n < self.model.height):

            offset = c.GRAPH_LINE_WIDTH / 2

            x1 = originX
            y1 = originY - ((n / self.model.height) * graphHeight) - offset

            x2 = screenSize[0] - c.GRAPH_PADDING - c.GRAPH_LINE_WIDTH - c.GRAPH_NOTCH_LENGTH
            y2 = y1

            pg.draw.rect(self.screen, c.GRAPH_COLOUR, (x1, y1, c.GRAPH_NOTCH_LENGTH, c.GRAPH_LINE_WIDTH))
            pg.draw.rect(self.screen, c.GRAPH_COLOUR, (x2, y2, c.GRAPH_NOTCH_LENGTH, c.GRAPH_LINE_WIDTH))

            n += c.GRAPH_NOTCH_SPACING

    def renderModel(self):

        screenSize = self.screen.get_size()
        originX = c.GRAPH_PADDING + c.GRAPH_LINE_WIDTH
        originY = screenSize[1] - c.GRAPH_PADDING - c.GRAPH_LINE_WIDTH

        graphWidth = screenSize[0] - (2 * (c.GRAPH_PADDING + c.GRAPH_LINE_WIDTH))
        graphHeight = screenSize[1] - (2 * (c.GRAPH_PADDING + c.GRAPH_LINE_WIDTH))

        for i in range(len(self.model.edges)):

            node1 = self.model.getEdge(i).n1
            node2 = self.model.getEdge(i).n2

            x1 = originX + ((node1.x / self.model.width) * graphWidth)
            y1 = originY - ((node1.y / self.model.height) * graphHeight)

            x2 = originX + ((node2.x / self.model.width) * graphWidth)
            y2 = originY - ((node2.y / self.model.height) * graphHeight)

            pg.draw.line(self.screen, c.EDGE_COLOUR, (x1, y1), (x2, y2), c.EDGE_WIDTH)

        for i in range(self.model.count):

            node = self.model.getNode(i)

            x = originX + ((node.x / self.model.width) * graphWidth)
            y = originY - ((node.y / self.model.height) * graphHeight)

            pg.draw.circle(self.screen, c.NODE_COLOUR, (x, y), c.NODE_RADIUS)

        text = self.distFont.render(f"{round(self.model.distance, 2)}", True, (0, 0, 0))
        self.screen.blit(text, (screenSize[0] - c.GRAPH_PADDING - c.GRAPH_LINE_WIDTH - text.get_width() - 5,
                                     screenSize[1] - c.GRAPH_PADDING - c.GRAPH_LINE_WIDTH - text.get_height() - 5))