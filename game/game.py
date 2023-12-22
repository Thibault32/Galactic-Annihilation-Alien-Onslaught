import pygame
from player import Player
from enemy import Enemy

class game:
    def __init__(self):
        
        # Générer notre joueur
        self.player = Player(self)
        
        #groupe d'enemy
        self.all_enemy = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_enemy()

    def spawn_enemy(self):
       enemy = Enemy(300, 100)
       self.all_enemy.add(enemy)



