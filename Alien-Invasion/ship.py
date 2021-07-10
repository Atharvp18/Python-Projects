import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    #Initializing ship and its position
    def __init__(self,ai_settings,screen):
        #Initialize the ship and set its starting position
        super(Ship,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the ship image and getting its rect 
        self.image = pygame.image.load('images/rocket.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx 
        self.rect.bottom = self.screen_rect.bottom - 20

        #Ship's center decimal value
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        
        #Movement Flag
        self.moving_right= False
        self.moving_left= False
        self.moving_up= False
        self.moving_down= False
   
    def update(self):
        #Gives continous motion to ship when flag is true
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor 

        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.ai_settings.ship_speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor      

        #Update rect object to center
        self.rect.centerx= self.centerx
        self.rect.centery= self.centery

    def blitme(self):
        #Drawing the ship at the current position
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.centerx = self.screen_rect.centerx 
        self.centery = self.screen_rect.centery + 351       

    