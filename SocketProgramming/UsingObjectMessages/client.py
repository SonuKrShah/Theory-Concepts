import pygame
from Network import Network
from Player import Player

# Setting up the pygame window.

# Variables and Values.
WIDTH = 600
HEIGHT = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


# Setting the window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sonu Kr Shah")

clientNumber = 0


def redrawWindow(WIN, player, player2):
    WIN.fill(WHITE)
    player.draw(WIN)
    player2.draw(WIN)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.get_p()
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        p2 = n.send(p)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        p.move()
        redrawWindow(WIN, p, p2)
    pygame.quit()


main()
