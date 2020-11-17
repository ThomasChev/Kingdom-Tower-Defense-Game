import pygame
import os
from menu.menu import Menu, Button


class Kingdom:
    """
    Abstract class for towers
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.img = None
        self.selected = False
        self.width = 40
        self.height = 59
        self.range = 36
        self.tile_width = 36
        self.tile_height = 30
        self.sound = "kingdom.wav"
        self.price = [0, 0, 0]
        # self.menu = Menu(self, self.x, self.y, menu_bg, self.price)

    def draw (self, win):
        """
        draws the kingdoms' base cities and surface
        :param win: surface
        :return: None
        """
        img = self.img
        win.blit(self.img, (self.x - img.get_width() // 2, self.y - img.get_height() // 2))

        # draws kigndom's zone tile by tile
        if self.selected:
            for elem in self.tile:
                x = elem[0]
                y = elem[1]
                if elem[1] >= 313:
                    y = elem[1] + 5 # correction for better display
                self.draw_tile(win, x, y)
    

    # draw single tile
    def draw_tile(self, win, X, Y):
        if self.selected:
            surface = pygame.Surface((self.range*4, self.range*4), pygame.SRCALPHA, 32)
            pygame.draw.rect(surface, self.rgb, (self.range, self.range, self.range, self.tile_height), 0)
            win.blit(surface, (X - 1.5*self.range, Y - self.range))

    def click (self, X, Y):
        """
        returns if tower has been clicked on
        and selects tower if it was clicked
        :param X: int
        :param Y: int
        :return: bool
        """
        img = self.img
        if X <= self.x - img.get_width()//2 + self.width and X >= self.x - img.get_width()//2:
            if Y <= self.y + self.height - img.get_height()//2 and Y >= self.y - img.get_height()//2:
                pygame.mixer.Channel(0).play(pygame.mixer.Sound(os.path.join("game_assets/sounds/", self.sound)))
                return True
        return False