class GameStats():
    # track stats for game

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        # init stats that can change during game
        self.ships_left = self.ai_settings.ship_limit

    