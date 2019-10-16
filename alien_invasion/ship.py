import pygame
class Ship():
    def __init__(self, screen, ai_settings):  #屏幕实例传递过来只是给飞船定个初始位置
        self.screen = screen
        self.screen_rect = self.screen.get_rect()  # 屏幕的rect属性

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()      #飞船ship的rect属性
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.centerx = float(self.rect.centerx)

        self.ai_settings = ai_settings

        self.moving_right = False              #加上两个类属性
        self.moving_left = False
    def update(self):    #该方法管理飞船位置
        if self.moving_right and self.rect.centerx < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
            self.rect.centerx = self.centerx
        if self.moving_left and self.rect.centerx > self.screen_rect.left:
            self.centerx -= self.ai_settings.ship_speed_factor
            self.rect.centerx = self.centerx

    def blitme(self):
        self.screen.blit(self.image, self.rect)   # 这是surface文件里定义的一个方法
    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx