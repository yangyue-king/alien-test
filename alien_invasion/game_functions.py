import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
def check_keydown_event(event, ai_settings, screen, ship, bullets):   #以中断事件event对ship属性作修改
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
            # ship.rect.centerx += 1
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
            # ship.rect.centerx -= 1
        elif event.key == pygame.K_SPACE:
            fire_bullet(ai_settings, screen, ship, bullets)
        elif event.key == pygame.K_q:
            sys.exit()
def check_keyup_event(event, ship):    # 以中断事件event对ship属性作修改
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        if event.key == pygame.K_LEFT:
            ship.moving_left = False
def check_events(ai_settings, screen, ship, aliens, bullets, stats, play_button):   # 函数里创建bullet实例，给编组bullets
    for event in pygame.event.get():  # 获得中断事件event
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and stats.game_active == False:   # 判断鼠标是否点在了按钮上
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, ship, aliens, bullets, stats, play_button, mouse_x, mouse_y)
        else:
            check_keydown_event(event, ai_settings, screen, ship, bullets)  # 判断keydown
            check_keyup_event(event, ship)    # 判断keyup


def check_play_button(ai_settings, screen, ship, aliens, bullets, stats, play_button, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):    # 检测点是否在一个区域里   play_button实例的rect属性是外面的框
        stats.game_active = True
        stats.reset_stats()       # 重新加命
        aliens.empty()
        bullets.empty()
        creat_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)



def update_screen(ai_settings, screen, ship, bullets, aliens, stats, play_button):  # 4个实例传递参数  bullets为编组
    screen.fill(ai_settings.bg_color)    # 颜色填充
    ship.blitme()
    for alien in aliens.sprites():
        alien.blitme()
                                        # 飞船按照自己的rect属性画好  while里面更新屏幕内容
    for bullet in bullets.sprites():
        bullet.draw_bullet()             # 子弹实例按照自己的属性画好
    if not stats.game_active:
        play_button.draw_button()          # 游戏状态为非活跃时显示按钮
    pygame.display.flip()               # 更新屏幕



def update_bullets(ai_settings, screen, ship, bullets, aliens):
    bullets.update()  # 对整个bullets编组进行操作，精灵的Group功能  这里必须是update
    for bullet in bullets.copy():  # 这里遍历编组bullets的副本，到达边缘的子弹删除，避免浪费空间
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
#       print(len(bullets))
    check_bullet_alien_collisions(ai_settings, screen, ship, bullets, aliens)
def check_bullet_alien_collisions(ai_settings, screen, ship, bullets, aliens):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)  # 将碰撞的飞船子弹删除
    if len(aliens) == 0:
        bullets.empty()     # 外星人打完子弹也立刻消失

        ai_settings.increase_speed()   # 游戏提速，下面新创建的外星人速度属性就变了

        creat_fleet(ai_settings, screen, ship, aliens)



# 下面四个函数为创建外星人编组

def creat_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)  # 一行可以放多少个外星人
    number_rows = get_numbe_rows(ai_settings, ship.rect.height, alien.rect.height)  #计算的行数
    for number_row in range(number_rows):     # 在行列里都安排上外星人
        for alien_number in range(number_aliens_x):
            creat_alien(ai_settings, screen, aliens, alien_number, number_row)
def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x                                      # 计算一行放多少个外星人
def get_numbe_rows(ai_settings, ship_height, alien_height):
    available_space_y = ai_settings.screen_height - 3*alien_height - ship_height
    numbers_rows = int(available_space_y / (2*alien_height))
    return numbers_rows                                         # 计算可以放多少行外星人
def creat_alien(ai_settings, screen, aliens, alien_number, number_row):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2*alien_width*alien_number
    alien.y = alien_height + 2*alien_height*number_row
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)                           # 每一个外星人实例，经过修改位置属性，再加入编组


# 下面函数为控制外星人运动
def update_aliens(ai_settings, screen, ship, aliens, bullets, stats):
    check_alien_edges(ai_settings, aliens)
    aliens.update()      # 编组操作，每个外星人实例都调用类方法改变位置
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, ship, aliens, bullets, stats)
    check_aliens_bottom(ai_settings, screen, ship, aliens, bullets, stats)
# 第三次碰撞或到达底部，没命时，把游戏状态改称非活跃
def check_alien_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():                           # 有任何外星人到达边缘
            change_aliens_direction(ai_settings, aliens)  # 全部下降且改变方向
            break
def change_aliens_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.alien_drop_speed
        alien.change_alien_direction()
def ship_hit(ai_settings, screen, ship, aliens, bullets, stats):
    if stats.ship_left > 0:
        stats.ship_left -= 1     # stats实例中的外星人剩余数减一
        aliens.empty()
        bullets.empty()    # 清空外星人，子弹
        creat_fleet(ai_settings, screen, ship, aliens)   # 重新创建一批外星人放入aliens中
        ship.center_ship()
        sleep(1)
#       print(stats.ship_left)
    else:
        stats.game_active = False
def check_aliens_bottom(ai_settings, screen, ship, aliens, bullets, stats):
    screen_rect = screen.get_rect()         # 局部变量
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:  # 外星人实例属性
            ship_hit(ai_settings, screen, ship, aliens, bullets, stats)
            break     # 这里必须加break，不然多个外星人同时触底，三条命直接一次用完