import pygame
import os
import random

#créer une classe qui va gérer la notion d'ennemi sur notre jeu

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        skins = ["enemie.png", "red enemie.png"]

        # Charger l'image du joueur
        self.image = pygame.image.load(os.path.join("assets", random.choice(skins)))
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()

        # Placer le joueur aux coordonnées (x, y)
        self.rect.x = x
        self.rect.y = y

        # Initialiser les statistiques de l'ennemi
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.last_move = 0
        self.last_movement = pygame.time.get_ticks()

        # Déterminer sa mort
        self.death_time = 0
        self.is_dead = False

    
    def move(self, gamespeed):
        # Déplacer l'ennemi
        moves = [1, -1]

        if self.last_move == 0:
            self.last_move = random.choice(moves)
        else:
            now = pygame.time.get_ticks()
            if now - self.last_movement > 500:
                self.last_movement = now
                self.last_move = random.choice(moves)
        
        self.rect.x += (self.last_move * gamespeed) / 2