class GameStats():
    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        #Start the game in an inactive state which will become active when we pres play button
        self.game_active = False
        #High Score
        self.high_score = 0

    def reset_stats(self):
        #Initializing the statistics which can change during the game
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
