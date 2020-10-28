import pygame
from .tower import Tower
import os
import math
import time
from menu.menu import Menu

menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/menu/", "red_menu.png")),(171, 50))
upgrade_btn = pygame.image.load(os.path.join("game_assets/menu/", "upgrade_btn.png"))

# load base tower images and animation images 6
base_imgs6 = []
animation_imgs6 = []
for x in range(0,3):
    base_imgs6.append(pygame.image.load(os.path.join("game_assets/fortress/fortress_base", str(x) + ".png" )))
for x in range(0,3):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    animation_imgs6.append(pygame.image.load(os.path.join("game_assets/fortress/fortress_animation", "0" + add_str + ".png" )))

class Fortress(Tower):
    """
    Add extra range to each surrounding tower
    """
    def __init__(self, x, y):
        super().__init__(x,y)
        self.range = 60
        self.effect = [100, 200, 400]
        self.price = [400, 750, 9999]
        self.menu = Menu(self, self.x, self.y, menu_bg, self.price)
        self.menu.add_btn(upgrade_btn, "Upgrade")
        self.base_imgs = base_imgs6[:]
        self.animation_imgs = animation_imgs6[:]
        self.width = 40
        self.height = 44
        self.name = "fortress"
        self.max_health = 500
        self.health = self.max_health
        self.collapse = False

    def get_upgrade_cost(self):
        """
        gets the upgrade cost
        :return: int
        """
        return self.menu.get_item_cost()

    def resist(self, enemy):
        """
        will resist according to health and nearby enemies
        :param towers: list
        :return: None
        """
        if enemy.name == "wei_catapult":
            coef = 2
        elif enemy.name == "wei_balista":
            coef = 2
        else:
            coef = 1
        self.health -= 1*coef
        if self.health <= 0:
            return False
        return True

    def draw(self, win):
        """
        draw the fortress base and fortress
        :param win: surface
        :return: int
        """
        super().draw_radius(win)
        super().draw(win)

        fortress = self.animation_imgs[self.level-1]
        add_x = 2
        add_y = 5
        win.blit(fortress, ((self.x - fortress.get_width()/2 + add_x), (self.y - fortress.get_height()/2 - add_y)))
        self.draw_health_bar(win)

    def draw_health_bar(self, win):
        """
        draw health bar above enemy
        :param win: surface
        :return: None
        """
        length = 30

        health_bar = length*(1-((self.max_health-self.health)/self.max_health))
        add_y = 5
        pygame.draw.rect(win, (255, 26, 26), (self.x - 13, self.y - 55 + add_y, length, 5), 0) # red rectangle
        pygame.draw.rect(win, (102, 255, 51), (self.x - 13, self.y - 55 + add_y, health_bar, 5), 0) # green rectangle
        pygame.draw.rect(win, (77, 77, 77), (self.x - 13, self.y - 55 + add_y, health_bar, 5), 1) # grey rectangle border
