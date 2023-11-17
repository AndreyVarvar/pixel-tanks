import pygame as pg


class EventManager:
    def __init__(self):
        self.events = {}  # ?? idk, what _are_ events?

    def update(self) -> None:
        # get the events
        self.events = pg.event.get()
