import pygame, sys

class Game:
    def __init__(self):

        #general group
        pygame.init()
        self.screen = pygame.display.set_mode((1024, 768))
        pygame.display.set_caption('Test Game')
        self.clock = pygame.time.Clock()
    def run(self):
        background_surface = pygame.image.load('graphics/background.png')
        grass_surface = pygame.image.load('graphics/grass.png')
        while True:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.blit(background_surface, (0, 0))
            self.screen.blit(grass_surface, (0, 0))
            self.clock.tick(60)


if __name__=="__main__":
    game = Game()
    game.run()

