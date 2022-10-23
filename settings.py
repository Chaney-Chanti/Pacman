class Settings():
    """A class to store all settings for Pacman."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 990
        self.bg_color = (50, 50, 50)
        
        self.pacman_limit = 3         # total pacmans allowed in game before game over
        self.pac_dot_points = 10
        self.power_pellet_points = 50
        
        self.initialize_speed_settings()

    def initialize_speed_settings(self):
        self.ghost_speed_factor = 2
        self.pacman_speed_factor = 2

    #def increase_speed(self):
        #scale = self.speedup_scale
        #self.ship_speed_factor *= scale
        #self.laser_speed_factor *= scale
