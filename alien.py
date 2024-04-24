import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set it's starting position."""
        super().__init__()
        self.ai_game=ai_game
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.scale_coordinate=[50,50]

        # Load the alien image and set it's rect attribute.
        self.ai_game.level.level_attributes[0]['image'] = pygame.Surface.convert_alpha(pygame.image.load("images/alien.png"))
        self.ai_game.level.level_attributes[1]['image'] = pygame.Surface.convert_alpha(pygame.image.load("images/alien.png"))
        self.ai_game.level.level_attributes[2]['image'] = pygame.Surface.convert_alpha(pygame.image.load("images/alien.png"))
        self.ai_game.level.level_attributes[3]['image'] = pygame.Surface.convert_alpha(pygame.image.load("images/xen_spaceship-2.png"))
        self.ai_game.level.level_attributes[4]['image'] = pygame.Surface.convert_alpha(pygame.image.load("images/alien.png"))
        self.ai_game.level.level_attributes[5]['image'] = pygame.Surface.convert_alpha(pygame.image.load("images/alien.png"))
        self.ai_game.level.level_attributes[6]['image'] = pygame.Surface.convert_alpha(pygame.image.load("images/alien.png"))
        self.ai_game.level.level_attributes[7]['image'] = pygame.Surface.convert_alpha(pygame.image.load("images/alien.png"))
        self.ai_game.level.level_attributes[8]['image'] = pygame.Surface.convert_alpha(pygame.image.load("images/alien.png"))
        self.ai_game.level.level_attributes[9]['image'] = pygame.Surface.convert_alpha(pygame.image.load("images/alien.png"))
        self.ai_game.level.level_attributes[10]['image'] = pygame.Surface.convert_alpha(pygame.image.load("images/alien.png"))



        print(f"Loading level {self.ai_game.level_number} alien image")
        self.image=self.ai_game.level.level_attributes[self.ai_game.level_number-1]['image'] # Sprite derivative class expects a self.image
        self.prescale=self.image
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
    
    def check_edges(self):
        """Return true if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
    def update(self):
        
        # Make it seem as if the alien is coming towards you
        if self.scale_coordinate[0]<=200 and self.scale_coordinate[1]<=200:
            self.scale_coordinate[0]+=2
            self.scale_coordinate[1]+=2
        else:
            self.image=self.prescale
            self.scale_coordinate[0]=50
            self.scale_coordinate[1]=50

        if(self.ai_game.level.level_attributes[self.ai_game.level_number-1]['boss_fight']==False): # No rotation needed for boss
            print(f"Boss fight is {self.ai_game.level.level_attributes[self.ai_game.level_number-1]['boss_fight']}, rotating alien")
            if (self.ai_game.level.level_attributes[self.ai_game.level_number-1]['rotate_time']) == (self.ai_game.level.level_attributes[self.ai_game.level_number-1]['rotate_val']):
                # Alien comes forward by zooming in
                self.image = pygame.transform.scale(self.image,self.scale_coordinate)
                # Alien rotates by 90 degrees left or right depending on rotate_val - or +
                self.image = pygame.transform.rotate(self.image, 90)
                self.ai_game.level.level_attributes[self.ai_game.level_number-1]['rotate_val'] = 0
            else :
                self.ai_game.level.level_attributes[self.ai_game.level_number-1]['rotate_val'] += 10
        else:
            print(f"Boss fight is {self.ai_game.level.level_attributes[self.ai_game.level_number-1]['boss_fight']} not rotating")

        """Move the alien right or left."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
        