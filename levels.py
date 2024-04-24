import pygame

class Level:
        """Display Level Name and Show Level Background"""
        def __init__(self,screen):
                
                self.screen=screen

                # create a font object.
                # 1st parameter is the font file
                # which is present in pygame.
                # 2nd parameter is size of the font

                self.top_marker = pygame.font.Font('fonts/Oxanium-ExtraLight.ttf', 32)
                self.level_marker = pygame.font.Font('fonts/Oxanium-ExtraLight.ttf',150)

                # define the RGB value for white,
                #  green, blue colour .
                self.white = (255, 255, 255)
                self.green = (0, 255, 0)
                self.blue = (0, 0, 128)
                self.black = (0,0,0)
                self.red = (0,0,255)

                # Show level background
                self.level_1=pygame.Surface.convert_alpha(pygame.image.load("images/base.jpg"))
                self.level_2=pygame.Surface.convert_alpha(pygame.image.load("images/base_2.jpg"))
                self.level_3=pygame.Surface.convert_alpha(pygame.image.load("images/commanderxen_boss.jpg"))
                self.level_4=pygame.Surface.convert_alpha(pygame.image.load("images/base_4.jpg"))
                self.level_5=pygame.Surface.convert_alpha(pygame.image.load("images/base_5.jpg"))
                self.level_6=pygame.Surface.convert_alpha(pygame.image.load("images/base_6.jpg"))
                self.level_7=pygame.Surface.convert_alpha(pygame.image.load("images/base_7.jpg"))
                self.level_8=pygame.Surface.convert_alpha(pygame.image.load("images/lorelei_boss.jpg"))
                self.level_9=pygame.Surface.convert_alpha(pygame.image.load("images/base_9.jpg"))
                self.level_10=pygame.Surface.convert_alpha(pygame.image.load("images/base_9.jpg"))
    
                self.passed_time=500
                
                #self.blink_level1=0
                #self.blink_level2=0
                #self.blink_level3=0
                #self.blink_level4=0
                #self.blinked = [0,0,0,0,0,0]
                #self.interlude=False

                self.level_dict_1={'boss_fight':False,'interlude':False,'blinked':True,'start':False,'finish':False,'rotate_val':10,'rotate_time': 100,'alien_speed':1,'pause':False}
                self.level_dict_2={'boss_fight':False,'interlude':False,'blinked':True,'start':False,'finish':False,'rotate_val':10,'rotate_time': 100,'alien_speed':1,'pause':False}
                self.level_dict_3={'boss_fight':False,'interlude':True,'blinked':False,'start':False,'finish': False,'rotate_val':10,'rotate_time': 100,'alien_speed':1,'pause':True}
                self.level_dict_4={'boss_fight':True,'interlude':False,'blinked':False,'start':False,'finish': False,'rotate_val':10,'rotate_time': 100,'alien_speed':1,'pause':False}
                self.level_dict_5={'boss_fight':False,'interlude':False,'blinked':False,'start':False,'finish': False,'rotate_val':10,'rotate_time': 100,'alien_speed':1,'pause':False}
                self.level_dict_6={'boss_fight':False,'interlude':False,'blinked':False,'start':False,'finish': False,'rotate_val':10,'rotate_time': 100,'alien_speed':1,'pause':False}
                self.level_dict_7={'boss_fight':False,'interlude':False,'blinked':False,'start':False,'finish': False,'rotate_val':10,'rotate_time': 100,'alien_speed':1,'pause':False}
                self.level_dict_8={'boss_fight':False,'interlude':True,'blinked':False,'start':False,'finish': False,'rotate_val':10,'rotate_time': 100,'alien_speed':1,'pause':True}
                self.level_dict_9={'boss_fight':True,'interlude':False,'blinked':False,'start':False,'finish': False,'rotate_val':10,'rotate_time': 100,'alien_speed':1,'pause':False}
                self.level_dict_10={'boss_fight':False,'interlude':False,'blinked':False,'start':False,'finish': False,'rotate_val':10,'rotate_time': 100,'alien_speed':1,'pause':False}

                # Setup attributes per level
                self.level_attributes=[self.level_dict_1,self.level_dict_2,self.level_dict_3,self.level_dict_4,self.level_dict_5,
                                  self.level_dict_6,self.level_dict_7,self.level_dict_7,self.level_dict_8,self.level_dict_9,
                                  self.level_dict_10]


        def blitme(self):
                
                if self.screen.level_number == 1:
                # NORMAL LEVEL
                        self.screen.settings.alien_speed=1
                        # Value of 10 works best for all aliens, you could do len(self.aliens)*4 for all sides which makes them rotate more evenly
                        # But it's not perfect and it starts behaving erratically (more aliens you shoot the faster another will go!)
                        self.screen.settings.rotate_val=10
                        # create a font object.

                        text = self.top_marker.render(f'Level 1 - Planet Salikor Aliens Alive: {len(self.screen.aliens)} Aliens Killed: {self.screen.aliens_killed}', True, self.green, self.blue)
                        
                        if self.level_attributes[self.screen.level_number-1]['start']==False:
                                print('Level start announce set to False')
                                if(self.passed_time==500): # Wait that no other blit is happening
                                        print('Level start announce blit message queue available')
                                        self.screen.message='Level 1!'
                                        self.screen.text = self.level_marker.render(self.screen.message, True, self.green, self.blue)
                                        print('Level start announce set to True')
                                        self.level_attributes[self.screen.level_number-1]['start']=True
                                        
                        # create a rectangular object for the
                        # text surface object
                        textRect = text.get_rect()

                        # Blit the level background image
                        self.rect = self.screen.screen.get_rect()
                        self.screen.screen.blit(self.level_1, self.rect)
                        # copying the text surface object
                        # to the display surface object
                        # at the center coordinate.
                        self.screen.screen.blit(text, textRect)

                        # Blit the level marker for few seconds
                        
                        self.level_announce()

                if self.screen.level_number == 2:
                # NORMAL LEVEL
                        self.screen.settings.alien_speed=5
                        self.screen.settings.rotate_val=10
                        
                        # create a font object.

                        text = self.top_marker.render(f'Level 2 - Planet Z Aliens Alive: {len(self.screen.aliens)} Aliens Killed: {self.screen.aliens_killed}', True, self.green, self.blue)

                        if self.level_attributes[self.screen.level_number-1]['start']==False:
                                if(self.passed_time==500): # Wait that no other blit is happening
                                        self.screen.message='Level 2!'
                                        self.screen.text = self.level_marker.render(self.screen.message, True, self.green, self.blue)
                                        self.level_attributes[self.screen.level_number-1]['start']=True

                        # create a rectangular object for the
                        # text surface object
                        textRect = text.get_rect()
                        #textRect_2 = text_2.get_rect()

                        # Blit the level background image
                        self.rect = self.screen.screen.get_rect()
                
                        self.screen.screen.blit(self.level_2, self.rect)
                        # copying the text surface object
                        # to the display surface object
                        # at the center coordinate.
                        self.screen.screen.blit(text, textRect)

                        self.level_announce()

                if self.screen.level_number == 3:

                        self.screen.settings.alien_speed=10
                        self.screen.settings.rotate_val=10
                        # create a font object.

                        text = self.top_marker.render(f'Commander Xen: You cannot beat me. I will destroy your puny little ship!', True, self.white, self.black)
                        
                        if self.level_attributes[self.screen.level_number-1]['start']==False:
                                if(self.passed_time==500): # Wait that no other blit is happening
                                        print(f"First time start message from level is: {self.screen.message}")
                                        self.screen.message='Commander Xen!'
                                        self.screen.text = self.level_marker.render(self.screen.message, True, self.green, self.blue)
                                        self.level_attributes[self.screen.level_number-1]['start']=True

                        # create a rectangular object for the
                        # text surface object
                        textRect = text.get_rect()

                        # Blit the level background image

                        self.rect = self.level_3.get_rect(center=self.screen.screen.get_rect().center)

                        self.screen.screen.blit(self.level_3, self.rect)
                
                        # copying the text surface object
                        # to the display surface object
                        # at the center coordinate.
                    
                        self.screen.screen.blit(text, self.screen.screen.get_rect())

                        self.level_announce()


                if self.screen.level_number == 4:
                # BOSS FIGHT LEVEL
                        self.screen.settings.alien_speed=1
                        self.screen.settings.rotate_val=0 # No rotation for big guy, it looks funny for some reason as well
                        
                        # create a font object.

                        text = self.top_marker.render(f'Level 4 - Commander Xen Aliens Alive: {len(self.screen.aliens)} Aliens Killed: {self.screen.aliens_killed}', True, self.green, self.blue)
                        
                        if self.level_attributes[self.screen.level_number-1]['start']==False:
                                if(self.passed_time==500): # Wait that no other blit is happening
                                        self.screen.message='Level 4! - BOSS FIGHT!'
                                        self.screen.text = self.level_marker.render(self.screen.message, True, self.green, self.blue)
                                        self.level_attributes[self.screen.level_number-1]['start']=True
                        # create a rectangular object for the
                        # text surface object
                        textRect = text.get_rect()
                        #textRect_2 = text_2.get_rect()

                        # Blit the level background image
                        self.rect = self.screen.screen.get_rect()
                
                        self.screen.screen.blit(self.level_4, self.rect)
                        # copying the text surface object
                        # to the display surface object
                        # at the center coordinate.
                        self.screen.screen.blit(text, textRect)

                        self.level_announce()


                if self.screen.level_number == 5:
                        
                        self.screen.settings.alien_speed=1
                        self.screen.settings.rotate_val=10       

                        # create a font object.

                        text = self.top_marker.render(f'Level 5 - Planet Eridor Aliens Alive: {len(self.screen.aliens)} Aliens Killed: {self.screen.aliens_killed}', True, self.green, self.blue)

                        if self.level_attributes[self.screen.level_number-1]['start']==False:
                                if(self.passed_time==500): # Wait that no other blit is happening
                                        self.screen.message='Level 5!'
                                        self.screen.text = self.level_marker.render(self.screen.message, True, self.green, self.blue)
                                        self.level_attributes[self.screen.level_number-1]['start']=True

                        # create a rectangular object for the
                        # text surface object
                        textRect = text.get_rect()

                        # Blit the level background image
                        #self.rect = self.level_1.get_rect() just now
                        self.rect = self.screen.screen.get_rect()
                        self.screen.screen.blit(self.level_5, self.rect)
                        # copying the text surface object
                        # to the display surface object
                        # at the center coordinate.
                        self.screen.screen.blit(text, textRect)

                        self.level_announce()

                if self.screen.level_number == 6:
                        
                        self.screen.settings.alien_speed=1
                        self.screen.settings.rotate_val=10       

                        # create a font object.

                        text = self.top_marker.render(f'Level 6 - Planet Sol Aliens Alive: {len(self.screen.aliens)} Aliens Killed: {self.screen.aliens_killed}', True, self.green, self.blue)

                        if self.level_attributes[self.screen.level_number-1]['start']==False:
                                if(self.passed_time==500): # Wait that no other blit is happening
                                        self.screen.message='Level 6!'
                                        self.screen.text = self.level_marker.render(self.screen.message, True, self.green, self.blue)
                                        self.level_attributes[self.screen.level_number-1]['start']=True

                        # create a rectangular object for the
                        # text surface object
                        textRect = text.get_rect()

                        # Blit the level background image
                        #self.rect = self.level_1.get_rect() just now
                        self.rect = self.screen.screen.get_rect()
                        self.screen.screen.blit(self.level_6, self.rect)
                        # copying the text surface object
                        # to the display surface object
                        # at the center coordinate.
                        self.screen.screen.blit(text, textRect)

                        self.level_announce()

                if self.screen.level_number == 7:
                        
                        self.screen.settings.alien_speed=1
                        self.screen.settings.rotate_val=10       

                        # create a font object.

                        text = self.top_marker.render(f'Level 7 - W.O.R. Compound Aliens Alive: {len(self.screen.aliens)} Aliens Killed: {self.screen.aliens_killed}', True, self.green, self.blue)

                        if self.level_attributes[self.screen.level_number-1]['start']==False:
                                if(self.passed_time==500): # Wait that no other blit is happening
                                        self.screen.message='Level 7!'
                                        self.screen.text = self.level_marker.render(self.screen.message, True, self.green, self.blue)
                                        self.level_attributes[self.screen.level_number-1]['start']=True

                        # create a rectangular object for the
                        # text surface object
                        textRect = text.get_rect()

                        # Blit the level background image
                        #self.rect = self.level_1.get_rect() just now
                        self.rect = self.screen.screen.get_rect()
                        self.screen.screen.blit(self.level_7, self.rect)
                        # copying the text surface object
                        # to the display surface object
                        # at the center coordinate.
                        self.screen.screen.blit(text, textRect)

                        self.level_announce()

                if self.screen.level_number == 8:
                        
                        self.screen.settings.alien_speed=1
                        self.screen.settings.rotate_val=10       

                        # create a font object.

                        text = self.top_marker.render('Lorelei: You are insignificant human. You will die.', True, self.white, self.black)

                        if self.level_attributes[self.screen.level_number-1]['start']==False:
                                if(self.passed_time==500): # Wait that no other blit is happening
                                        self.screen.message='Lorelei!!'
                                        self.screen.text = self.level_marker.render(self.screen.message, True, self.green, self.blue)
                                        self.level_attributes[self.screen.level_number-1]['start']=True

                        # create a rectangular object for the
                        # text surface object
                        textRect = text.get_rect()

                        # Blit the level background image
                        #self.rect = self.level_1.get_rect() just now
                        self.rect = self.screen.screen.get_rect()
                        self.screen.screen.blit(self.level_8, self.rect)
                        # copying the text surface object
                        # to the display surface object
                        # at the center coordinate.
                        self.screen.screen.blit(text, textRect)

                        self.level_announce()

                if self.screen.level_number == 9:
                        
                        self.screen.settings.alien_speed=1
                        self.screen.settings.rotate_val=10       

                        # create a font object.

                        text = self.top_marker.render(f'Level 9 - Lorelei Aliens Alive: {len(self.screen.aliens)} Aliens Killed: {self.screen.aliens_killed}', True, self.green, self.blue)

                        if self.level_attributes[self.screen.level_number-1]['start']==False:
                                if(self.passed_time==500): # Wait that no other blit is happening
                                        self.screen.message='Level 9! - BOSS FIGHT!'
                                        self.screen.text = self.level_marker.render(self.screen.message, True, self.green, self.blue)
                                        self.level_attributes[self.screen.level_number-1]['start']=True

                        # create a rectangular object for the
                        # text surface object
                        textRect = text.get_rect()

                        # Blit the level background image
                        #self.rect = self.level_1.get_rect() just now
                        self.rect = self.screen.screen.get_rect()
                        self.screen.screen.blit(self.level_9, self.rect)
                        # copying the text surface object
                        # to the display surface object
                        # at the center coordinate.
                        self.screen.screen.blit(text, textRect)

                        self.level_announce()

        def level_announce(self):
                """Shows level announcement passed in through message """
                """ message = string you want to display"""
                """ offset = add x for every extra character of string should work
                """
                #In addition if the current fight is an interlude it will :
                
                #- SET INTERLUDE BOOL """
                #- PAUSE ACTION """
                #- 500MS LONGER FOR BLINK """
                #- UNPAUSE ACTION """
                #- SETS BOSS FIGHT PARAMETER """
                #- EMPTY LIST TO TRIGGER NEXT LEVEL""" 
                
                #text = self.level_marker.render(f'{message}', True, self.green, self.blue)

                # Blit the level marker for few seconds
                
                if self.screen.prev_msg!=self.screen.message:
                        self.level_attributes[self.screen.level_number]['blinked']=False # Set false while we blink to have a simple queuing system
                        print(f"Prev msg {self.screen.prev_msg} Current msg {self.screen.message}")
                        if(self.passed_time!=0):
                                self.passed_time -=2
                                print(f"Current message queue timer is now: {self.passed_time}")
                                                
                                if(self.passed_time %5 == 0):
                                        print("Blit")
                                        #self.screen.screen.blit(self.screen.text, self.screen.text.get_width()/2) # Offset the center tuple with 200 so it really shows centered
                                        self.screen.screen.blit(self.screen.text, ((self.screen.screen.get_width()/2-(self.screen.text.get_width())/2,
                                                                                        (self.screen.screen.get_height()/2-(self.screen.text.get_height()/2)))))
                        else:
                                print(f"Mesage queue timer reached 0, resetting to 500")
                                self.passed_time=500
                                self.level_attributes[self.screen.level_number]['blinked']=True # Message queue empty
                                # Store previous message
                                print(f"Storing previous message after blit is done")
                                self.screen.prev_msg=self.screen.message
                                #self.screen.message=''

                else:
                        print(f"Same message: Prev msg {self.screen.prev_msg} : Current msg {self.screen.message}")
     