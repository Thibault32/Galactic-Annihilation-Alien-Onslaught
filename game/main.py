import pygame
import random
import os
from player import Player
from enemy import Enemy
from projectile import Projectile
from buttons import Button

pygame.init()
pygame.font.init()

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

# Importer de charger l'arrière plan de notre jeu
background = pygame.image.load('assets/parallax-space-backgound-animx1.gif').convert()
background = pygame.transform.scale(background, (1080, 720))
background = pygame.transform.rotate(background, -90)

# Charger l'image des boutons
play_img = pygame.image.load('assets/play_btn.png').convert_alpha()
quit_img = pygame.image.load('assets/quit_btn.png').convert_alpha()
youtube_img = pygame.image.load('assets/youtube.png').convert_alpha()

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

# Charger la musique
pygame.mixer.init()
pygame.mixer.music.load(os.path.join("assets", "musique.mp3"))
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

# Charge le son de tir
shoot_sound = pygame.mixer.Sound(os.path.join("assets", "tir.mp3"))

# Valeurs de jeu
paused = False
main_menu = True
game_over = False
running = True

# Boucle tant que running est vrai
while running:
    # Mettre le jeu à une framerate fixe
    gamespeed = pygame.time.Clock().tick(60)

    # Appliquer l'arrière plan de notre jeu
    screen.blit(background, (0, 0))
    
    # Vérifier si le jeu est en pause
    if main_menu == True: 
        # Charger la police
        font = pygame.font.Font("assets/font.ttf", 60)

        for event in pygame.event.get():
            # Quitter le jeu
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("Fermeture du jeu")
                exit()

        # Appliquer l'arrière plan de notre jeu
        screen.blit(background, (0, 0))

        # Ecrire pause
        pause_text = font.render("MAIN MENU", 1, (255, 255, 255))
        screen.blit(pause_text, ((screen_width / 2) - (pause_text.get_width() / 2), screen_height / 5))

        # Dessiner les boutons
        play_button = Button(screen_width, screen_height, play_img, "play")
        quit_button = Button(screen_width, screen_height, quit_img, "quit")
        youtube_button = Button(screen_width, screen_height, youtube_img, "youtube")

        play_state = play_button.draw(screen)
        quit_state = quit_button.draw(screen)
        youtube_state = youtube_button.draw(screen)

        # Vérifier si le joueur a cliqué sur le bouton play
        if play_state:
            main_menu = False
        # Vérifier si le joueur a cliqué sur le bouton quit
        if quit_state:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
            exit()
        # Vérifier si le joueur a cliqué sur le bouton youtube
        if youtube_state:
            os.system("start https://www.youtube.com/watch?v=dQw4w9WgXcQ")

        # Mettre à jour l'écran
        pygame.display.flip()
    elif game_over == True:
        # Charger la police
        font = pygame.font.Font("assets/font.ttf", 60)

        for event in pygame.event.get():
            # Quitter le jeu
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("Fermeture du jeu")
                exit()

        # Appliquer l'arrière plan de notre jeu
        screen.blit(background, (0, 0))

        # Ecrire pause
        pause_text = font.render("GAME OVER", 1, (255, 255, 255))
        screen.blit(pause_text, ((screen_width / 2) - (pause_text.get_width() / 2), screen_height / 5))

        # Ecrire le score
        font = pygame.font.Font("assets/font.ttf", 30)
        score_text = font.render("Score: " + str(score), 1, (255, 255, 255))
        screen.blit(score_text, ((screen_width / 2) - (score_text.get_width() / 2), screen_height / 5 + 150))

        # Dessiner les boutons
        play_button = Button(screen_width, screen_height, play_img, "play")
        quit_button = Button(screen_width, screen_height, quit_img, "quit")

        play_state = play_button.draw(screen)
        quit_state = quit_button.draw(screen)

        # Vérifier si le joueur a cliqué sur le bouton play
        if play_state:
            game_over = False
            # Réinitialiser le jeu
            player.kill()
            player = Player(300, 800)
            score = 0
        # Vérifier si le joueur a cliqué sur le bouton quit
        if quit_state:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
            exit()

        # Mettre à jour l'écran
        pygame.display.flip()
    elif paused == True:
        # Charger la police
        font = pygame.font.Font("assets/font.ttf", 60)

        for event in pygame.event.get():
            # Enlever le mode pause
            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                paused = False
            # Quitter le jeu
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("Fermeture du jeu")
                exit()

        # Appliquer l'arrière plan de notre jeu
        screen.blit(background, (0, 0))

        # Ecrire pause
        pause_text = font.render("PAUSE", 1, (255, 255, 255))
        screen.blit(pause_text, ((screen_width / 2) - (pause_text.get_width() / 2), screen_height / 5))

        # Ecrire les instructions
        font = pygame.font.Font("assets/font.ttf", 15)
        instructions_text = font.render("Appuyez sur ECHAP pour continuer", 1, (255, 255, 255))
        screen.blit(instructions_text, ((screen_width / 2) - (instructions_text.get_width() / 2), screen_height / 2))

        # Dessiner les boutons
        quit_button = Button(screen_width, screen_height, quit_img, "quit")

        quit_state = quit_button.draw(screen)

        # Vérifier si le joueur a cliqué sur le bouton quit
        if quit_state:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
            exit()

        # Mettre à jour l'écran
        pygame.display.flip()
    else:
        # Charger la police
        font = pygame.font.Font("assets/font.ttf", 15)

        for event in pygame.event.get():
            # Activer le mode pause
            if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                paused = True
            # Quitter le jeu
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("Fermeture du jeu")
                exit()

        # Afficher le score
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
            projectiles.append(Projectile(player.rect.x + 50, player.rect.y, "projectile", player.attack))
            shoot_sound.set_volume(random.choice([0.1, 0.2, 0.3, 0.4, 0.5]))
            shoot_sound.play()
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
                        if player.health < player.max_health:
                            player.health += 25
                            if player.health > player.max_health:
                                player.health = player.max_health

                        death_sound_effect = random.choice([os.path.join("assets", "mort.mp3"), os.path.join("assets", "mort2.mp3")])
                        death_sound = pygame.mixer.Sound(death_sound_effect)
                        if death_sound_effect == os.path.join("assets", "mort.mp3"):
                            death_sound.set_volume(0.2)
                        else:
                            death_sound.set_volume(0.5)
                        death_sound.play()

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
                # Faire bouger l'ennemi aléatoirement à gauche ou à droite
                enemy.move(gamespeed)
                screen.blit(enemy.image, enemy.rect)
                enemy.rect.clamp_ip(screen_rect)

                # Dessiner la barre de vie de l'ennemi
                pygame.draw.rect(screen, (60, 63, 60), [(enemy.rect.x + 50) - (enemy.max_health / 2), enemy.rect.y - 20, enemy.max_health, 5])
                pygame.draw.rect(screen, (255, 46, 46), [(enemy.rect.x + 50) - (enemy.max_health / 2), enemy.rect.y - 20, enemy.health, 5])

        # Gestion des projectiles ennemis
        for enemy in all_enemies:
            if not enemy.is_dead:
                now = pygame.time.get_ticks()
                if now - enemy.last_shot > enemy.attack_speed:
                    if random.choice([True, False]):
                        enemy_projectiles.append(Projectile(enemy.rect.x + 50, enemy.rect.y + 100, "enemy_projectile", enemy.attack))
                        shoot_sound.set_volume(random.choice([0.1, 0.2, 0.3, 0.4, 0.5]))
                        shoot_sound.play()
                    enemy.last_shot = now

        for projectile in enemy_projectiles:
            projectile.move(gamespeed)
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

                # Vérifier si le joueur est mort
                if player.health <= 0:
                    player.image = pygame.image.load(os.path.join("assets", "death.png"))
                    player.image = pygame.transform.scale(player.image, (100, 100))
                    screen.blit(player.image, player.rect)
                    
                    death_sound_effect = random.choice([os.path.join("assets", "mort.mp3"), os.path.join("assets", "mort2.mp3")])
                    death_sound = pygame.mixer.Sound(death_sound_effect)
                    if death_sound_effect == os.path.join("assets", "mort.mp3"):
                        death_sound.set_volume(0.2)
                    else:
                        death_sound.set_volume(5)
                    death_sound.play()

                    all_enemies.clear()
                    projectiles.clear()
                    enemy_projectiles.clear()
                    
                    game_over = True

        # Mettre à jour l'écran
        pygame.display.flip()