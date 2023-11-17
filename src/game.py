import pygame as pg

from src.managers.display_manager import DisplayManager
from src.managers.event_manager import EventManager

from src.input.mouse import Mouse
from src.input.key import Keys


class Game:
    def __init__(self):
        pg.init()

        # initialize all the managers
        self.dm = DisplayManager()
        self.em = EventManager()

        # input managers
        self.mouse = Mouse()
        self.keys = Keys()

    def run(self):
        while self.dm.running:
            self.update(self.dm.dt)
            self.handle_events(self.em.events)
            self.draw(self.dm.dt)

    def draw(self, *args):
        dt = args[0]

        self.dm.clear_display()

    def update(self, *args):
        dt = args[0]

        # managers update
        self.dm.update()
        self.em.update()

        # mouse and keys update
        self.mouse.update()
        self.keys.update()

        self.mouse.handle_events(self.em.events)
        self.keys.handle_events(self.em.events)

    def handle_events(self, *args):
        events = args[0]

        self.dm.handle_events(events)
