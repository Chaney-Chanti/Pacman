import pygame as pg

class Pacman(pg.sprite.Sprite):
    def __init__(self, screen, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('assets/PacUp1.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x * self.rect.width, y * self.rect.height
        self.screen = screen

        self.dying = self.dead = False
                        
        # add pacman animation here
        # self.timer_normal = Alien.alien_timers[type]              
        # self.timer_explosion = Timer(image_list=Alien.alien_explosion_images, is_loop=False)  
        # self.timer = self.timer_normal 

    def check_collisions_ghost():
        pass

    def check_collisions_wall():
        pass

    def update(self):
        self.draw()
        return
        self.check_collisions_ghost()
        self.check_collisions_wall()

    def draw(self): 
        self.screen.blit(self.image, self.rect)