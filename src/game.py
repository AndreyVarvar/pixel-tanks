import pygame as pg
from src.managers.display_manager import DisplayManager


class Game:
    def __init__(self):
        self.dm = DisplayManager()

        self.running = True

    def run(self):
        while self.running:
            events = pg.event.get()

            self.handle_events(events)

    def handle_events(self, *args):
        events = args[0]

        for event in events:
            if event.type == pg.QUIT:
                self.running = False
