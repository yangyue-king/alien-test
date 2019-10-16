class Settings():
    def __init__(self):
        self.screen_width = 1100
        self.screen_height = 700
        self.bg_color = (230, 230, 230)    # 屏幕属性

        self.ship_speed_factor = 2         # 飞船属性
        self.ship_limit = 1

        self.bullet_speed_factor = 3
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = 200, 60, 100     # 子弹属性
        self.bullets_allowed = 3

        self.alien_speed_factor = 1
        self.alien_drop_speed = 10
        self.alien_direction = 1            # 外星人编组初始方向为向右

        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):    # 由于类方法中已经默认有了这个方法，所以这个方法默认执行一遍
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
