import pygame
from .tower import Tower
import os
import math
import time
from menu.menu import Menu

menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/menu/", "red_menu.png")),(171, 50))
upgrade_btn = pygame.image.load(os.path.join("game_assets/menu/", "upgrade_btn.png"))
sell_btn = pygame.image.load(os.path.join("game_assets/menu/", "sell_btn.png"))

# load base tower images 4
base_imgs4 = []
for x in range(0,3):
    base_imgs4.append(pygame.image.load(os.path.join("game_assets/support_towers/ten_base", str(x) + ".png" )))

class TenTower(Tower):
    """
    Add extra range to each surrounding tower
    """
    def __init__(self, x, y):
        super().__init__(x,y)
        self.range = 60
        self.effect = [0.1, 0.2, 0.3]
        self.menu = Menu(self, self.x, self.y, menu_bg, self.price)
        self.menu.add_btn(upgrade_btn, "Upgrade")
        self.menu.add_btn(sell_btn, "Sell")
        self.base_imgs = base_imgs4[:]
        self.width = 40
        self.height = 44
        self.name = "ten"
        self.sell_price = [100, 135, 260]
        self.price = [180, 350, 9999]

    def get_upgrade_cost(self):
        """
        gets the upgrade cost
        :return: int
        """
        return self.menu.get_item_cost()

    def draw(self, win):
        # super().draw_radius(win)
        super().draw_rectangle(win)
        super().draw(win)

    def support(self, towers):
        """
        will modify towers according to abillity
        :param towers: list
        :return: None
        """
        effected = []
        for tower in towers:
            x = tower.x
            y = tower.y

            dis = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

            if dis <= self.range + tower.width/2:
                effected.append(tower)

        for tower in effected:
            tower.range = tower.original_range + round(tower.range * self.effect[self.level -1])

# load base tower images 5
base_imgs5 = []
for x in range(0,3):
    base_imgs5.append(pygame.image.load(os.path.join("game_assets/support_towers/kyoukai_base", str(x) + ".png" )))

class KyoukaiTower(TenTower):
    """
    add damage to surrounding towers
    """
    def __init__(self, x, y):
        super().__init__(x,y)
        self.range = 60
        self.base_imgs = base_imgs5[:]
        self.effect = [1, 2, 3]
        self.menu = Menu(self, self.x, self.y, menu_bg, self.price)
        self.menu.add_btn(upgrade_btn, "Upgrade")
        self.menu.add_btn(sell_btn, "Sell")
        self.name = "kyoukai"
        self.sell_price = [100, 135, 260]
        self.price = [180, 350, 9999]

    def support(self, towers):
        """
        will modify towers according to ability
        :param towers: list
        :return: None
        """
        effected = []
        for tower in towers:
            x = tower.x
            y = tower.y

            dis = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

            if dis <= self.range + tower.width/2:
                effected.append(tower)

        for tower in effected:
            tower.damage = tower.original_damage + round(tower.original_damage * self.effect[self.level -1])


# load base tower images 6
base_imgs6 = []
for x in range(0,3):
    base_imgs6.append(pygame.image.load(os.path.join("game_assets/support_towers/ryo_base", str(x) + ".png" )))

class RyoTower(TenTower):
    """
    enhance rewards surrounding towers
    """
    def __init__(self, x, y):
        super().__init__(x,y)
        self.range = 100
        self.base_imgs = base_imgs6[:]
        self.effect = [1, 2, 3]
        self.menu = Menu(self, self.x, self.y, menu_bg, self.price)
        self.menu.add_btn(upgrade_btn, "Upgrade")
        self.menu.add_btn(sell_btn, "Sell")
        self.name = "ryo"
        self.sell_price = [100, 135, 260]
        self.price = [180, 350, 9999]

    def support(self, towers):
        """
        will modify towers according to ability
        :param towers: list
        :return: None
        """
        effected = []
        for tower in towers:
            x = tower.x
            y = tower.y

            dis = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

            if dis <= self.range + tower.width/2:
                effected.append(tower)

        for tower in effected:
            for i in range(1,3):
                tower.distribution[i] = tower.original_distribution[i] + round(tower.original_distribution[i] * self.effect[self.level -1], 3)
            tower.distribution[0] = 1 - (tower.distribution[1] + tower.distribution[2])