import pygame as pg
from pygame.sprite import Sprite, Group
import random


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
        #self.counter = 0
        
    def ghostAI(self, pacman):
        self.blinky.blinkyAI(pacman)
        if(pg.time.get_ticks() >= 3000):
            self.clyde.clydeAI(pacman)
        if(pg.time.get_ticks() >= 5000):
            self.inky.inkyAI(pacman)
        
    def update(self, pacman):
        if not any(type(obj) == Fruit for obj in self.ghosts.sprites()):
            if random.randrange(0, 1000) < 1:
                randSpawn = random.choice(self.spawns['Fruit'])
                fruit = Fruit(self.screen, randSpawn[0], randSpawn[1])
                self.ghosts.add(fruit)
        self.ghosts.update()
        self.ghostAI(pacman)
                    

class Ghost(pg.sprite.Sprite):
    def __init__(self, screen, x, y, image):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x * self.rect.width, y * self.rect.height
        self.rect.x = self.rect.left
        self.rect.y = self.rect.top
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
        
    def blinkyAI(self, pacman):
        if(pacman.rect.x > self.rect.x): #right
            self.rect.x += 1
            self.image = pg.image.load('assets/BlinkyR.png')
        if(pacman.rect.x < self.rect.x): #left
            self.rect.x -= 1
            self.image = pg.image.load('assets/BlinkyL.png')
        if(pacman.rect.y > self.rect.y): #down
            self.rect.y += 1
            self.image = pg.image.load('assets/BlinkyD.png')
        if(pacman.rect.y < self.rect.y): #up
            self.rect.y -= 1
            self.image = pg.image.load('assets/BlinkyUp.png')
    
class Clyde(Ghost):
    def __init__(self, screen, x, y):
        image = 'assets/ClydeR.png'
        Ghost.__init__(self, screen, x, y, image)
        
    def clydeAI(self, pacman):
        if(pacman.rect.x > self.rect.x): #right
            self.rect.x += 1
            self.image = pg.image.load('assets/ClydeR.png')
        if(pacman.rect.x < self.rect.x): #left
            self.rect.x -= 1
            self.image = pg.image.load('assets/ClydeL.png')
        if(pacman.rect.y > self.rect.y): #down
            self.rect.y += 1
            self.image = pg.image.load('assets/ClydeD.png')
        if(pacman.rect.y < self.rect.y): #up
            self.rect.y -= 1
            self.image = pg.image.load('assets/ClydeUp.png')

class Inky(Ghost):
    def __init__(self, screen, x, y):
        image = 'assets/InkyR.png'
        Ghost.__init__(self, screen, x, y, image)
        
    def inkyAI(self, pacman):
        if(pacman.rect.x > self.rect.x): #right
            self.rect.x += 1
            self.image = pg.image.load('assets/InkyR.png')
        if(pacman.rect.x < self.rect.x): #left
            self.rect.x -= 1
            self.image = pg.image.load('assets/InkyL.png')
        if(pacman.rect.y > self.rect.y): #down
            self.rect.y += 1
            self.image = pg.image.load('assets/InkyD.png')
        if(pacman.rect.y < self.rect.y): #up
            self.rect.y -= 1
            self.image = pg.image.load('assets/InkyUp.png')
            

class Fruit(Ghost):
    def __init__(self, screen, x, y):
        image = 'assets/cherry.png'
        Ghost.__init__(self, screen, x, y, image)