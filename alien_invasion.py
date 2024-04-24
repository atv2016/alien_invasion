import sys

import pygame
import random

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from sound import Bg_Music, Bg_Sound
from levels import Level
from healthbar import HealthBar
from captain import Captain
from explosion import Explosion

class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):

        """Initialize the game, and create game resources."""
        pygame.init()
        
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # We start at level 1
        self.level_number=1
        self.aliens_killed=0
        # Usee this for boss interludes and set it in levels.py. If this is enabled, we only draw the boss and suspend everything else.
        self.pause=0
        self.timer=500
        self.paused_by_user=False # User pressed P on keyboard

        # Words for announcing randomly based on a modulus of aliens killed
        self.words = ['AWESOME!','GREAT','SUPER!','SWEET','AMAZING','COOL','YES!','KILLER','BOOM!','BULLSEYE','NICE WORK','RAD','NINJA','LIT','DESTROYED!',
                      'COWABUNGA!','SUPERB','ASTRO-LICIOUS','FINGER-LICKING GOOD!','ACE','BALLER!','HAVE MERCY','WIPEOUT!','HOLY COW!','BLASPHEMOUS!','WINNER WINNER','HEROIC','PUNCTUAL!','FASTIDIOUS!',
                      'BAZUNGA!','HOLY SMOKES!','MAESTRO!','EL MARIACHI!','THE CHOSEN','YOU BETTER RUN','RAZED','LASER-BOTOMY...','WHAM!','BAM!','BATMAN!','MASTER-NINJA','PLANETKILLER','STAR-LORD!']

        # Set the game icon
        gameIcon = pygame.image.load('images/alien.png')
        pygame.display.set_icon(gameIcon)

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.healthbar = HealthBar(self)
        self.level=Level(self)
        #self.level_reset=Level(self) # Setup a instance we can exchange, this will be a little bit faster then in __init__ rather then setting it up during the main loop
        self.message = ""
        self.prev_msg = self.message

        self._create_fleet()
        
        Bg_Music() # Only needs this one all in init method
        self.sound=Bg_Sound(self) # Need this more then once, separate methods
        self.sound.level_up_sound() # Play this once for the first level

        self.captain=Captain(self) # Disabled as it takes too long to startup

        self.explosion_group = pygame.sprite.Group()
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.paused_by_user!=True:
                self.sound.level_sounds() # 
                #self._check_events()
                self.ship.update()
                #self._create_fleet()
                self._update_bullets()
                self._update_aliens()
                self._update_screen()
                self.clock.tick(60)
    
    def _check_events(self):
        """Respond to keypresses and mouse events. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses. """
        if event.key == pygame.K_0:
            self.captain.blitme()
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
            self.sound.ship_move()
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
            self.sound.ship_move()
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
            self.sound.ship_move()
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
            self.sound.ship_move()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_f:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
            self._create_fleet()
            #self.settings = Settings()
            self.ship = Ship(self)
        elif event.key == pygame.K_w:
            self.settings.screen_width = 1200
            self.settings.screen_height = 800
            self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
            self._create_fleet()
            #self.settings = Settings()
            self.ship = Ship(self)
        elif event.key == pygame.K_p:
            if self.paused_by_user==True:
                self.paused_by_user=False
                self.message='RESUMING...'
                self.text = self.level.level_marker.render(self.message, True, self.level.white, self.level.blue)
                self.level.level_announce()
                pygame.mixer.Channel(0).play(pygame.mixer.Sound(f'sounds/gameresumed.mp3'), maxtime=-1)
            else:
                self.paused_by_user=True
                pygame.mixer.Channel(1).play(pygame.mixer.Sound(f'sounds/gamepaused.mp3'), maxtime=-1)
                self._update_screen()

        elif event.key == pygame.K_q:
            sys.exit()

        elif self.captain.name_set==False:
                if(event.key != pygame.K_RETURN):
                    #self.captain.name.append(pygame.key.name(event.key))
                    self.captain.name+=event.unicode
                    self.captain.name = ''.join(self.captain.name)
                    self.captain.update_name()
                else:
                    print("Player name set")
                    #self.captain.name = ''.join(self.captain.name)
                    #self.captain.update_name()
                    self.captain.name_set=True

    def _check_keyup_events(self, event):
        """Respond to key releases. """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

        # Also play a sound
        self.sound.ship_laser()

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <0:
                self.bullets.remove(bullet)

        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien.
        collision = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        if collision:
            self.alien_kill=self.aliens_killed
            self.aliens_killed+=1
            self.sound.alien_explosion()
            for a,b in collision.items():
                for alien in b:
                    self.explosion = Explosion(alien.rect.x,alien.rect.y)
            self.explosion_group.add(self.explosion)

        if(self.healthbar.bar_level<=50):
            self.sound.defeated() # Play top monster boss sound after defeat
            self.message='YOU LOST'
            self.lost_explosion = Explosion(self.ship.rect.x+random.randint(0,100), self.ship.rect.y+random.randint(0,100))
            self.explosion_group.add(self.lost_explosion)
            self.text = self.level.level_marker.render(self.message, True, self.level.white, self.level.blue)
            self.level.level_announce()
            #self.healthbar.bar_level=500
            #self.level_number=1
            #self.level=self.level_reset # Reset all the flags in the dictionary again so parameters are honored but this introduces a bug
            if self.level.passed_time==500:
                pygame.mixer.Channel(2).play(pygame.mixer.Sound('sounds/shipdestroyed.mp3'), maxtime=-1)
                self.__init__() #works but slow but resets position as well
            #self.message=''
            self._create_fleet()
        else:
            for alien in self.aliens.sprites():
                if self.ship.rect.colliderect(alien.rect):
                    # Flash the health bar
                    self.healthbar.bar_flash=True
                    # Play damage sound
                    self.sound.ship_damage()
                    self.healthbar.bar_level-=5

        # Let's do a candy crush type of words encouraging the player
        if self.aliens_killed > 0 and self.aliens_killed %4 == 0 and self.alien_kill<self.aliens_killed: # Only grab from bag o'words if we killed more aliens
                self.message=f'{random.choice(self.words)}'
                self.text = self.level.level_marker.render(self.message, True, self.level.white, self.level.blue)
                self.alien_kill=self.aliens_killed
            
        #if self.aliens_killed==5:
        #    self.message='STARKILLER'
        #    self.text = self.level.level_marker.render(self.message, True, self.level.white, self.level.blue)
        #    self.settings.bullet_width=10
        #    self.settings.bullet_width=15
        #    self.settings.bullet_color=(100,100,100)

        #if self.aliens_killed==10:
        #    self.message='GIGA!'
        #    self.text = self.level.level_marker.render(self.message, True, self.level.green, self.level.blue)
        #    self.settings.bullet_width=15
        #    self.settings.bullet_width=20
        #    self.settings.bullet_color=(200,100,100)
        

        # Change this to if hit
        #if self.level_number==2:
        #    self.healthbar.bar_level=400
        # And loose bullet super powers

        if(self.level.level_attributes[self.level_number-1]['pause']==True):
            print("Pausing for 1-1 with the boss before boss level starts...")
            pygame.mixer.Channel(3).play(pygame.mixer.Sound('sounds/interlude.mp3'), maxtime=-1)

            self.level.level_announce()
            pygame.mixer.Channel(4).play(pygame.mixer.Sound(f'sounds/level{self.level_number}.mp3'), maxtime=-1)


            self.timer-=1
            print(f"Current pause timer set to: {self.timer}")
            if self.timer==0:
                self.message=f'Level {self.level_number} cleared...'
                self.text = self.level.level_marker.render(self.message, True, self.level.green, self.level.blue)
                self.level.level_announce()
                self.level_number+=1
                print(f"Level up current level is now {self.level_number}")
                self.sound.level_up_sound()
                pygame.mixer.Channel(5).play(pygame.mixer.Sound('sounds/levelcleared.mp3'), maxtime=-1)
                self._create_fleet()
                print(f"Setting level pause flag to pause again: {self.level.level_attributes[self.level_number-1]['pause']}")
                self.level.level_attributes[self.level_number-1]['pause']=False
                print("Resetting pause timer to 500")
                self.timer=500

        else:
            self.level.level_announce()
            if self.paused_by_user==True: # Don't announce level if we are paused
                pygame.mixer.Channel(6).play(pygame.mixer.Sound(f'sounds/level{self.level_number}.mp3'), maxtime=-1)

            if len(self.aliens) == 0:
                print("List empty!")
                self.message=f'Level {self.level_number} cleared...'
                self.text = self.level.level_marker.render(self.message, True, self.level.green, self.level.blue)
                self.level.level_announce()
                self.level_number += 1
                print(f"Level up current level is now {self.level_number}")
                self.sound.level_up_sound()
                pygame.mixer.Channel(7).play(pygame.mixer.Sound('sounds/levelcleared.mp3'), maxtime=-1)
                self._create_fleet()

    def _update_aliens(self):
        """Check if the fleet is at an edge, then update positions."""
        self._check_fleet_edges()
        self.aliens.update()

    def _create_fleet(self):
        """Create the fleet of aliens. """
        self.aliens = pygame.sprite.Group()
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width and one alien height.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        
        current_x, current_y = alien_width, alien_height

        if self.level.level_attributes[self.level_number-1]['pause']==False:

            if(self.level.level_attributes[self.level_number-1]['boss_fight']==False):
                print(f"regular enemies level: {self.level_number}")
                print(f"boss fight: (should be always be 0): {self.level.level_attributes[self.level_number-1]['boss_fight']}")
                while current_y < (self.settings.screen_height -3 * alien_height):
                    while current_x < (self.settings.screen_width -2 * alien_width):
                        self._create_alien(current_x, current_y)
                        current_x += 2 * alien_width

                    # Finished a row; reset x value, and increment y value.
                    current_x = alien_width
                    current_y += 2 * alien_height
                    print(f"Created: {len(self.aliens)} regular aliens")
            else:
                print(f"boss enemy level : {self.level_number}")
                print(f"boss fight: (should always be 1) {self.level.level_attributes[self.level_number-1]['boss_fight']}")
                pygame.mixer.Channel(3).play(pygame.mixer.Sound('sounds/bosslevel.mp3'), maxtime=-1)
                #while current_y < (self.settings.screen_height -3 * alien_height):
                #    while current_x < (self.settings.screen_width -2 * alien_width):
                self._create_alien(current_x, current_y)
                #current_x += 2 * alien_width

                # Finished a row; reset x value, and increment y value.
                #current_x = alien_width
                #current_y += 2 * alien_height
                print(f"Created: {len(self.aliens)} boss aliens")


    def _create_alien(self,x_position, y_position):
            new_alien = Alien(self)
            new_alien.x = x_position
            new_alien.rect.x = x_position
            new_alien.rect.y = y_position
            self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen. """
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        
        self.level.blitme()
        self.healthbar.blitme()
        self.captain.blitme() # Disabled as it takes too long to startup

        if(self.level.level_attributes[self.level_number-1]['pause']==False):
            self.ship.blitme()
            self.aliens.draw(self.screen)
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.explosion_group.draw(self.screen)
            self.explosion_group.update()
        else:
            print(f"Not blitting aliens, bullets or ship as pause flag is set to {self.level.level_attributes[self.level_number-1]['pause']} for level {self.level_number}")

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def scale_bar(self,image, width):
        size = image.get_size()
        margin = 4
        middel_parat = image.subsurface(pygame.Rect(margin, 0, size[0]-margin*2, size[1]))
        scaled_image = pygame.Surface((width, size[1]))
        scaled_image.set_colorkey(( 0 , 0 , 0))
        scaled_image.blit(image, (0, 0), (0, 0, margin, size[1]))
        scaled_image.blit(pygame.transform.smoothscale(middel_parat, (width-margin*2, size[1])), (margin, 0))
        scaled_image.blit(image, (width-margin, 0), (size[0]-margin, 0, margin, size[1]) )
        return scaled_image


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()