from random import randrange

class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,0,0)

        # Ship settings
        self.ship_speed = 10.5

        # Bullet settings
        self.bullet_speed = 5.0
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 10

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        self.rotate_time = 0
        # We slowly decrease the rotations per level, 100 is very slow.
        self.rotate_val = 100
        self.boss_fight = 0 # Start out with regular battles, is set in level code