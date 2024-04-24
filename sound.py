import pygame
from pygame import mixer

class Bg_Music:
    def __init__(self):
        # Starting the mixer 
        mixer.init() 
        mixer.set_num_channels=16
        # Loading the song 
        mixer.music.load("sounds/theme.mp3") 
  
        # Setting the volume 
        mixer.music.set_volume(0.9) 

        # Start playing the song 
        mixer.music.play(loops=-1,start=0.0,fade_ms=10000) 

class Bg_Sound:
    def __init__(self,main_self): 
        self.main_self=main_self

        self.level_1_sound_played=0
        self.level_2_sound_played=0
        self.level_3_sound_played=0
        self.level_4_sound_played=0
        self.level_5_sound_played=0

    @staticmethod
    def level_up_sound():
        pygame.mixer.Channel(6).play(pygame.mixer.Sound('sounds/level_up.mp3'), maxtime=-1)

    def level_sounds(self):
        # e.g. if Level 1:
        if(self.main_self.level_number==1 and self.level_1_sound_played==0):
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds/level_1.mp3'), maxtime=-1)
            self.level_1_sound_played=1

        if(self.main_self.level_number==2 and self.level_2_sound_played==0):
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds/level_2.mp3'), maxtime=-1)
            self.level_2_sound_played=1

        if(self.main_self.level_number==3 and self.level_3_sound_played==0):
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds/level_3.mp3'), maxtime=-1)
            self.level_3_sound_played=1

        if(self.main_self.level_number==4 and self.level_4_sound_played==0):
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds/level_4.mp3'), maxtime=-1)
            self.level_4_sound_played=1

        if(self.main_self.level_number==5 and self.level_5_sound_played==0):
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds/level_5.mp3'), maxtime=-1)
            self.level_5_sound_played=1

    @staticmethod
    def ship_laser():
        # Laser
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('sounds/laser.mp3'), maxtime=600)

    @staticmethod
    def alien_explosion():
        # Explosion
        pygame.mixer.Channel(2).play(pygame.mixer.Sound('sounds/explosion-1.mp3'), maxtime=600)

    @staticmethod
    def ship_move():
        # Moving
        pygame.mixer.Channel(3).play(pygame.mixer.Sound('sounds/move.mp3'), maxtime=4000)

    @staticmethod
    def ship_damage():
        # Moving
        pygame.mixer.Channel(4).play(pygame.mixer.Sound('sounds/damage.mp3'), maxtime=4000)

    @staticmethod
    def defeated():
        # Top boss is telling you you will never win after loosing
        pygame.mixer.Channel(5).play(pygame.mixer.Sound('sounds/defeat.mp3'), maxtime=-1)
