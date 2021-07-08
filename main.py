import pygame
from game import Game

pygame.init()

# on charge les images de fond
background = pygame.image.load('assets/bg.jpg')
background2 = pygame.image.load('assets/button.png')

pygame.display.set_caption('Dead Comet Falling')
screen = pygame.display.set_mode((1080, 720))

game = Game()
running = True
saut = False
game.is_playing = True

while running:  
    screen.blit(background, (0, -200))          # on injecte l'image sur l'écran    
 

    if game.is_playing:
        game.update(screen)

    game.loosing()

    if game.is_playing == False:
        running = False

    pygame.display.flip()                       # on met à jour la fenêtre
    
    for event in pygame.event.get():            # tous les évènements du joueur 

        if event.type == pygame.KEYDOWN:        # si le joueur utilise une touche du clavier
            game.pressed[event.key] = True
            if event.key == pygame.K_SPACE:     # si le joueur clique sur espace
                game.player.launch_projectile()
            
        elif event.type == pygame.KEYUP:        # Lorsque le joueur lache une touche
            game.pressed[event.key] = False

        elif event.type == pygame.QUIT:         # si le joueur veut quitter
            running = False
            pygame.quit()

