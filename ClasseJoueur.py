import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.maxhealth = 100
        self.attack = 20
        self.velocity = 2.5
        self.image = pygame.image.load('assets/player.png')
        self.all_projectile = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 435
        self.rect.y = 500
        self.xmax = 0
        self.yinit = 500

    def move_right(self): 
        if not self.game.check_collision(self, self.game.all_monsters) and not self.game.check_collision(self, self.game.all_minimonsters):
            self.rect.x += 2

    def move_left(self): 
        self.rect.x -= 2

    def launch_projectile(self):
        self.all_projectile.add(Projectile(self, self.game))

    def damaged(self, amount):
        if self.health - amount >= 0:
            self.health -= amount

    def jump(self):
        if self.yinit - self.rect.y < 200:
            self.rect.y -= 10

    def health_bar(self, surface): 
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x+50, self.rect.y+20, self.maxhealth, 7]) # barre de vie de fond                              # définir une couleur de jauge, vert clair ici   # position de la jauge, largeur et épaisseur
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x+50, self.rect.y+20, self.health, 7]) # barre de vie actuel
