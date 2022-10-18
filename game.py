import time
import pygame as pg
from settings import Settings
from map import Map
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
        self.sound.play_bg()
        
        while True:
            MENU_MOUSE = pg.mouse.get_pos()
            
            TITLE = pg.image.load("assets/PacmanTitle.png")
            MENU_TITLE = pg.transform.scale(TITLE, (800,800))
            MENU_RECT = MENU_TITLE.get_rect(center=(self.settings.screen_width / 2, (self.settings.screen_height / 2) - 300))
            self.screen.blit(MENU_TITLE, MENU_RECT)
            
            PACMAN = pg.image.load("assets/PacR2.png")
            BLINKY = pg.image.load("assets/BlinkyR.png")
            INKY = pg.image.load("assets/InkyR.png")
            CLYDE = pg.image.load("assets/ClydeR.png")
            #BLINKY = pg.image.load("assets/BlinkyR.png")
            
            PACMANPOS = PACMAN.get_rect(center=((self.settings.screen_width / 2) + 50, (self.settings.screen_height / 2)))
            BLINKYPOS = BLINKY.get_rect(center=((self.settings.screen_width / 2) - 50, (self.settings.screen_height / 2)))
            INKYPOS = INKY.get_rect(center=((self.settings.screen_width / 2) - 100, (self.settings.screen_height / 2)))
            CLYDEPOS = CLYDE.get_rect(center=((self.settings.screen_width / 2) - 150, (self.settings.screen_height / 2)))
            #BLINKYPOS = BLINKY.get_rect(center=((self.settings.screen_width / 2) - 100, (self.settings.screen_height / 2)))
            
            self.screen.blit(PACMAN,PACMANPOS)
            self.screen.blit(BLINKY, BLINKYPOS)
            self.screen.blit(INKY, INKYPOS)
            self.screen.blit(CLYDE, CLYDEPOS)
            #self.screen.blit(BLINKY, GHOSTPOS)
            
            PLAY_BUTTON = Button(image=pg.image.load("assets/Play_Rect.png"), pos=(self.settings.screen_width / 2, (self.settings.screen_height / 2) + 200), 
                text_input="PLAY GAME", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
            HIGH_SCORE_BUTTON = Button(image=pg.image.load("assets/Play_Rect.png"), pos=(self.settings.screen_width / 2, (self.settings.screen_height / 2) + 300), 
                text_input="HIGH SCORE", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=pg.image.load("assets/Play_Rect.png"), pos=(self.settings.screen_width / 2, (self.settings.screen_height / 2) + 400), 
                text_input="QUIT GAME", font=get_font(40), base_color="#d7fcd4", hovering_color="White")

            for button in [PLAY_BUTTON,QUIT_BUTTON,HIGH_SCORE_BUTTON]:
                button.changeColor(MENU_MOUSE)
                button.update(self.screen)
        
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE):
                        self.play()
                    if HIGH_SCORE_BUTTON.checkForInput(MENU_MOUSE):
                        self.high_score_window()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE):
                        pg.quit()
                        sys.exit()
            
            pg.display.update()
            self.screen.fill((0, 0, 0))
    
    def high_score_window(self):
        pg.display.set_caption("HIGH SCORE")
        high_score_file = open("high_score.txt", "r")
        name = high_score_file.readline(10)
        score = high_score_file.readline(10)
        font = get_font(30)
        text = font.render("The high score is " + score + ", held by " + name + ".", True, (255,255,255), (0,0,0))
        text_rect= text.get_rect(center=((self.settings.screen_width) / 2, (self.settings.screen_height) / 2))
        while True:
            MENU_MOUSE = pg.mouse.get_pos()
            self.screen.fill(self.settings.bg_color)
            self.screen.blit(text, text_rect)
            
            BACK_BUTTON = Button(image=pg.image.load("assets/Play_Rect.png"), pos=(150, 50), 
                text_input="<-BACK", font=get_font(40), base_color="#d7fcd4", hovering_color="White")
            for button in [BACK_BUTTON]:
                button.changeColor(MENU_MOUSE)
                button.update(self.screen)
                
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if BACK_BUTTON.checkForInput(MENU_MOUSE):
                        self.menu()
            
            pg.display.update()
        
        
        
    def play(self):
        pg.display.set_caption("PACMAN")
        pg.mixer.music.stop()

        while True:
            gf.check_events(settings=self.settings)
            self.screen.fill(self.settings.bg_color)
            self.map.update()
            self.scoreboard.update()
            pg.display.flip()



    
def main():
    g = Game()
    g.menu()


if __name__ == '__main__':
    main()