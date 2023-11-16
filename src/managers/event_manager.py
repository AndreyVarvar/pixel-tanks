import pygame as pg


class EventManager:
    def __init__(self):
        self.events = {}  # ?? idk, what _are_ events?

        # keys BABYYYY
        self.keys_states = {
            0: "released",
            1: "nothing",
            2: "pressed"
        }

        self.keys_change = {
            "state": self.keys_states[1],
            "key": None
        }

    def update(self) -> None:
        # get the events
        self.events = pg.event.get()