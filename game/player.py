import pygame
import os

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # Charger l'image du joueur
        self.image = pygame.image.load(os.path.join("assets", "player.png"))
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()

        # Placer le joueur aux coordonnées (x, y)
        self.rect.x = x
        self.rect.y = y

        # Initialiser les statistiques du joueur
        self.velocity = 1
        self.health = 100
        self.max_health = 100
        self.shooting_speed = 250

        self.is_shooting = False
        self.last_shot = pygame.time.get_ticks()

    def move(self, dx, dy):
        # Déplacer le joueur avec les valeurs (dx, dy)
        self.rect.x += dx
        self.rect.y += dy
