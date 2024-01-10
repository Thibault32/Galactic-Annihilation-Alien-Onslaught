import pygame
import os

class Button():
    def __init__(self, screen_width, screen_height, image, type):
        super().__init__()

        ratio = 1
        if type == "youtube":
            ratio = 0.3

        # Charger l'image du bouton
        self.image = image
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * ratio), int(self.image.get_height() * ratio)))
        self.rect = self.image.get_rect()

        # Placer les boutons aux coordonnées (x, y)
        self.rect.x = screen_width / 2 - self.rect.width / 2
        
        if type == "play":
            self.rect.y = screen_height / 2 - self.rect.height / 2
        elif type == "quit":
            self.rect.y = (screen_height / 2 - self.rect.height / 2) + 250
        elif type == "youtube":
            self.rect.y = screen_height - 100

        # Initialiser les valeurs du bouton
        self.clicked = False

    def draw(self, surface):
        action = False

        # Obtenir la position de la souris
        pos = pygame.mouse.get_pos()

        # Vérifier si la souris est sur le bouton et si le bouton est cliqué
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked

        # Dessiner le bouton sur l'écran
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action