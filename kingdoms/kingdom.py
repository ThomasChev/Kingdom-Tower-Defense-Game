import pygame

class Kingdom:
    """
    Abstract class for towers
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.img = None
        self.selected = False
        # self.width = 0
        # self.height = 0

    def draw (self, win):
        """
        draws the kingdoms' base cities
        :param win: surface
        :return: None
        """
        win.blit(self.img, (self.x - self.img.get_width() // 2, self.y - self.img.get_height() // 2))

        # draw other
        if self.selected:
            pass
            # self.menu.draw(win)