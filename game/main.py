import pygame
from player import Player
from enemy import Enemy
from game import game
pygame.init()


print("Lancement du jeu")
print("Chargement des assets")

# Create the screen
pygame.display.set_caption("Galactic Annihilation: Alien Onslaught")
screen = pygame.display.set_mode((700, 1000))
screen_rect = screen.get_rect()
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# Définir la taille de la fenêtre
window_width = int(screen_width * 0.5)  # Par exemple, 80% de la largeur de l'écran
window_height = int(screen_height * 0.5)  # Par exemple, 80% de la hauteur de l'écran

running = True

#importer de charger l'arrière plan de notre jeu
background = pygame.image.load('assets/parallax-space-backgound-animx1.gif').convert()
background = pygame.transform.scale(background, (1080, 720))
background = pygame.transform.rotate(background, -90)

# Charger notre joueur
player = Player(300, 800)


#boucle tant que running est vrai
while running:
    #appliquer l'arrière plan de notre jeu
    screen.blit(background, (0, 0))


# Détecter le mouvement du joueur
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move(-1, 0)
    if keys[pygame.K_RIGHT]:
        player.move(player.velocity, 0)
    if keys[pygame.K_UP]:
        player.move(0, -1)
    if keys[pygame.K_DOWN]:
        player.move(0, player.velocity)

    # Garder le joueur dans l'écran
    player.rect.clamp_ip(screen_rect)

    # Dessiner le joueur
    screen.blit(player.image, player.rect)

    #appliquer l'ensemble des images de mon groupe d'enemy
    game.all_enemy.draw(screen)

#mettre à jour l'écran
    pygame.display.flip()

    #si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
            exit()
