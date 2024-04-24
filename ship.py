import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position. """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the ship image and get its rect.
        self.image = pygame.Surface.convert_alpha(pygame.image.load("images/ship.png"))
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal and vertical position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def update(self):
        """Update the ship's position based on the movement flag. """
        # Update the ship's x value
        if self.moving_right and self.rect.right < self.screen_rect.right-20:
            self.x += self.settings.ship_speed
            
        if self.moving_left and self.rect.left > self.screen_rect.left+20:
            self.x -= self.settings.ship_speed

        if self.moving_up and self.rect.top > self.screen_rect.top+20:
            self.y -= self.settings.ship_speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom-20:
            self.y += self.settings.ship_speed
            

        # Update rect object from self.x.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)