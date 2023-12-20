import pygame
pygame.init()
from player import Player

print("Lancement du jeu")
print("Chargement des assets")

# Create the screen
pygame.display.set_caption("Galactic Annihilation: Alien Onslaught")
screen = pygame.display.set_mode((700, 1000))

running = True

#importer de charger l'arrière plan de notre jeu
background = pygame.image.load('assets/parallax-space-backgound-animx1.gif').convert()
background = pygame.transform.scale(background, (1080, 720))
background = pygame.transform.rotate(background, -90)

# Charger notre joueur
player = Player(300, 500)

#boucle tant que running est vrai
while running:
    #appliquer l'arrière plan de notre jeu
    screen.blit(background, (0, 0))


# Détecter le mouvement du joueur
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move(-1, 0)
    if keys[pygame.K_RIGHT]:
        player.move(1, 0)
    if keys[pygame.K_UP]:
        player.move(0, -1)
    if keys[pygame.K_DOWN]:
        player.move(0, 1)

    # Dessiner le joueur
    screen.blit(player.image, player.rect) 


#mettre à jour l'écran
    pygame.display.flip()

    #si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
            exit()
