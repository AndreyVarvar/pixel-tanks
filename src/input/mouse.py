import pygame as pg


class Mouse:
    def __init__(self):
        self.last_event = None

        # uhh, i don't want to explain all of thiisss
        self.mouse_press_states = {
            0: "released",
            1: "nothing",
            2: "pressed"
        }

        self.mouse_pos_states = {
            0: "idle",
            1: "moved"
        }

        self.released = 0
        self.nothing = 1
        self.pressed = 2

        self.idle = 0
        self.moved = 1

        self.mouse_change = {
            "press state": self.mouse_press_states[self.nothing],
            "key": None,  # this changes in case "press change" is non-neutral ("released" or "pressed")
            "move state": self.mouse_pos_states[self.idle],
            "pos change": (0, 0)
        }

    def update(self, event_manager) -> None:
        events = event_manager.events

        # if previous mouse changes were not cleared, clear them
        if self.mouse_change["press state"] != self.mouse_press_states[self.nothing]:
            self.mouse_change["press state"] = self.mouse_press_states[self.nothing]
            self.mouse_change["key"] = None


        if self.mouse_change["move state"] != self.mouse_pos_states[self.idle]:
            self.mouse_change["move state"] = self.mouse_pos_states[self.idle]
            self.mouse_change["pos change"] = (0, 0)

        for event in events:
            if event.type == pg.MOUSEMOTION:
                self.mouse_change["move state"] = self.mouse_pos_states[self.moved]
                print(event)
