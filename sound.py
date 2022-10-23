import pygame as pg
import time


class Sound:
    def __init__(self, bg_music):
        pg.mixer.init()
        pg.mixer.music.load(bg_music)
        pg.mixer.music.set_volume(0.1)
        pacman_chomp_sound = 'sounds/pacman_chomp.wav'
        pacman_death_sound = 'sounds/pacman_death.wav'
        pacman_eatfruit_sound = 'sounds/pacman_eatfruit.wav'
        pacman_eatghost_sound = 'sounds/pacman_eatghost.wav'
        pacman_extrapac_sound = 'sounds/pacman_extrapac.wav'
        pacman_intermission_sound = 'sounds/pacman_intermission.wav'
        gameover_sound = 'sounds/gameover.wav'
        self.sounds = {'pacman_chomp':pacman_chomp_sound,'pacman_death': pacman_death_sound,'pacman_eatfruit': pacman_eatfruit_sound, 
                       'pacman_eatghost': pacman_eatghost_sound, 'pacman_extrapac': pacman_extrapac_sound,
                       'pacman_intermission': pacman_intermission_sound,'gameover': gameover_sound,}

    def play_bg(self):
        pg.mixer.music.play(-1, 0.0)

    def stop(self):
        pg.mixer.music.stop()

    def play(self, song): 
        pg.mixer.music.load(song)
        pg.mixer.music.play(-1, 0.0)

    def gameover(self): 
        self.stop() 
        pg.mixer.music.load('sounds/pacman_death.wav')
        self.play_bg()
        time.sleep(1.5)
