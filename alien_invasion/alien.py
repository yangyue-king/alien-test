import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.ai_settings = ai_settings
        self.direction = self.ai_settings.alien_direction    # 设置了初始方向

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()                    # 在图像中加载图形属性
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):

        self.x += (self.ai_settings.alien_speed_factor*self.direction)
        self.rect.x = self.x
    def check_edges(self):
        if self.rect.right >= self.screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
    def change_alien_direction(self):
        self.direction = (-1)*self.direction
