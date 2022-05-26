import json

class GameStats:
    """ track statistic for alien invasion """

    def __init__(self, ai_game):
        """ initialise statistics """
        self.settings = ai_game.settings
        self.reset_stats()

        # start alien invasion in an active state
        self.game_active = False

        # high score should never be reset
        self.high_score = self.get_saved_high_score()

    def get_saved_high_score(self):
        """ get high score from file, if it exists """
        try:
            with open('high_score.json',) as f:
                return json.load(f)

        except FileNotFoundError:
            return 0

    def reset_stats(self):
        """ initialise statistics that can change during the game """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1