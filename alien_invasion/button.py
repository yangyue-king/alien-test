import pygame.font    # 导入模块pygame.font
class Button():
    def __init__(self, ai_settings, screen, msg):       # msg为要显示的文本
        self.screen = screen
        self.screen_rect = self.screen.get_rect()       # 获得屏幕属性

        self.width, self.height = 200, 50               # 按钮尺寸，颜色
        self.button_color = (0, 255, 0)

        self.text_color = (255, 255, 255)               # 文本颜色

        self.font = pygame.font.SysFont(None, 48)       # none选择默认字体，48为文本字号
                                                        # 相当于字体对象

        self.rect = pygame.Rect(0, 0, self.width, self.height)      # 创建一个矩形图像

        self.rect.center = self.screen_rect.center                  # 将矩形按钮 图像放在屏幕中间
        self.prep_msg(msg)

    # 这个方法将文本渲染为图像并 放在按钮上
    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        # render是字体类的类方法，参数为 文本，抗锯齿，文本颜色，按钮背景色
        # render方法将msg文本渲染为   文本图像

        self.msg_image_rect = self.msg_image.get_rect()     # 获得图像属性
        self.msg_image_rect.center = self.rect.center       # 将文本图像放在按钮区域 中间

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)      # 屏幕实例的fill方法在屏幕特定区域画颜色

        # 将  文本图像  msg_image   看成和飞船一样的   图片对象
        self.screen.blit(self.msg_image, self.msg_image_rect)