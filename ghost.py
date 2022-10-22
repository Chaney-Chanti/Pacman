import pygame as pg
from pygame.sprite import Sprite, Group


class Ghosts:
    def __init__(self, game, spawns):
        self.ghosts = Group()
        self.spawns = spawns
        self.game = game
        self.screen = self.game.screen
        self.blinky = Blinky(self.screen, self.spawns['Blinky'][0], self.spawns['Blinky'][1])
        self.clyde = Clyde(self.screen, self.spawns['Clyde'][0], self.spawns['Clyde'][1])
        self.inky = Inky(self.screen, self.spawns['Inky'][0], self.spawns['Inky'][1])
        self.ghosts.add(self.blinky)
        self.ghosts.add(self.clyde)
        self.ghosts.add(self.inky)
    
    def update(self):
        self.ghosts.update()
                    

class Ghost(pg.sprite.Sprite):
    def __init__(self, screen, x, y, image):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x * self.rect.width, y * self.rect.height
        self.screen = screen

        self.dying = self.dead = False
                        
        # add ghost animation here
        # self.timer_normal = Alien.alien_timers[type]              
        # self.timer_explosion = Timer(image_list=Alien.alien_explosion_images, is_loop=False)  
        # self.timer = self.timer_normal 

    def check_collisions_wall():
        pass

    def update(self):
        self.draw()
        return
        self.check_collisions_ghost()
        self.check_collisions_wall()

    def draw(self): 
        self.screen.blit(self.image, self.rect)
        
class Blinky(Ghost):
    def __init__(self, screen, x, y):
        image = 'assets/BlinkyR.png'
        Ghost.__init__(self, screen, x, y, image)
        
    def blinkyAI():
        pass

class Clyde(Ghost):
    def __init__(self, screen, x, y):
        image = 'assets/ClydeR.png'
        Ghost.__init__(self, screen, x, y, image)
        
    def clydeAI():
        pass

class Inky(Ghost):
    def __init__(self, screen, x, y):
        image = 'assets/InkyR.png'
        Ghost.__init__(self, screen, x, y, image)
        
    def inkyAI():
        pass