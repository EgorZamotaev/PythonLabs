from pygame import *
PLATFORM_WIDTH = 10
PLATFORM_HEIGHT = 10
PLATFORM_COLOR = "#ffffff"
WIN_WIDTH = 1010  # Ширина создаваемого окнa
WIN_HEIGHT = 1010  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#FA8072"
BUTTON_COLOR = "#412227"


class Finish(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

    def collaid(self, hero, stepc):
        ms = 'k'
        if sprite.collide_rect(self, hero):
            sc = display.set_mode(DISPLAY)

            bg = Surface(DISPLAY)
            bg.fill(Color(BACKGROUND_COLOR))
            sc.blit(bg, (0, 0))

            f1 = font.Font(None, 40)
            text1 = f1.render('GAME OVER', 1, (64, 34, 39))
            text2 = f1.render('number of steps:', 1, (64, 34, 39))
            text3 = f1.render(str(stepc), 1, (64, 34, 39))
            sc.blit(text1, (427, 450))
            sc.blit(text2, (390, 500))
            sc.blit(text3, (630, 500))

            x = 422
            y = 800
            width = 165
            height = 45
            cur = mouse.get_pos()
            click = mouse.get_pressed()
            if x + width > cur[0] > x and y + height > cur[1] > y:
                draw.rect(sc, (0, 0, 0), (x, y, width, height))
                text4 = f1.render('NEW GAME', 1, (250, 128, 114))
                sc.blit(text4, (427, 810))
                if click[0] == 1:
                    ms = 'kek'

            else:
                draw.rect(sc, (65, 34, 39), (x, y, width, height))
                text4 = f1.render('NEW GAME', 1, (250, 128, 114))
                sc.blit(text4, (427, 810))

        return ms