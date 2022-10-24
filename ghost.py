import pygame as pg
from pygame.sprite import Sprite, Group
import random
from timer import Timer
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
    
    def vulnerable(self):
        self.blinky.is_vuln = True
        self.clyde.is_vuln = True
        self.inky.is_vuln = True
        self.pinky.is_vuln = True
        
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
        self.pinky.x, self.pinky.y = self.spawns['Pinky'][0], self.spawns['Pinky'][1]

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
        self.is_vuln = False
        self.rect = self.image.get_rect()
        self.x, self.y = x, y
        self.rect.left, self.rect.top = x * self.rect.width, y * self.rect.height
        self.rect.x = self.rect.left
        self.rect.y = self.rect.top
        self.screen = self.game.screen
        
        self.ghost_vuln_animation = [pg.transform.rotozoom(pg.image.load(f'assets/GhostsBlue{n}.png'), 0, 1.0) for n in range(1,3)]
        self.ghost_blue_timer = Timer(image_list=self.ghost_vuln_animation, delay=100, is_loop=True) 

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
        image = 'assets/BlinkyR1.png'
        Ghost.__init__(self, game, x, y, image)
        
        self.blinky_up = [pg.transform.rotozoom(pg.image.load(f'assets/BlinkyUp{n}.png'), 0, 1.0) for n in range(1,3)]
        self.blinky_down = [pg.transform.rotozoom(pg.image.load(f'assets/BlinkyD{n}.png'), 0, 1.0) for n in range(1,3)]
        self.blinky_right = [pg.transform.rotozoom(pg.image.load(f'assets/BlinkyR{n}.png'), 0, 1.0) for n in range(1,3)]
        self.blinky_left = [pg.transform.rotozoom(pg.image.load(f'assets/BlinkyL{n}.png'), 0, 1.0) for n in range(1,3)]
        
        self.timer_up = Timer(image_list=self.blinky_up, delay=100, is_loop=True)
        self.timer_down = Timer(image_list=self.blinky_down, delay=100, is_loop=True)
        self.timer_right = Timer(image_list=self.blinky_right, delay=100, is_loop=True)
        self.timer_left = Timer(image_list=self.blinky_left, delay=100, is_loop=True)
        self.timer = self.timer_up
        
        self.rand = random.randint(0, 3)
        
    def blinkyAI(self, pacman):
        if random.randrange(0, 500) < 1:
            self.rand = random.randint(0, 3)
        if self.rand == 0: #right
            self.rect.x += 1
            if self.check_collisions_wall():
                self.rect.x -= 1
                self.rand = random.randint(0,3)
            if(self.is_vuln):
                self.timer = self.ghost_blue_timer
                self.image = self.ghost_blue_timer.image()
            else:
                self.timer = self.timer_right
                self.image = self.timer.image()
        if self.rand == 1: #left
            self.rect.x -= 1
            if self.check_collisions_wall():
                self.rect.x += 1
                self.rand = random.randint(0,3)
            if(self.is_vuln):
                #self.image = pg.image.load('assets/GhostsWhite1.png')
                self.timer = self.ghost_blue_timer
                self.image = self.ghost_blue_timer.image()
            else:
                #self.image = pg.image.load('assets/BlinkyL.png')
                self.timer = self.timer_left
                self.image = self.timer.image()
        if self.rand == 2: #down
            self.rect.y += 1
            if self.check_collisions_wall():
                self.rect.y -= 1
                self.rand = random.randint(0,3)
            if(self.is_vuln):
                #self.image = pg.image.load('assets/GhostsWhite1.png')
                self.timer = self.ghost_blue_timer
                self.image = self.ghost_blue_timer.image()
            else:
                #self.image = pg.image.load('assets/BlinkyD.png')
                self.timer = self.timer_down
                self.image = self.timer.image()
        if self.rand == 3: #up
            self.rect.y -= 1
            if self.check_collisions_wall():
                self.rect.y += 1
                self.rand = random.randint(0,3)
            if(self.is_vuln):
                #self.image = pg.image.load('assets/GhostsWhite1.png')
                self.timer = self.ghost_blue_timer
                self.image = self.ghost_blue_timer.image()
            else:
                #self.image = pg.image.load('assets/BlinkyUp.png')
                self.timer = self.timer_up
                self.image = self.timer.image()

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
        image = 'assets/ClydeR1.png'
        Ghost.__init__(self, game, x, y, image)
        
        self.clyde_up = [pg.transform.rotozoom(pg.image.load(f'assets/ClydeUp{n}.png'), 0, 1.0) for n in range(1,3)]
        self.clyde_down = [pg.transform.rotozoom(pg.image.load(f'assets/ClydeD{n}.png'), 0, 1.0) for n in range(1,3)]
        self.clyde_right = [pg.transform.rotozoom(pg.image.load(f'assets/ClydeR{n}.png'), 0, 1.0) for n in range(1,3)]
        self.clyde_left = [pg.transform.rotozoom(pg.image.load(f'assets/ClydeL{n}.png'), 0, 1.0) for n in range(1,3)]
        
        self.timer_up = Timer(image_list=self.clyde_up, delay=100, is_loop=True)
        self.timer_down = Timer(image_list=self.clyde_down, delay=100, is_loop=True)
        self.timer_right = Timer(image_list=self.clyde_right, delay=100, is_loop=True)
        self.timer_left = Timer(image_list=self.clyde_left, delay=100, is_loop=True)
        self.timer = self.timer_up
        
        self.rand = random.randint(0, 3)

    def clydeAI(self, pacman):
        if random.randrange(0, 500) < 1:
            self.rand = random.randint(0, 3)
        if self.rand == 0: #right
            self.rect.x += 1
            if self.check_collisions_wall():
                self.rect.x -= 1
                self.rand = random.randint(0,3)
            if(self.is_vuln):
                self.timer = self.ghost_blue_timer
                self.image = self.ghost_blue_timer.image()
            else:
                self.timer = self.timer_right
                self.image = self.timer.image()
        if self.rand == 1: #left
            self.rect.x -= 1
            if self.check_collisions_wall():
                self.rect.x += 1
                self.rand = random.randint(0,3)
            if(self.is_vuln):
                self.timer = self.ghost_blue_timer
                self.image = self.ghost_blue_timer.image()
            else:
                self.timer = self.timer_left
                self.image = self.timer.image()
        if self.rand == 2: #down
            self.rect.y += 1
            if self.check_collisions_wall():
                self.rect.y -= 1
                self.rand = random.randint(0,3)
            if(self.is_vuln):
                self.timer = self.ghost_blue_timer
                self.image = self.ghost_blue_timer.image()
            else:
                self.timer = self.timer_down
                self.image = self.timer.image()
        if self.rand == 3: #up
            self.rect.y -= 1
            if self.check_collisions_wall():
                self.rect.y += 1
                self.rand = random.randint(0,3)
            if(self.is_vuln):
                self.timer = self.ghost_blue_timer
                self.image = self.ghost_blue_timer.image()
            else:
                self.timer = self.timer_up
                self.image = self.timer.image()

class Inky(Ghost):
    def __init__(self, game, x, y):
        image = 'assets/InkyR1.png'
        Ghost.__init__(self, game, x, y, image)
        
        self.inky_up = [pg.transform.rotozoom(pg.image.load(f'assets/InkyUp{n}.png'), 0, 1.0) for n in range(1,3)]
        self.inky_down = [pg.transform.rotozoom(pg.image.load(f'assets/InkyD{n}.png'), 0, 1.0) for n in range(1,3)]
        self.inky_right = [pg.transform.rotozoom(pg.image.load(f'assets/InkyR{n}.png'), 0, 1.0) for n in range(1,3)]
        self.inky_left = [pg.transform.rotozoom(pg.image.load(f'assets/InkyL{n}.png'), 0, 1.0) for n in range(1,3)]
        
        self.timer_up = Timer(image_list=self.inky_up, delay=100, is_loop=True)
        self.timer_down = Timer(image_list=self.inky_down, delay=100, is_loop=True)
        self.timer_right = Timer(image_list=self.inky_right, delay=100, is_loop=True)
        self.timer_left = Timer(image_list=self.inky_left, delay=100, is_loop=True)
        self.timer = self.timer_up
        
        self.rand = random.randint(0, 3)
        
    def inkyAI(self, pacman):
        if random.randrange(0, 500) < 1:
            self.rand = random.randint(0, 3)
        if self.rand == 0: #right
            self.rect.x += 1
            if self.check_collisions_wall():
                self.rect.x -= 1
                self.rand = random.randint(0,3)
            if(self.is_vuln):
                self.timer = self.ghost_blue_timer
                self.image = self.ghost_blue_timer.image()
            else:
                self.timer = self.timer_right
                self.image = self.timer.image()
        if self.rand == 1: #left
            self.rect.x -= 1
            if self.check_collisions_wall():
                self.rect.x += 1
                self.rand = random.randint(0,3)
            if(self.is_vuln):
                self.timer = self.ghost_blue_timer
                self.image = self.ghost_blue_timer.image()
            else:
                self.timer = self.timer_left
                self.image = self.timer.image()
        if self.rand == 2: #down
            self.rect.y += 1
            if self.check_collisions_wall():
                self.rect.y -= 1
                self.rand = random.randint(0,3)
            if(self.is_vuln):
                self.timer = self.ghost_blue_timer
                self.image = self.ghost_blue_timer.image()
            else:
                self.timer = self.timer_down
                self.image = self.timer.image()
        if self.rand == 3: #up
            self.rect.y -= 1
            if self.check_collisions_wall():
                self.rect.y += 1
                self.rand = random.randint(0,3)
            if(self.is_vuln):
                self.timer = self.ghost_blue_timer
                self.image = self.ghost_blue_timer.image()
            else:
                self.timer = self.timer_up
                self.image = self.timer.image()
            
class Pinky(Ghost):
    def __init__(self, game, x, y):
        image = 'assets/PinkyR1.png'
        Ghost.__init__(self, game, x, y, image)
        
        self.pinky_up = [pg.transform.rotozoom(pg.image.load(f'assets/PinkyUp{n}.png'), 0, 1.0) for n in range(1,3)]
        self.pinky_down = [pg.transform.rotozoom(pg.image.load(f'assets/PinkyD{n}.png'), 0, 1.0) for n in range(1,3)]
        self.pinky_right = [pg.transform.rotozoom(pg.image.load(f'assets/PinkyR{n}.png'), 0, 1.0) for n in range(1,3)]
        self.pinky_left = [pg.transform.rotozoom(pg.image.load(f'assets/PinkyL{n}.png'), 0, 1.0) for n in range(1,3)]
        
        self.timer_up = Timer(image_list=self.pinky_up, delay=100, is_loop=True)
        self.timer_down = Timer(image_list=self.pinky_down, delay=100, is_loop=True)
        self.timer_right = Timer(image_list=self.pinky_right, delay=100, is_loop=True)
        self.timer_left = Timer(image_list=self.pinky_left, delay=100, is_loop=True)
        self.timer = self.timer_up
        
        self.rand = random.randint(0, 3)
        
    def pinkyAI(self, pacman):
        if random.randrange(0, 500) < 1:
            self.rand = random.randint(0, 3)
        if self.rand == 0: #right
            self.rect.x += 1
            if self.check_collisions_wall():
                self.rect.x -= 1
                self.rand = random.randint(0,3)
            if(self.is_vuln):
                self.timer = self.ghost_blue_timer
                self.image = self.ghost_blue_timer.image()
            else:
                self.timer = self.timer_right
                self.image = self.timer.image()
        if self.rand == 1: #left
            self.rect.x -= 1
            if self.check_collisions_wall():
                self.rect.x += 1
                self.rand = random.randint(0,3)
            if(self.is_vuln):
                self.timer = self.ghost_blue_timer
                self.image = self.ghost_blue_timer.image()
            else:
                self.timer = self.timer_left
                self.image = self.timer.image()
        if self.rand == 2: #down
            self.rect.y += 1
            if self.check_collisions_wall():
                self.rect.y -= 1
                self.rand = random.randint(0,3)
            if(self.is_vuln):
                self.timer = self.ghost_blue_timer
                self.image = self.ghost_blue_timer.image()
            else:
                self.timer = self.timer_down
                self.image = self.timer.image()
        if self.rand == 3: #up
            self.rect.y -= 1
            if self.check_collisions_wall():
                self.rect.y += 1
                self.rand = random.randint(0,3)
            if(self.is_vuln):
                self.timer = self.ghost_blue_timer
                self.image = self.ghost_blue_timer.image()
            else:
                self.timer = self.timer_up
                self.image = self.timer.image()
            

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