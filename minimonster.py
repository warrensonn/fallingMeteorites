 #demander comment avoir aide module avec import au lieu de from import 
import pygame, random

class MiniMonster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.maxhealth = 100
        self.attack = 1
        self.velocity = random.randint(1, 3)
        self.image = pygame.image.load('assets/mummy.png')
        self.image = pygame.transform.scale(self.image, (100, 80))
        self.rect = self.image.get_rect()
        self.rect.x = 950 + random.randint(0, 100)
        self.rect.y = 590 

    def forward(self):
        if not self.game.check_collision(self, self.game.players):
            self.rect.x -= self.velocity
        elif self.game.check_collision(self, self.game.players):
            self.game.player.damaged(self.attack)

    def damage(self, amount):
        self.health -= amount
        if self.health <=0:
            self.rect.x = 950 + random.randint(0, 100)
            self.health = self.maxhealth
            self.velocity = random.randint(1, 4)

    def check_death(self):
        if self.health <=0:
            self.game.all_minimonsters.remove(self)
    










    def update_health_bar(self, surface):   # définir une couleur de jauge, position, largeur et épaisseur     
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x+25, self.rect.y-10, self.maxhealth, 3]) # barre de fond
        pygame.draw.rect(surface, (255, 0, 200), [self.rect.x+25, self.rect.y-10, self.health, 3])  # barre de vie actuel