import pygame as pg
from pygame.sprite import Sprite, Group
import random
import time

class Ghosts:
    def __init__(self, game, spawns):
        self.ghosts = Group()
        self.spawns = spawns
        self.game = game
        self.screen = self.game.screen
        self.blinky = Blinky(self.game, self.spawns['Blinky'][0], self.spawns['Blinky'][1])
        self.clyde = Clyde(self.game, self.spawns['Clyde'][0], self.spawns['Clyde'][1])
        self.inky = Inky(self.game, self.spawns['Inky'][0], self.spawns['Inky'][1])
        self.pinky = Pinky(self.game, self.spawns['Pinky'][0], self.spawns['Pinky'][1])
        self.ghosts.add(self.blinky)
        self.ghosts.add(self.clyde)
        self.ghosts.add(self.inky)
        self.ghosts.add(self.pinky)
        #self.counter = 0
        
    def ghostAI(self, pacman):
        self.blinky.blinkyAI(pacman)
        if(pg.time.get_ticks() >= 3000): # delay
            self.clyde.clydeAI(pacman)
        if(pg.time.get_ticks() >= 5000):
            self.inky.inkyAI(pacman)
        if(pg.time.get_ticks() >= 7000):
            self.pinky.pinkyAI(pacman)
        
    def reset(self):
        self.blinky.x, self.blinky.y = self.spawns['Blinky'][0], self.spawns['Blinky'][1]
        self.clyde.x, self.clyde.y = self.spawns['Clyde'][0], self.spawns['Clyde'][1]
        self.inky.x, self.inky.y = self.spawns['Inky'][0], self.spawns['Inky'][1]

    def update(self, pacman):
        if not any(type(obj) == Fruit for obj in self.ghosts.sprites()):
            if random.randrange(0, 1000) < 1:
                randSpawn = random.choice(self.spawns['Fruit'])
                self.fruit = Fruit(self.game, randSpawn[0], randSpawn[1])
                self.ghosts.add(self.fruit)
        else:
            self.fruit.fruitAI()
        self.ghosts.update()
        self.ghostAI(pacman)
                    

class Ghost(pg.sprite.Sprite):
    def __init__(self, game, x, y, image):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(image)
        self.game = game
        self.rect = self.image.get_rect()
        self.x, self.y = x, y
        self.rect.left, self.rect.top = x * self.rect.width, y * self.rect.height
        self.rect.x = self.rect.left
        self.rect.y = self.rect.top
        self.screen = self.game.screen

        self.dying = self.dead = False
                        
        # add ghost animation here
        # self.timer_normal = Alien.alien_timers[type]              
        # self.timer_explosion = Timer(image_list=Alien.alien_explosion_images, is_loop=False)  
        # self.timer = self.timer_normal 


    def check_collisions_wall(self):
        collisions = pg.sprite.spritecollide(self, self.game.map.walls, False)
        screen_rect = self.screen.get_rect()
        if collisions:
            return True
        elif self.rect.right >= self.rect.width * len(max(self.game.map.game_map, key=len)) or self.rect.left <= 0:
            return True
        else:
            return False
    
    def moves(self, ghost):
        moves = ['up', 'down', 'left', 'right']
        print(ghost.y, ghost.x)
        if self.game.map.game_map[ghost.y][ghost.x - 1] == '#': #left
            moves.remove('left')
        if self.game.map.game_map[ghost.y][ghost.x + 1] == '#': #right
            moves.remove('right')
        if self.game.map.game_map[ghost.y - 1][ghost.x] == '#': #up
            moves.remove('up')
        if self.game.map.game_map[ghost.y + 1][ghost.x] == '#': #down
            moves.remove('down')
        return moves

    def fruitAI(self):
        if random.randrange(0, 1000) < 1:
            self.rand = random.randint(0, 3)
        if self.rand == 0: #right
            self.rect.x += 1
            if self.check_collisions_wall():
                self.rect.x -= 1
                self.rand = random.randint(0,3)
        if self.rand == 1: #left
            self.rect.x -= 1
            if self.check_collisions_wall():
                self.rect.x += 1 
                self.rand = random.randint(0,3)
        if self.rand == 2: #down
            self.rect.y += 1
            if self.check_collisions_wall():
                self.rect.y -= 1
                self.rand = random.randint(0,3)
        if self.rand == 3: #up
            self.rect.y -= 1
            if self.check_collisions_wall():
                self.rect.y += 1
                self.rand = random.randint(0,3)

    def update(self):
        self.draw()

    def draw(self): 
        self.screen.blit(self.image, self.rect)
        
class Blinky(Ghost):
    def __init__(self, game, x, y):
        image = 'assets/BlinkyR.png'
        Ghost.__init__(self, game, x, y, image)
        self.rand = random.randint(0, 3)
        
    def blinkyAI(self, pacman):
        if random.randrange(0, 500) < 1:
            self.rand = random.randint(0, 3)
        if self.rand == 0: #right
            self.rect.x += 1
            if self.check_collisions_wall():
                self.rect.x -= 1
                self.rand = random.randint(0,3)
            self.image = pg.image.load('assets/ClydeR.png')
        if self.rand == 1: #left
            self.rect.x -= 1
            if self.check_collisions_wall():
                self.rect.x += 1
                self.rand = random.randint(0,3)
                self.image = pg.image.load('assets/ClydeL.png')
        if self.rand == 2: #down
            self.rect.y += 1
            if self.check_collisions_wall():
                self.rect.y -= 1
                self.rand = random.randint(0,3)
            self.image = pg.image.load('assets/ClydeD.png')
        if self.rand == 3: #up
            self.rect.y -= 1
            if self.check_collisions_wall():
                self.rect.y += 1
                self.rand = random.randint(0,3)
            self.image = pg.image.load('assets/ClydeUp.png')

        # if(pacman.rect.x > self.rect.x): #right
        #     self.rect.x += 1
        #     if self.check_collisions_wall():
        #         self.rect.x -= 1
        #     self.image = pg.image.load('assets/BlinkyR.png')
        # if(pacman.rect.x < self.rect.x): #left
        #     self.rect.x -= 1
        #     if self.check_collisions_wall():
        #         self.rect.x += 1
        #     self.image = pg.image.load('assets/BlinkyL.png')
        # if(pacman.rect.y > self.rect.y): #down
        #     self.rect.y += 1
        #     if self.check_collisions_wall():
        #         self.rect.y -= 1
        #     self.image = pg.image.load('assets/BlinkyD.png')
        # if(pacman.rect.y < self.rect.y): #up
        #     self.rect.y -= 1
        #     if self.check_collisions_wall():
        #         self.rect.y += 1
        #     self.image = pg.image.load('assets/BlinkyUp.png')
    
class Clyde(Ghost):
    def __init__(self, game, x, y):
        image = 'assets/BlinkyR.png'
        Ghost.__init__(self, game, x, y, image)
        self.rand = random.randint(0, 3)

    def clydeAI(self, pacman):
        if random.randrange(0, 500) < 1:
            self.rand = random.randint(0, 3)
        if self.rand == 0: #right
            self.rect.x += 1
            if self.check_collisions_wall():
                self.rect.x -= 1
                self.rand = random.randint(0,3)
            self.image = pg.image.load('assets/BlinkyR.png')
        if self.rand == 1: #left
            self.rect.x -= 1
            if self.check_collisions_wall():
                self.rect.x += 1
                self.rand = random.randint(0,3)
                self.image = pg.image.load('assets/BlinkyL.png')
        if self.rand == 2: #down
            self.rect.y += 1
            if self.check_collisions_wall():
                self.rect.y -= 1
                self.rand = random.randint(0,3)
            self.image = pg.image.load('assets/BlinkyD.png')
        if self.rand == 3: #up
            self.rect.y -= 1
            if self.check_collisions_wall():
                self.rect.y += 1
                self.rand = random.randint(0,3)
            self.image = pg.image.load('assets/BlinkyUp.png')

class Inky(Ghost):
    def __init__(self, game, x, y):
        image = 'assets/InkyR.png'
        Ghost.__init__(self, game, x, y, image)
        self.rand = random.randint(0, 3)
        
    def inkyAI(self, pacman):
        if random.randrange(0, 500) < 1:
            self.rand = random.randint(0, 3)
        if self.rand == 0: #right
            self.rect.x += 1
            if self.check_collisions_wall():
                self.rect.x -= 1
                self.rand = random.randint(0,3)
            self.image = pg.image.load('assets/InkyR.png')
        if self.rand == 1: #left
            self.rect.x -= 1
            if self.check_collisions_wall():
                self.rect.x += 1
                self.rand = random.randint(0,3)
                self.image = pg.image.load('assets/InkyL.png')
        if self.rand == 2: #down
            self.rect.y += 1
            if self.check_collisions_wall():
                self.rect.y -= 1
                self.rand = random.randint(0,3)
            self.image = pg.image.load('assets/InkyD.png')
        if self.rand == 3: #up
            self.rect.y -= 1
            if self.check_collisions_wall():
                self.rect.y += 1
                self.rand = random.randint(0,3)
            self.image = pg.image.load('assets/InkyUp.png')
            
class Pinky(Ghost):
    def __init__(self, game, x, y):
        image = 'assets/PinkyR.png'
        Ghost.__init__(self, game, x, y, image)
        self.rand = random.randint(0, 3)
        
    def pinkyAI(self, pacman):
        if random.randrange(0, 500) < 1:
            self.rand = random.randint(0, 3)
        if self.rand == 0: #right
            self.rect.x += 1
            if self.check_collisions_wall():
                self.rect.x -= 1
                self.rand = random.randint(0,3)
            self.image = pg.image.load('assets/PinkyR.png')
        if self.rand == 1: #left
            self.rect.x -= 1
            if self.check_collisions_wall():
                self.rect.x += 1
                self.rand = random.randint(0,3)
                self.image = pg.image.load('assets/PinkyL.png')
        if self.rand == 2: #down
            self.rect.y += 1
            if self.check_collisions_wall():
                self.rect.y -= 1
                self.rand = random.randint(0,3)
            self.image = pg.image.load('assets/PinkyD.png')
        if self.rand == 3: #up
            self.rect.y -= 1
            if self.check_collisions_wall():
                self.rect.y += 1
                self.rand = random.randint(0,3)
            self.image = pg.image.load('assets/PinkyUp.png')
            

class Fruit(Ghost):
    def __init__(self, game, x, y):
        image = 'assets/cherry.png'
        Ghost.__init__(self, game, x, y, image)
        self.rand = random.randint(0,3)
    
    def fruitAI(self):
        if random.randrange(0, 1000) < 1:
            self.rand = random.randint(0, 3)
        if self.rand == 0: #right
            self.rect.x += 1
            if self.check_collisions_wall():
                self.rect.x -= 1
                self.rand = random.randint(0,3)
        if self.rand == 1: #left
            self.rect.x -= 1
            if self.check_collisions_wall():
                self.rect.x += 1
                self.rand = random.randint(0,3)
        if self.rand == 2: #down
            self.rect.y += 1
            if self.check_collisions_wall():
                self.rect.y -= 1
                self.rand = random.randint(0,3)
        if self.rand == 3: #up
            self.rect.y -= 1
            if self.check_collisions_wall():
                self.rect.y += 1
                self.rand = random.randint(0,3)