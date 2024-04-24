import pygame

class HealthBar:
    """A class to manage the healthbar."""

    def __init__(self, screen):
        self.screen=screen
        """Create a bullet object at the ship's current position."""
        # Set the game health bar
        self.bar_image = pygame.image.load('images/scrollbar.png').convert_alpha()
        self.bar_level=500
        self.bar_flash=False
        self.bar_timer=10

    def blitme(self):
        self.scaled_image=self.screen.scale_bar(self.bar_image,self.bar_level)
        # If bar_flash is set because of collision between alien and ship in main code, we flash the border
        if self.bar_flash == True:
            self.bar_timer-=1
            if self.bar_timer %2 == 0:
                self.tintDamage(self.scaled_image,1)

        """Draw the healthbar to the screen"""
        self.screen.screen.blit(self.scaled_image, self.scaled_image.get_rect(center = self.screen.screen.get_rect().topright))

    def tintDamage(self, surface, scale):
        # Make the red transparent and flash to the screen while taking damage.
        GB = min(255, max(0, round(255 * (1-scale))))
        #surface.fill((255, GB, GB,255), special_flags = pygame.BLEND_MULT|pygame.BLEND_RGBA_ADD)

        pygame.draw.rect(self.screen.screen, (255,0,0), self.screen.screen.get_rect(),10,border_radius=1)
        # Epileptic inducing mode below!
        #pygame.draw.rect(self.screen.screen, (255,0,0), self.screen.screen.get_rect())
        self.bar_flash=False
