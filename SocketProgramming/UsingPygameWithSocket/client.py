import pygame
from Network import Network

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


class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def UpdateRect(self):
        self.rect = (self.x, self.y, self.width, self.height)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel
        self.UpdateRect()


def read_pos(data):
    print(type(data), data)
    data = data.split(",")
    return int(data[0]), int(data[1])
    # return 50, 50


def make_pos(tup):
    return str(tup[0]) + ","+str(tup[1])


def redrawWindow(WIN, player, player2):
    WIN.fill(WHITE)
    player.draw(WIN)
    player2.draw(WIN)
    pygame.display.update()


def main():
    run = True
    n = Network()
    startPos = read_pos(n.get_pos())
    p = Player(startPos[0], startPos[1], 50, 50, RED)
    p2 = Player(0, 0, 50, 50, GREEN)
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        print("Position is ", make_pos((p.x, p.y)))
        p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
        print(p2Pos)
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.UpdateRect()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        p.move()
        redrawWindow(WIN, p, p2)
    pygame.quit()


main()
