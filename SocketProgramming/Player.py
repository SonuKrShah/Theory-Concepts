import pygame


class Player:
    # Initializing the charcter
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.vel = 5
        self.width = width
        self.height = height
        self.color = color
        self.rect = (self.x, self.y, self.width, self.height)
        # In the future instead of the rect, I can use the image and then draw it onto the screen

    def Update_Rect(self):
        self.rect = (self.x, self.y, self.width, self.height)
        pass

    def draw(self, WIN):
        pygame.draw.rect(WIN, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
            self.Update_Rect()
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
            self.Update_Rect()
        if keys[pygame.K_UP]:
            self.y -= self.vel
            self.Update_Rect()
        if keys[pygame.K_DOWN]:
            self.y += self.vel
            self.Update_Rect()
