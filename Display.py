import pygame
from Sim import sim
import sys
import json

class display:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 600, 600
        self.DISPLAY_FACTOR = 30
        self.screen = pygame.display.set_mode(
            (self.WIDTH, self.HEIGHT)
        )
        pygame.display.set_caption("Ecosystem Simulation")
        self.clock = pygame.time.Clock()
        self.FPS = 2

        self.WHITE = (255, 255, 255)
        self.BLUE = (0, 0, 255)
        self.RED = (255, 0, 0)
        self.BLACK = (0, 0, 0)

        with open("data.json") as f:
            self.data = json.load(f)

    def draw_animals(self, info):
        for animal in info:
            x = animal["x"] * self.DISPLAY_FACTOR
            y = animal["y"] * self.DISPLAY_FACTOR
            pygame.draw.rect(self.screen, self.RED, (x, y, self.DISPLAY_FACTOR, self.DISPLAY_FACTOR))
            pygame.draw.rect(self.screen, self.BLACK, (x, y, self.DISPLAY_FACTOR, self.DISPLAY_FACTOR), 1)

    def draw_food(self, foods):
        for food in foods:
            x = food["x"] * self.DISPLAY_FACTOR
            y = food["y"] * self.DISPLAY_FACTOR
            pygame.draw.rect(self.screen, self.BLUE, (x, y, self.DISPLAY_FACTOR, self.DISPLAY_FACTOR))


    def run(self):
        loop = 0
        while loop < len(self.data):
            data = self.data[loop]
            self.clock.tick(self.FPS)

            #Check and handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.q:
                        sys.exit()

                    #Pause the display
                    # if event.key == pygame.p:
                    #     while True:
                    #         for event in pygame.event.get():
                    #             if event.type == pygame.QUIT:
                    #                 sys.exit()
                    #             if event.type == pygame.KEYDOWN:
                    #                 if event.key == pygame.q:
                    #                     sys.exit()
                    #                 if event.key == pygame.p:
                    #                     break

            self.screen.fill(self.WHITE)
            ###Draw Items###
            self.draw_food(data["food_data"])
            self.draw_animals(data["animals"]["info"])

            pygame.display.flip()
            loop += 1

if __name__ == '__main__':
    d = display()
    d.run()
