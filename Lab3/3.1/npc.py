from pygame import *
MOVE_SPEED = 10
WIDTH = 10
HEIGHT = 10
COLOR = '#ff0033'


class NPC(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.startX = x
        self.startY = y
        self.rect = Rect(x, y, WIDTH, HEIGHT)
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
