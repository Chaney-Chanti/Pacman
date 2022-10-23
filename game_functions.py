import sys
import pygame as pg
from vector import Vector
import pprint
import time

movement = {
    pg.K_LEFT: -1,
    pg.K_RIGHT: 1,
    pg.K_UP: -1,
    pg.K_DOWN: 1
}
  
def check_keydown_events(game, event, settings, pacman):
    key = event.key
    print(key)
    if key in movement.keys(): 
        if key == 1073741904: #left
            if game.map.game_map[pacman.y][pacman.x - 1] != '#' and -10 < (pacman.rect.y - pacman.y * pacman.rect.height) < 10:
                pacman.direction = 'left'
        if key == 1073741906: #up
            if game.map.game_map[pacman.y - 1][pacman.x] != '#' and -10 < (pacman.rect.x - pacman.x * pacman.rect.width) < 10:
                pacman.direction = 'up'
        if key == 1073741903: #right
             if game.map.game_map[pacman.y][pacman.x + 1] != '#' and -10 < (pacman.rect.y - pacman.y * pacman.rect.height) < 10:
                pacman.direction = 'right'
        if key == 1073741905: #down
             if game.map.game_map[pacman.y + 1][pacman.x] != '#' and -10 < (pacman.rect.x - pacman.x * pacman.rect.width) < 10:
                pacman.direction = 'down'

# def check_keyup_events(event):
#     pass
    # key = event.key
    # if key == pg.K_SPACE: ship.shooting = False
    # elif key == pg.K_ESCAPE: 
    #     ship.vel = Vector()   

def check_events(game, settings, pacman): 
    for event in pg.event.get():
       if event.type == pg.QUIT: sys.exit()
       elif event.type == pg.KEYDOWN: check_keydown_events(game, event=event, settings=settings, pacman=pacman)

def clamp(posn, rect, settings):
    pass
    # left, top = posn.x, posn.y
    # width, height = rect.width, rect.height
    # left = max(0, min(left, settings.screen_width - width))
    # top = max(0, min(top, settings.screen_height - height))
    # return Vector(x=left, y=top), pg.Rect(left, top, width, height)