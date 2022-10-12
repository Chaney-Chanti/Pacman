class Settings():
    """A class to store all settings for Pacman."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (0, 0, 0)
        
        self.pacman_limit = 3         # total pacmans allowed in game before game over
        
        self.initialize_speed_settings()

    def initialize_speed_settings(self):
        self.ghost_speed_factor = 2
        self.pacman_speed_factor = 2

    #def increase_speed(self):
        #scale = self.speedup_scale
        #self.ship_speed_factor *= scale
        #self.laser_speed_factor *= scale
