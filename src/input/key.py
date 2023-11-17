import pygame as pg


class Keys:
    def __init__(self):
        self.keys_pressed = []
        self.focused = False

        self.keys_states = {
            0: "released",
            1: "nothing",
            2: "pressed"
        }

        self.released = 0
        self.nothing = 1
        self.pressed = 2

        self.keys_state = {
            "press state": self.keys_states[self.nothing],
            "key": None
        }

    def update(self):
        self.focused = pg.key.get_focused()

    def handle_events(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                self.keys_state["press state"] = self.keys_states[self.pressed]
                self.keys_state["key"] = event.key
                self.keys_pressed.append(event.key)

            elif event.type == pg.KEYUP:
                self.keys_state["press state"] = self.keys_states[self.pressed]
                self.keys_state["key"] = None
                self.keys_pressed.remove(event.key)
