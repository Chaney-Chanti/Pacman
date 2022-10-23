import pygame as pg
from timer import Timer
from ghost import Fruit
from pygame import mixer

class Pacman(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.image.load('assets/PacUp1.png')
        self.rect = self.image.get_rect()
        self.ogSpawn = [x,y]
        self.x = x
        self.y = y
        self.direction = 'up'
        self.rect.left, self.rect.top = x * self.rect.width, y * self.rect.height
        self.screen = game.screen
        self.food_sound = mixer.Sound('sounds/pacman_eatfruit.wav')

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
        collisions = pg.sprite.spritecollide(self , self.game.map.food, True)
        for food in collisions:
            self.food_sound.play()
            self.game.scoreboard.increment_score(food.points)
        collisions = pg.sprite.spritecollide(self ,self.game.ghosts.ghosts, False)
        if collisions:
            if any(type(obj) == Fruit for obj in collisions):
                self.game.scoreboard.increment_score(300)
                for obj in collisions:
                    obj.kill()
            else:
                self.die()

    def reset(self):
        self.x = self.ogSpawn[0]
        self.y = self.ogSpawn[1]

    def die(self):
        self.game.game_over()
        self.game.reset()

    def check_collisions_wall(self):
        pass

    def update(self):
        self.check_collisions()
        if self.direction == 'left':
            if self.rect.x > self.x * self.rect.width:
                self.rect.x -= 1
            elif self.game.map.game_map[self.y][self.x - 1] != '#':
                self.x -= 1
        elif self.direction == 'right':
            if self.rect.x < self.x * self.rect.width:
                self.rect.x += 1
            elif self.game.map.game_map[self.y][self.x + 1] != '#':
                self.x += 1
        elif self.direction == 'up':
            if self.rect.y > self.y * self.rect.height:
                self.rect.y -= 1
            elif self.game.map.game_map[self.y - 1][self.x] != '#':
                self.y -= 1
        elif self.direction == 'down':
            if self.rect.y < self.y * self.rect.height:
                self.rect.y += 1
            elif self.game.map.game_map[self.y + 1][self.x] != '#':
                self.y += 1
        self.draw()
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
        # self.rect = self.image.get_rect()
        # self.rect.left, self.rect.top = self.x * self.rect.width, self.y * self.rect.height
        self.screen.blit(self.image, self.rect)