import pygame
from pygame import constants
import ConstantVariables as C
from Player import Player

WIN = pygame.display.set_mode((C.WIDTH, C.HEIGHT))
pygame.display.set_caption("Ship Wars")


def draw_window(LPlayer, RPlayer):
    WIN.fill(C.WHITE)
    LPlayer.draw(WIN)
    RPlayer.draw(WIN)
    pygame.display.update()


def main():
    # Creating a player
    Left_Player = Player(100, 100, 50, 50, C.BLACK)
    Right_Player = Player(200, 400, 50, 50, C.GREEN)

    C.run = True
    clock = pygame.time.Clock()
    # print("Hello World")
    while C.run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                C.run = False
        Left_Player.move()
        Right_Player.move()
        draw_window(Left_Player, Right_Player)
    pygame.quit()
    pass


main()
