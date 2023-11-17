import pygame as pg


class DisplayManager:
    def __init__(self):
        self.display = pg.display.set_mode((1000, 800))

        self.fps = 60
        self.clock = pg.time.Clock()
        self.dt = 0

        self.running = True

    def update(self):
        self.dt = self.clock.tick(self.fps)/1000

    def handle_events(self, events):
        for event in events:
            if event.type == pg.QUIT:
                self.running = False

    def clear_display(self):
        pg.display.update()
        self.display.fill("white")  # it's 9 o'clock, i don't know why i am adding this comment
