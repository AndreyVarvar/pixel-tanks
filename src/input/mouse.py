import pygame as pg


class Mouse:
    def __init__(self):
        self.mouse_pos = (0, 0)
        self.mouse_pressed = []

        self.buttons = "left", "scroll-wheel", "right"
        self.left = 0
        self.scroll_wheel = 1
        self.right = 2

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

    def handle_events(self, events) -> None:
        # first, make sure the press state and everythign else is reset

        for event in events:
            # mouse has changed its position, record the cahnge
            if event.type == pg.MOUSEMOTION:
                self.mouse_change["move state"] = self.mouse_pos_states[self.moved]
                self.mouse_change["pos change"] = event.rel

            # mouse was just pressed, record it
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.mouse_change["press state"] = self.mouse_press_states[self.pressed]
                self.mouse_change["key"] = event.button

                # whatever button was pressed, add it to the 'pressed_buttons' variable or whatever it is called
                if event.button == 0:
                    button_pressed = self.left
                elif event.button == 1:
                    button_pressed = self.scroll_wheel
                else:
                    button_pressed = self.right

                self.mouse_pressed.append(self.buttons[button_pressed])

            # MOM BRING THE CAMERA, THE KEY ON THE MOUSE WAS JUST RELEASED
            elif event.type == pg.MOUSEBUTTONUP:
                self.mouse_change["press state"] = self.mouse_press_states[self.released]
                self.mouse_change["key"] = None

                # whatever button was released, remove it from the list
                if event.button == 0:
                    button_released = self.left
                elif event.button == 1:
                    button_released = self.scroll_wheel
                else:
                    button_released = self.right

                self.mouse_pressed.remove(self.buttons[button_released])

    def reset(self):
        self.mouse_pos = pg.mouse.get_pos()

        self.mouse_change["press state"] = self.mouse_press_states[self.nothing]
        self.mouse_change["key"] = None

        self.mouse_change["move state"] = self.mouse_pos_states[self.idle]
        self.mouse_change["pos change"] = (0, 0)

    @staticmethod
    def hide():
        pg.mouse.set_visible(False)

    @staticmethod
    def show():
        pg.mouse.set_visible(True)

    @staticmethod
    def lock(pos=(100, 100)):
        pg.mouse.set_pos(pos)
