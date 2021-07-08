import pygame

class Projectile(pygame.sprite.Sprite):

    def __init__(self, player, game):
        super().__init__()
        self.velocity = 3
        self.player = player
        self.game = game
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 150
        self.rect.y = player.rect.y + 90
        self.origin_image = self.image
        self.angle = 0
        self.xinitial = player.rect.x + 150

    def rotate(self):
        self.angle += 10
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center) 

    def remove(self):
            self.player.all_projectile.remove(self)
    
    def move(self):
        # if self.rect.xinit - self.rect.x < 500:
        self.rect.x += self.velocity
        self.rotate()
        for monster in self.game.check_collision(self, self.player.game.all_monsters):
            monster.damage(self.player.attack)
            self.remove()

        if self.rect.x >1080 or self.rect.x - self.xinitial > 500: 
            self.remove()



    
