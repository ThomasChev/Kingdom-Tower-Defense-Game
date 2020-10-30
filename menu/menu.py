import pygame
import os
from game_assets.colors import rgb
pygame.font.init()

class Button:
    """
    Button class for menu objects
    """
    def __init__(self, menu, img, name):
    # def __init__(self, x, y, img, name):
        self.name = name
        self.img = img
        self.x = menu.x - 75
        self.y = menu.y - 81
        self.menu = menu
        self.width = self.img.get_width()
        self.height = self.img.get_height()

    def click(self, X, Y):
        """
        returns if the positon has collided with the menu
        :param X: int
        :param Y: int
        :return: bool
        """
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    def draw(self, win):
        """
        draws the button image
        :param win: surface
        :return: None
        """
        win.blit(self.img, (self.x, self.y))

    def update(self, i):
        """
        updates button position
        :return: None
        """
        self.x = self.menu.x - 72 + i*80
        self.y = self.menu.y - 81


class PlayPauseButton(Button):
    def __init__(self, play_img, pause_img, x, y):
        self.img = play_img
        self.play = play_img
        self.pause = pause_img
        self.x = x
        self.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.paused = True

    def draw(self, win):
        if self.paused:
            win.blit(self.play, (self.x, self.y))
        else:
            win.blit(self.pause, (self.x, self.y))


class VerticalButton(Button):
    """
    Button class for menu objects
    """
    def __init__(self, x, y, img, name, cost):
        self.name = name
        self.img = img
        self.x = x
        self.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.cost = cost


class Menu:
    """
    menu for holding items
    """
    def __init__(self, tower, x, y, img, item_cost):
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.item_cost = item_cost
        self.buttons = []
        self.items = 0
        self.bg = img
        self.font = pygame.font.Font("game_assets/fonts/SF Atarian System.ttf", 16)
        self.tower = tower

    def add_btn(self, img, name):
        """
        adds buttons to menu
        :param img: surface
        :param name: str
        :return: None
        """
        self.items += 1
        # btn_x = self.x - 25
        # btn_y = self.y + (self.items-1)*74
        # self.buttons.append(Button(btn_x, btn_y, img, name, cost))
        self.buttons.append(Button(self, img, name))

    def get_item_cost(self):
        """
        gets cost of upgrade to next level
        :return: int
        """
        return self.item_cost[self.tower.level - 1]

    # def draw(self, win, dis):
    def draw(self, win):
        """
        draws btns and menu bg
        :param win: surface
        :return: None
        """
        win.blit(self.bg, (self.x - self.bg.get_width()/2, self.y - 90))
        for item in self.buttons:
            item.draw(win)
            if item.name =="Upgrade":
                upgrade_cost = "$ " + str(self.item_cost[self.tower.level - 1])
                text = self.font.render(upgrade_cost, 1, (255,255,255))
                # win.blit(text, (item.x + item.width + 30 - text.get_width()/2, item.y + star.get_height() -8))
                win.blit(text, (item.x + item.width + 20 - text.get_width()/2, item.y + 8))
            elif item.name == "Sell":
                sell_price = "$ " + str(self.tower.sell())
                text = self.font.render(sell_price, 1, (255,255,255))
                win.blit(text, (item.x + item.width + 18 - text.get_width()/2, item.y + 8))

    def get_clicked(self, X, Y):
        """
        return the clicked item from the menu
        :param X: int
        :param Y: int
        :return: str
        """
        for btn in self.buttons:
            if btn.click(X,Y):
                return btn.name
        return None

    def update(self):
        """
        update menu and button location
        :return: None
        """
        for i, btn in enumerate(self.buttons):
            btn.update(i)


class VerticalMenu(Menu):
    """
    Vertical Menu for side bar of game
    """
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.buttons = []
        self.items = 0
        self.bg = img
        self.font = pygame.font.Font("game_assets/fonts/SF Atarian System.ttf", 16)
        self.blink = False

    def add_btn(self, img, name, cost):
        """
        adds buttons to menu
        :param img: surface
        :param name: str
        :return: None
        """
        self.items += 1
        btn_x = self.x - 25
        btn_y = self.y + (self.items-1)*74
        self.buttons.append(VerticalButton(btn_x, btn_y, img, name, cost))

    def get_item_cost(self, name):
        """
        gets cost of item
        :param name: str
        :return: int
        """
        for btn in self.buttons:
            if btn.name == name:
                return btn.cost
        return -1

    def draw(self, win):
        """
        draws btns and menu bg
        :param win: surface
        :return: None
        """
        add_blink = 6
        if self.blink:
            win.blit(self.bg, (self.x - self.bg.get_width()/2 - 8, self.y - 12 + add_blink))
        else:
            win.blit(self.bg, (self.x - self.bg.get_width()/2 - 8, self.y - 12))
        
        for item in self.buttons:
            item.draw(win)
            text = self.font.render("$ " + str(item.cost), 1, rgb(255,255,255))
            win.blit(text, (item.x + item.width/2 - text.get_width()/2, item.y + item.height + 1))