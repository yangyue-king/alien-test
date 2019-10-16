class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.game_active = False       # 游戏启动时为活跃状态，死了三条命则为不活跃
        self.reset_stats()
    def reset_stats(self):
        self.ship_left = self.ai_settings.ship_limit