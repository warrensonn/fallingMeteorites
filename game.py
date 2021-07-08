from ClasseJoueur import Player
import pygame
from monster import Monster
from meteor import Meteor
from minimonster import MiniMonster

# GENERER DEUXIEME JOUEUR, SE BATTRE A DEUX POUR SURVIVRE
class Game:
    def __init__(self): 
        self.is_playing = False
        self.players = pygame.sprite.Group()        
        self.player = Player(self) 
        self.players.add(self.player)               # générer notre joueur    
        self.all_monsters = pygame.sprite.Group()   # groupe de monstres
        self.all_minimonsters = pygame.sprite.Group()
        self.all_meteors = pygame.sprite.Group()

        self.spawn_meteor()
        self.spawn_meteor()
        self.spawn_monster()
        self.spawn_monster()
        
        self.pressed = {}
        

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):       
        monster = Monster(self)
        self.all_monsters.add(monster)

    def spawn_meteor(self):
        meteor = Meteor(self)
        self.all_meteors.add(meteor)

    def spawn_minimonster(self):
        minimonster = MiniMonster(self)
        self.all_minimonsters.add(minimonster)

    def loosing(self):
        if self.player.health <=0:
            self.isplaying = False
    
    def update(self, screen):
        
        screen.blit(self.player.image, self.player.rect)    # appliquer l'image de mon joueur

        self.player.health_bar(screen)

        for meteor in self.all_meteors:
            self.all_meteors.draw(screen)
            meteor.fall()
    
        for projectile in self.player.all_projectile:
            projectile.move()

        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        for minimonster in self.all_minimonsters:
            minimonster.forward()
            minimonster.update_health_bar(screen)
    

        self.player.all_projectile.draw(screen)
        self.all_monsters.draw(screen)  
        self.all_minimonsters.draw(screen)

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < screen.get_width() - self.player.image.get_width() + 20:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > -20:
            self.player.move_left()