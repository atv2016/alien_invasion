import pygame

import pygame.camera
from pygame.locals import *
import time

from gtts import gTTS

class Captain:
    """Show captain mugshot next to healthbar. """

    def __init__(self, screen):
        self.screen=screen
        self.size=(240,180)
        self.gotcaptain=0
        self.name=[]
        self.name_set=False
        self.flash=500

        self.rect=self.screen.screen.get_rect()

        # define the RGB value for white,
         #  green, blue colour .
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 128)
        self.black = (0,0,0)
        self.red = (0,0,255)
        
        self.font_1 = pygame.font.Font('fonts/Oxanium-ExtraLight.ttf', 24)
        self.font_2 = pygame.font.Font('fonts/Oxanium-ExtraLight.ttf', 32)
        self.font_3 = pygame.font.Font('fonts/Oxanium-ExtraLight.ttf',150)
        self.text_1 = self.font_2.render(f'Player: {self.name}', True, self.green,self.blue)
        self.text_2 = self.font_2.render('Ammo',True, self.green,self.blue)
        self.text_3 = self.font_1.render('Bullets:',True, self.red,self.black)
        self.text_4 = self.font_1.render('Rockets:',True, self.red,self.black)
        self.text_5 = self.font_1.render('Bombs:',True, self.red,self.black)
        self.text_6 = self.font_2.render('Pickups',True, self.green,self.blue)
        self.text_7 = self.font_1.render('Space oddity',True, self.red,self.black)
        self.text_8 = self.font_2.render('Fuel',True, self.green,self.blue)
        self.text_9 = self.font_1.render('Afterburner: 100%',True, self.red,self.black)
        self.text_10 = self.font_3.render('Player:',True, self.green,self.blue)
        self.text_11 = self.font_3.render(f'{self.name}',True,self.green,self.blue)

        pygame.camera.init()

        # this is the same as what we saw before
        self.clist = pygame.camera.list_cameras()
        if not self.clist:
            raise ValueError("Sorry, no cameras detected.")
        self.cam = pygame.camera.Camera(self.clist[0], self.size)
        self.cam.start()

        # create a surface to capture to.  for performance purposes
        # bit depth is the same as that of the display surface.
        self.snapshot = pygame.surface.Surface(self.size, 0, self.screen.screen)

        # Pre-created mp3 files on init
        tts_identify_text="Please identify"
        tts_identify = gTTS(tts_identify_text, lang='en', slow=False)
        tts_identify.save("sounds/identify.mp3")

        tts_identify_text='Level cleared'
        tts_identify= gTTS(tts_identify_text, lang='en',slow=False)
        tts_identify.save("sounds/levelcleared.mp3")

        tts_identify_text='Level 1'
        tts_identify= gTTS(tts_identify_text, lang='en',slow=False)
        tts_identify.save("sounds/level1.mp3")

        tts_identify_text='Level 2'
        tts_identify= gTTS(tts_identify_text, lang='en',slow=False)
        tts_identify.save("sounds/level2.mp3")

        tts_identify_text='Level 3'
        tts_identify= gTTS(tts_identify_text, lang='en',slow=False)
        tts_identify.save("sounds/level3.mp3")

        tts_identify_text='Level 4'
        tts_identify= gTTS(tts_identify_text, lang='en',slow=False)
        tts_identify.save("sounds/level4.mp3")

        tts_identify_text='Level 5'
        tts_identify= gTTS(tts_identify_text, lang='en',slow=False)
        tts_identify.save("sounds/level5.mp3")

        tts_identify_text='Level 6'
        tts_identify= gTTS(tts_identify_text, lang='en',slow=False)
        tts_identify.save("sounds/level6.mp3")
    
        tts_identify_text='Level 7'
        tts_identify= gTTS(tts_identify_text, lang='en',slow=False)
        tts_identify.save("sounds/level7.mp3")
    
        tts_identify_text='Level 8'
        tts_identify= gTTS(tts_identify_text, lang='en',slow=False)
        tts_identify.save("sounds/level8.mp3")
    
        tts_identify_text='Level 9'
        tts_identify= gTTS(tts_identify_text, lang='en',slow=False)
        tts_identify.save("sounds/level9.mp3")
    
        tts_identify_text='Level 10'
        tts_identify= gTTS(tts_identify_text, lang='en',slow=False)
        tts_identify.save("sounds/level10.mp3")

        tts_identify_text='Interlude'
        tts_identify= gTTS(tts_identify_text, lang='en',slow=False)
        tts_identify.save("sounds/interlude.mp3")

        tts_identify_text='Boss Level'
        tts_identify= gTTS(tts_identify_text, lang='en',slow=False)
        tts_identify.save("sounds/bosslevel.mp3")

        tts_identify_text='Ship Destroyed'
        tts_identify= gTTS(tts_identify_text, lang='en',slow=False)
        tts_identify.save("sounds/shipdestroyed.mp3")

        tts_identify_text='Game Paused'
        tts_identify= gTTS(tts_identify_text, lang='en',slow=False)
        tts_identify.save("sounds/gamepaused.mp3")

        tts_identify_text='Game Resumed'
        tts_identify= gTTS(tts_identify_text, lang='en',slow=False)
        tts_identify.save("sounds/gameresumed.mp3")

        self.gtss_pause=250
        self.gtss_after_blit=0

    def update_name(self):
        """Set self.name once only"""
        self.text_1 = self.font_2.render(f'Player: {self.name}', True, self.green,self.blue)
        self.text_11 = self.font_3.render(f'{self.name}',True,self.green,self.blue)

    def blitme(self):

        # Get a snapshot of the pilot
        if self.gotcaptain!=1:
            if self.cam.query_image():
                self.snapshot = self.cam.get_image(self.snapshot)
                self.gotcaptain=1
                #self.cam.stop()

        # Change to live mode when we have a 1-1 with a interlude level
        if self.screen.level.level_attributes[self.screen.level_number-1]['interlude']==True:
             #if time.time() % 1 > 0.5: # Add a timer to lower framerate if needed
            if self.cam.query_image():
                self.snapshot = self.cam.get_image(self.snapshot)
                #print('test')
                
        # Blit mugshot and name
        self.screen.screen.blit(self.snapshot, (0,self.screen.settings.screen_height-200))
        # If we haven't set our name yet flash for input (and keep flashing Taito style)
        if(self.name_set==False):
            # Flash on screen using simple timer
            if time.time() % 1 > 0.5:
                self.screen.screen.blit(self.text_10,(self.screen.settings.screen_width/2-200,self.screen.settings.screen_height/2))
                self.screen.screen.blit(self.text_11,(self.screen.settings.screen_width/2+250,self.screen.settings.screen_height/2))
                # Blit name while input is given
                self.screen.screen.blit(self.text_1,(0,self.screen.settings.screen_height-250))
                
            if(self.gtss_pause>=0):
                self.gtss_pause-=1
            else:
                pygame.mixer.Channel(7).play(pygame.mixer.Sound('sounds/identify.mp3'), maxtime=-1)
                self.gtss_pause=250
        else:
                # Blit name once input is complete
                self.screen.screen.blit(self.text_1,(0,self.screen.settings.screen_height-250))
                if self.gtss_after_blit==0:
                    # Pre-created mp3 files on init
                    tts_identify_text=f"Welcome Captain { self.name }. You are authorized for destruction."
                    tts_identify = gTTS(tts_identify_text, lang='en', slow=False)
                    tts_identify.save("sounds/authorized.mp3")
                    pygame.mixer.Channel(7).play(pygame.mixer.Sound('sounds/authorized.mp3'), maxtime=-1)
                    self.gtss_after_blit=1
        # Blit inventory
        self.screen.screen.blit(self.text_2,(self.screen.settings.screen_width-550,self.screen.settings.screen_height-250))
        self.screen.screen.blit(self.text_3,(self.screen.settings.screen_width-550,self.screen.settings.screen_height-200))
        self.screen.screen.blit(self.text_4,(self.screen.settings.screen_width-550,self.screen.settings.screen_height-150))
        self.screen.screen.blit(self.text_5,(self.screen.settings.screen_width-550,self.screen.settings.screen_height-100))
        self.screen.screen.blit(self.text_6,(self.screen.settings.screen_width-400,self.screen.settings.screen_height-250))
        self.screen.screen.blit(self.text_7,(self.screen.settings.screen_width-400,self.screen.settings.screen_height-200))
        self.screen.screen.blit(self.text_8,(self.screen.settings.screen_width-250,self.screen.settings.screen_height-250))
        self.screen.screen.blit(self.text_9,(self.screen.settings.screen_width-250,self.screen.settings.screen_height-200))

