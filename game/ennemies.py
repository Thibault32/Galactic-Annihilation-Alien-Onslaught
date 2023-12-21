import pygame
import random

# Initialisation de Pygame
pygame.init()

# Paramètres du jeu
largeur_fenetre = 800
hauteur_fenetre = 600
couleur_fond = (255, 255, 255)
fps = 60

# Paramètres du personnage principal
perso_couleur = (0, 128, 255)
perso_taille = 50
perso_x = largeur_fenetre // 2 - perso_taille // 2
perso_y = hauteur_fenetre - 2 * perso_taille

# Paramètres des ennemis
ennemi_couleur = (255, 0, 0)
ennemi_taille = 30
ennemi_vitesse = 5
nombre_ennemis_par_vague = 5
vitesse_apparition_ennemis = 1
temps_entre_vagues = 3

# Initialisation de la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Jeu Pygame - Ennemis attaquants")

# Horloge pour contrôler le nombre d'images par seconde
horloge = pygame.time.Clock()

# Fonction pour afficher le personnage principal
def afficher_personnage(x, y):
    pygame.draw.rect(fenetre, perso_couleur, [x, y, perso_taille, perso_taille])

# Fonction pour afficher un ennemi
def afficher_ennemi(x, y):
    pygame.draw.rect(fenetre, ennemi_couleur, [x, y, ennemi_taille, ennemi_taille])

# Boucle principale du jeu
running = True
vagues_ennemis = 0
temps_debut_vague = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Déplacement du personnage principal
    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT] and perso_x > 0:
        perso_x -= 5
    if touches[pygame.K_RIGHT] and perso_x < largeur_fenetre - perso_taille:
        perso_x += 5

    # Affichage du fond
    fenetre.fill(couleur_fond)

    # Affichage du personnage principal
    afficher_personnage(perso_x, perso_y)

    # Génération des vagues d'ennemis
    temps_actuel = pygame.time.get_ticks()
    temps_ecoule_vague = (temps_actuel - temps_debut_vague) / 1000

    if temps_ecoule_vague > temps_entre_vagues:
        if vagues_ennemis < 5:  # Limiter le nombre de vagues pour l'exemple
            for _ in range(nombre_ennemis_par_vague):
                ennemi_x = random.randint(0, largeur_fenetre - ennemi_taille)
                ennemi_y = random.randint(-100, -ennemi_taille)
                vagues_ennemis += 1

        temps_debut_vague = pygame.time.get_ticks()

    # Mouvement et affichage des ennemis
    for i in range(vagues_ennemis):
        ennemi_y += ennemi_vitesse
        afficher_ennemi(ennemi_x, ennemi_y)

        # Gestion des collisions avec le personnage principal
        if (
            perso_x < ennemi_x < perso_x + perso_taille
            and perso_y < ennemi_y < perso_y + perso_taille
        ):
            print("Collision avec un ennemi!")
            # Vous pouvez ajouter ici la logique de gestion de la collision, par exemple, réduire la vie du joueur.

    pygame.display.flip()

    # Contrôle des images par seconde
    horloge.tick(fps)

# Quitter Pygame
pygame.quit()
