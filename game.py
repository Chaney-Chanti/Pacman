import time
import pygame as pg
from settings import Settings
from map import Wall, Map
import game_functions as gf
from sound import Sound
from scoreboard import Scoreboard
from button import Button
import sys
import pprint

def get_font(size): 
    return pg.font.Font("assets/font.ttf", size)

class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        size = self.settings.screen_width, self.settings.screen_height   # tuple
        self.screen = pg.display.set_mode(size=size)

        self.map = Map(self.screen)
        self.sound = Sound(bg_music="sounds/pacman_beginning.wav")
        self.scoreboard = Scoreboard(game=self)  

        self.settings.initialize_speed_settings()

    def reset(self):
        print('Resetting game...')
        # self.scoreboard.reset()

    def game_over(self):
        print('Pacman is dead: game over!')
        self.sound.gameover()
        #self.ship.pacman_left = self.settings.pacman_limit
        self.sound.stop_bg()
        self.reset()
        self.sound = Sound(bg_music="sounds/pacman_beginning.wav")
        self.menu()

    def menu(self):
        pg.display.set_caption("Menu")
        pg.mixer.music.play()
        
        while True:
            MENU_MOUSE = pg.mouse.get_pos()

            MENU_TEXT = get_font(75).render("PACMAN", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(self.settings.screen_width / 2, (self.settings.screen_height / 2) - 200))

            PLAY_BUTTON = Button(image=pg.image.load("assets/Play_Rect.png"), pos=(self.settings.screen_width / 2, (self.settings.screen_height / 2)), 
                text_input="PLAY GAME", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=pg.image.load("assets/Play_Rect.png"), pos=(self.settings.screen_width / 2, (self.settings.screen_height / 2) + 100), 
                text_input="QUIT GAME", font=get_font(40), base_color="#d7fcd4", hovering_color="White")

            self.screen.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON,QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE)
                button.update(self.screen)
        
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE):
                        self.play()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE):
                        pg.quit()
                        sys.exit()
            
            pg.display.update()
            self.screen.fill((0, 0, 0))
        
    def play(self): #NEED TO REPLACE MENTIONS OF "SHIP" WITH "PACMAN" ONCE PACMAN HAS BEEN IMPLEMENTED
        pg.display.set_caption("PACMAN")

        while True:
            gf.check_events(settings=self.settings)
            self.screen.fill(self.settings.bg_color)
            self.map.update()
            self.scoreboard.update()
            pg.display.update()



    
def main():
    g = Game()
    g.menu()


if __name__ == '__main__':
    main()