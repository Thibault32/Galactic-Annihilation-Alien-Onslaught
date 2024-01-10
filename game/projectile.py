import pygame
import os

clock = pygame.time.Clock()

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, type, attack):
        super().__init__()

        # Charger l'image du projectile
        self.image = pygame.image.load(os.path.join("assets", type + ".png"))
        self.image = pygame.transform.scale(self.image, (15, 25))
        self.rect = self.image.get_rect()

        # Placer le projectile aux coordonnées (x, y)
        self.rect.x = x
        self.rect.y = y

        # Initialiser les statistiques du projectile
        self.velocity = 1
        self.damage = attack

    def move(self, direction):
        # Déplacer le projetile dans la direction specifiée
        self.rect.y += direction

    def kill(self):
        # Supprimer le projectile
        super().kill()
