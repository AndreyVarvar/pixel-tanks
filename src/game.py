import pygame as pg
from src.managers.display_manager import DisplayManager
from src.managers.event_manager import EventManager
from src.input.mouse import Mouse


class Game:
    def __init__(self):
        self.dm = DisplayManager()
        self.em = EventManager()

        self.mouse = Mouse()

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

        self.dm.update()
        self.em.update()
        self.mouse.update()

    def handle_events(self, *args):
        events = args[0]

        self.dm.handle_events(events)
        self.mouse.handle_events(events)
