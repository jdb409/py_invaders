class Settings():

    def __init__(self):
        # static settings

        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_limit = 3

        # bullet settings
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 30

        # alien settings
        self.fleet_drop_speed = 10

        # game speed up rate
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # init settings that change throughout game
        self.ship_speed_factor = 10
        self.bullet_speed_factor = 30
        self.alien_speed_factor = 50

        # fleet direction of 1 reps right, -1 reps left
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
