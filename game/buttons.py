import pygame
import os

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame_transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
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

#créer bouton instances
play_button = Button(100, 200, play_img, 0.5)
settings_button = Button(100, 400, settings_img, 0.5)
quit_button = Button(100, 600, quit_img, 0.5)