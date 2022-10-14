import pygame as pg

class Wall(pg.sprite.Sprite):
    def __init__(self, screen, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('images/wall3.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x * self.rect.width, y * self.rect.height
        self.screen = screen

    # def update(self, game_map):
    #      for row in range(0, len(game_map)):
    #         for column in range(0, len(game_map[row])):
    #             if game_map[row][column] == '#':
    #                 print('hashtag')
    #                 newWall = Wall(self.screen, row, column)
    #                 newWall.draw(self.screen)
    #             if game_map[row][column] == '.':
    #                 print('food')
    #             else:
    #                 print('something else')

    def draw(self, screen):
        screen.blit(self.image, self.rect)
