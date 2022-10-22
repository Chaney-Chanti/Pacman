import pygame as pg

class Pacman(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.image.load('assets/PacUp1.png')
        self.rect = self.image.get_rect()
        self.x = x
        self. y = y
        self.direction = 'up'
        self.rect.left, self.rect.top = x * self.rect.width, y * self.rect.height
        self.screen = game.screen

        self.dying = self.dead = False
                        
        # add pacman animation here
        # self.timer_normal = Alien.alien_timers[type]              
        # self.timer_explosion = Timer(image_list=Alien.alien_explosion_images, is_loop=False)  
        # self.timer = self.timer_normal 

    def check_collisions(self):
        collisions = pg.sprite.spritecollide(self ,self.game.map.food, True)
        for food in collisions:
            self.game.scoreboard.increment_score(food.points)
        collisions = pg.sprite.spritecollide(self ,self.game.map.ghosts, False)
        if collisions:
            self.die()

    def die(self):
        self.game.reset()

    def check_collisions_wall(self):
        pass

    def update(self):
        self.check_collisions()
        self.draw()
        return
        # self.check_collisions_ghost()
        # self.check_collisions_wall()

    def draw(self): 
        if self.direction == 'up':
            self.image = pg.image.load('assets/PacR1.png')
        if self.direction == 'down':
            self.image = pg.image.load('assets/PacD1.png')
        if self.direction == 'left':
            self.image = pg.image.load('assets/PacL1.png')
        if self.direction == 'right':
            self.image = pg.image.load('assets/PacUp1.png')
        self.rect.left, self.rect.top = self.x * self.rect.width, self.y * self.rect.height
        self.screen.blit(self.image, self.rect)