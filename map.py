import pygame as pg
from pacman import Pacman
from ghost import Blinky, Clyde, Inky


class Map:
    def __init__(self, screen):
        self.screen = screen
        self.walls = pg.sprite.Group()
        self.food = pg.sprite.Group()
        # self.pacman = pg.sprite.Group()
        self.game_map = self.read_map_file()
        # self.tile_size = self.get_tile_size()
        self.create_map()

    def read_map_file(self):
        rowList = []
        with open("map.txt", "r") as f:
            rows = f.readlines()
            for line in rows:
                rowList.append(line[:-1])
        return rowList
    
    # def get_tile_size(self):
    #     map_size = (len(max(self.game_map, key=len)), len(self.game_map)) # derives (# of columns, # of rows)
    #     size = min(math.floor(self.screen.get_width()/map_size[0]), math.floor(self.screen.get_height()/map_size[1])) # determine smallest size relative to screen size
    #     return size

    def create_map(self):
        for row in range(0, len(self.game_map)):
            for column in range(0, len(self.game_map[row])):
                if self.game_map[row][column] == '#':
                    # print(f'wall at row {row + 1}, column {column + 1}')
                    newWall = Wall(self.screen, column, row)
                    self.walls.add(newWall)
                elif self.game_map[row][column] == '.':
                    # print(f'food at row {row + 1}, column {column + 1}')
                    newFood = Food(self.screen, column, row, 1)
                    self.food.add(newFood)
                elif self.game_map[row][column] == '@':
                    # print(f'power item at row {row + 1}, column {column + 1}')
                    newFood = Food(self.screen, column, row, 2)
                    self.food.add(newFood)
                elif self.game_map[row][column] == 'P':
                    self.pacman = Pacman(self.screen, column, row)
                elif self.game_map[row][column] == 'B':
                    self.blinky = Blinky(self.screen, column, row)
                elif self.game_map[row][column] == 'C':
                    self.clyde = Clyde(self.screen, column, row)
                elif self.game_map[row][column] == 'I':
                    self.inky = Inky(self.screen, column, row)
                else:
                    # print(f'something else at row {row + 1}, column {column + 1}')
                    pass
    
    def update(self):
        for wall in self.walls:
            wall.draw()
        for food in self.food:
            food.draw()
        self.pacman.update()
        self.blinky.update()
        self.clyde.update()
        self.inky.update()


class Wall(pg.sprite.Sprite):
    def __init__(self, screen, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('assets/wall2.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x * self.rect.width, y * self.rect.height
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, self.rect)


class Food(pg.sprite.Sprite):
    def __init__(self, screen, x, y, type):
        pg.sprite.Sprite.__init__(self)
        self.type = type
        if type == 1:
            self.image = pg.image.load('assets/pill.png')
        elif type == 2:
            self.image = pg.image.load('assets/bigPill.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = x * self.rect.width, y * self.rect.height
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, self.rect)

