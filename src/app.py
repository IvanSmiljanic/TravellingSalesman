import pygame as pg
import config as c

class App:

    def __init__(self):

        pg.init()

        self.screen = pg.display.set_mode(c.RESOLUTION, pg.RESIZABLE)

        looping = True

        while looping:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    looping = False

            pg.display.update()