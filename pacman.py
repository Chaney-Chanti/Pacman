import pygame as pg
from timer import Timer

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
                        
        self.pacman_up_animation = [pg.transform.rotozoom(pg.image.load(f'assets/PacUp{n}.png'), 0, 1.0) for n in range(1,3)] #exclusive
        self.pacman_down_animation = [pg.transform.rotozoom(pg.image.load(f'assets/PacD{n}.png'), 0, 1.0) for n in range(1,3)] #exclusive
        self.pacman_right_animation = [pg.transform.rotozoom(pg.image.load(f'assets/PacR{n}.png'), 0, 1.0) for n in range(1,3)] #exclusive
        self.pacman_left_animation = [pg.transform.rotozoom(pg.image.load(f'assets/PacL{n}.png'), 0, 1.0) for n in range(1,3)] #exclusive

        self.timer_up = Timer(image_list=self.pacman_up_animation, delay=100, is_loop=True)
        self.timer_down = Timer(image_list=self.pacman_down_animation, delay=100, is_loop=True)
        self.timer_left = Timer(image_list=self.pacman_left_animation, delay=100, is_loop=True)
        self.timer_right = Timer(image_list=self.pacman_right_animation, delay=100, is_loop=True)
        self.timer = self.timer_up

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
            self.timer = self.timer_up
        if self.direction == 'down':
            self.timer = self.timer_down
        if self.direction == 'left':
            self.timer = self.timer_left
        if self.direction == 'right':
            self.timer = self.timer_right
        self.image = self.timer.image()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = self.x * self.rect.width, self.y * self.rect.height
        self.screen.blit(self.image, self.rect)