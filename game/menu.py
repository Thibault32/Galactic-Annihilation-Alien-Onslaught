import os
pygame.force_init()

#game variables
game_paused = False

#définir la font
font = pygame.font.SysFont("arialblack", 40)

#définir la couleur des textes
text_color = (255, 255, 255)

def draw_text(text, font, text_color, x, y):
    #définir le texte
    img = font.render(text, True, text_color)
    #afficher le texte
    screen.blit(img, (x, y))