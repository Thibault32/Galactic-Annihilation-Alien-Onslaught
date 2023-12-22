import pygame
import os
import random

#créer une classe qui va gérer la notion d'ennemi sur notre jeu

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load(os.path.join("assets", "enemie.png"))
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image = pygame.transform.rotate(self.image, 180)
        
