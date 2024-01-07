import pygame
import random
import os
from player import Player
from enemy import Enemy
from projectile import Projectile
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

# Projectiles
projectiles = []
enemy_projectiles = []

# Groupe d'ennemis
all_enemies = []

# Charger notre score
score = 0
score_increment = 10 # modifier cette variable si le joueur a un multiplicateur de score

#boucle tant que running est vrai
while running:
    # Mettre le jeu à une framerate fixe
    gamespeed = pygame.time.Clock().tick(60)

    #appliquer l'arrière plan de notre jeu
    screen.blit(background, (0, 0))

    # Afficher le score
    font = pygame.font.Font("assets/font.ttf", 15)
    score_text = font.render("Score: " + str(score), 1, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Détecter le mouvement du joueur
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move(-1 * player.velocity * gamespeed, 0)
    if keys[pygame.K_RIGHT]:
        player.move(1 * player.velocity * gamespeed, 0)

    # Garder le joueur dans l'écran
    player.rect.clamp_ip(screen_rect)

    # Dessiner le joueur
    screen.blit(player.image, player.rect)

    # Dessiner la barre de vie du joueur
    pygame.draw.rect(screen, (60, 63, 60), [(player.rect.x + 50) - (player.max_health / 2), player.rect.y + 120, player.max_health, 5])
    pygame.draw.rect(screen, (111, 210, 46), [(player.rect.x + 50) - (player.max_health / 2), player.rect.y + 120, player.health, 5])

    # Tirer un projectile
    if keys[pygame.K_SPACE] and not player.is_shooting:
        projectiles.append(Projectile(player.rect.x + 50, player.rect.y, "projectile"))
        player.is_shooting = True
    
    # Gestion du cooldown de tir
    if player.is_shooting:
        now = pygame.time.get_ticks()
        if now - player.last_shot > player.shooting_speed:
            player.last_shot = now
            player.is_shooting = False

    # Gestion des projectiles
    for projectile in projectiles:
        projectile.move(-1 * gamespeed)
        screen.blit(projectile.image, projectile.rect)

        # Supprimer le projectile s'il sort de l'écran
        if projectile.rect.x < 0:
            projectile.kill()
            projectiles.remove(projectile)
        
        # Vérifier si le projectile touche un ennemi
        for enemy in all_enemies:
            if projectile.rect.colliderect(enemy.rect) and not enemy.is_dead:
                enemy.health -= projectile.damage
                projectile.kill()
                projectiles.remove(projectile)

                # Vérifier si l'ennemi est mort
                if enemy.health <= 0 and not enemy.is_dead:
                    enemy.image = pygame.image.load(os.path.join("assets", "death.png"))
                    enemy.image = pygame.transform.scale(enemy.image, (100, 100))
                    screen.blit(enemy.image, enemy.rect)
                    enemy.death_time = pygame.time.get_ticks()
                    enemy.is_dead = True
                    score += score_increment

    # Gestion des ennemis
    if len(all_enemies) == 0:
        all_enemies.append(Enemy(300, 100))

    for enemy in all_enemies:
        if enemy.is_dead:
            screen.blit(enemy.image, enemy.rect)
            now = pygame.time.get_ticks()
            if now - enemy.death_time > 500:
                enemy.kill()
                all_enemies.remove(enemy)
        else:
            enemy.move(gamespeed)
            screen.blit(enemy.image, enemy.rect)
            enemy.rect.clamp_ip(screen_rect)

    # Gestion des projectiles ennemis
    for enemy in all_enemies:
        if not enemy.is_dead:
            now = pygame.time.get_ticks()
            if now - enemy.last_shot > 250:
                if random.choice([True, False]):
                    enemy_projectiles.append(Projectile(enemy.rect.x + 50, enemy.rect.y + 100, "enemy_projectile"))
                enemy.last_shot = now
    
    for projectile in enemy_projectiles:
        projectile.move(1 * gamespeed)
        screen.blit(projectile.image, projectile.rect)

        # Supprimer le projectile s'il sort de l'écran
        if projectile.rect.x < 0:
            projectile.kill()
            enemy_projectiles.remove(projectile)
        
        # Vérifier si le projectile touche le joueur
        if projectile.rect.colliderect(player.rect):
            player.health -= projectile.damage
            projectile.kill()
            enemy_projectiles.remove(projectile)

    #appliquer l'ensemble des images de mon groupe d'enemy
    #game.all_enemy.draw(screen)

    #mettre à jour l'écran
    pygame.display.flip()

    #si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
            exit()