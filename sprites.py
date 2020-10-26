from settings_imports import *


class textblock(pg.sprite.Sprite):
    def __init__(self, x, y, word_w, word_h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((word_w + 5, word_h))
        self.image.fill((50, 175, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


