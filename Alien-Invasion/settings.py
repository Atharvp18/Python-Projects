#Settings class to store all settings at one place
class Settings():
    #Screen static Settings
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color= (38,45,65)
        
        #Ship
        self.ship_limit = 3

        #Bullet
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255,0,0
        self.bullets_allowed = 4

        #Alien
        self.fleet_drop_speed = 8

        #Game speed up
        self.speedup_scale = 1.1
        #Score increases at each level
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 10.5
        self.bullet_speed_factor = 9
        self.alien_speed_factor = 3.6
        #Fleet direction: 1=right & -1=left
        self.fleet_direction = 1
        #Scoring
        self.alien_points = 50

    def increase_speed(self):
    #Increase speed settings & alien point values
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale   

        self.alien_points = int(self.alien_points * self.score_scale) 