import pygame
#import sys      由于函数重构 检查中断函数由check——events代替，故这里不再需要导入sys模块
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
def run_game():
    pygame.init()
    ai_settings = Settings()   #创建参数实例
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    play_button = Button(ai_settings, screen, 'Play')
    stats = GameStats(ai_settings)
    ship = Ship(screen, ai_settings)  # 创建飞船实例
    bullets = Group()                 # 精灵模块中的Group类，bullets实例用于编组所以的bullet实例，类似列表
    aliens = Group()
    gf.creat_fleet(ai_settings, screen, ship, aliens)  # ship用于计算各行，列能放多少外星人
    while True:
        gf.check_events(ai_settings, screen, ship, aliens, bullets, stats, play_button)  # 这里面创建bullet实例加入bullets编组，改ship的rect属性
        if stats.game_active:
            ship.update()                   # 更新飞船位置
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens)   # 更新子弹位置，并删除编组中到达边缘的子弹
                        # 删除碰撞的飞船子弹,外星人打完了重新创建一批,并且aliens，bullets，ship的速度属性都提升了

            gf.update_aliens(ai_settings, screen, ship, aliens, bullets, stats)
        # 检查aliens边缘，更新aliens左右位置，检测外星人与飞船是否碰撞，到达底部，若是则子弹，外星人清空，重新创建aliens，减一条命
        # 三条命用完了，就无法再创建aliens，游戏状态改成非活跃
        gf.update_screen(ai_settings, screen, ship, bullets, aliens, stats, play_button) # 上面的实例要以参数形势传递

run_game()