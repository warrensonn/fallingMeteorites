import pygame, random

class Meteor(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.velocity = 3
        self.attack = 15
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1000)
        self.rect.y = -300

    def remove(self):
        self.game.all_meteors.remove(self)
      
    def fall(self):
        if self.rect.y < 800 and not self.game.check_collision(self, self.game.players):
            self.rect.y += self.velocity
        # plutot mettre else: reninit(), if check_collision damage()
        else:
            if self.game.check_collision(self, self.game.players) and self.game.player.health >=0:
                self.game.player.health -= self.attack
            self.reinit()

    def reinit(self):
        self.rect.y = random.randint(-200, -50)
        self.rect.x = random.randint(0, 1000)
        self.velocity = random.randint(1, 4)
