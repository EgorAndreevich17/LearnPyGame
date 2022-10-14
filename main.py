import pygame, sys

pygame.init()
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption('Test Game')
# screen.fill('#FB607F')
clock = pygame.time.Clock()

background_surface = pygame.image.load('graphics/background.png')
grass_surface = pygame.image.load('graphics/grass.png')

while True:
    pygame.display.update()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    #screen.blit(grass_surface,(0,0))
    screen.blit(background_surface,(0,0))
    screen.blit(grass_surface,(0,0))
    clock.tick(60)