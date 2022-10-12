import pygame as pg
import time


class Sound:
    def __init__(self, bg_music):
        pg.mixer.init()
        pg.mixer.music.load(bg_music)
        pg.mixer.music.set_volume(0.1)
        pacman_chomp_sound = pg.mixer.Sound('sounds/pacman_chomp.wav')
        pacman_death_sound = pg.mixer.Sound('sounds/pacman_death.wav')
        pacman_eatfruit_sound = pg.mixer.Sound('sounds/pacman_eatfruit.wav')
        pacman_eatghost_sound = pg.mixer.Sound('sounds/pacman_eatghost.wav')
        pacman_extrapac_sound = pg.mixer.Sound('sounds/pacman_extrapac.wav')
        pacman_intermission_sound = pg.mixer.Sound('sounds/pacman_intermission.wav')
        gameover_sound = pg.mixer.Sound('sounds/gameover.wav')
        self.sounds = {'pacman_chomp':pacman_chomp_sound,'pacman_death': pacman_death_sound,'pacman_eatfruit': pacman_eatfruit_sound, 
                       'pacman_eatghost': pacman_eatghost_sound, 'pacman_extrapac': pacman_extrapac_sound,
                       'pacman_intermission': pacman_intermission_sound,'gameover': gameover_sound,}

    def play_bg(self):
        pg.mixer.music.play(-1, 0.0)

    def stop_bg(self):
        pg.mixer.music.stop()

    def gameover(self): 
        self.stop_bg() 
        pg.mixer.music.load('sounds/gameover.wav')
        self.play_bg()
        time.sleep(2.8)
