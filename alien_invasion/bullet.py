import pygame
from pygame.sprite import Sprite   # 从精灵模块中导入精灵类，精灵类可以将游戏中的相关元素编组
class Bullet(Sprite):              # 子弹类继承自精灵类
    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        # 子弹并非基于图像的，使用pygame.Rect()类从空白创建一个矩形。

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor  # 颜色 速度属性
    def update(self):                            #更新子弹的y位置
        self.y -= self.speed_factor
        self.rect.y = self.y                              # rect.y 才是子弹的rect属性
    def draw_bullet(self):                                #绘制子弹
        # 直接调pygame的draw rect方法画矩形，rect属性包括尺寸，位置信息
        pygame.draw.rect(self.screen, self.color, self.rect)