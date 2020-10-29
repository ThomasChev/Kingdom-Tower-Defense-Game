import pygame
from .tower import Tower
import os
import math
import time
from menu.menu import Menu

menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/menu/", "red_menu.png")),(171, 50))
upgrade_btn = pygame.image.load(os.path.join("game_assets/menu/", "upgrade_btn.png"))
sell_btn = pygame.image.load(os.path.join("game_assets/menu/", "sell_btn.png"))

# load base tower images and animation images 1
base_imgs1 = []
animation_imgs1 = []
for x in range(0,3):
    base_imgs1.append(pygame.image.load(os.path.join("game_assets/quin_towers/shin_base", str(x) + ".png" )))
for x in range(0,24):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    animation_imgs1.append(pygame.image.load(os.path.join("game_assets/quin_towers/shin_animation", "0" + add_str + ".png" )))

class ShinTower(Tower):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.base_imgs = base_imgs1[:]
        self.animation_imgs = animation_imgs1[:]
        self.animation_count = 0
        self.range = 75
        self.original_range = self.range
        self.inRange = False
        self.left = True
        self.timer = time.time()
        self.damage = 1
        self.original_damage = self.damage
        self.width = 40
        self.height = 44
        self.menu = Menu(self, self.x, self.y, menu_bg, self.price)
        self.menu.add_btn(upgrade_btn, "Upgrade")
        self.menu.add_btn(sell_btn, "Sell")
        self.moving = False
        self.sound = "sword.wav"
        self.name = "shin"
        self.sell_price = [15, 75, 225]
        self.price = [100, 300, 9999]

    def get_upgrade_cost(self):
        """
        gets the upgrade cost
        :return: int
        """
        return self.menu.get_item_cost()
    
    def draw(self, win):
        """
        draw the shin tower base and animated shin
        :param win: surface
        :return: int
        """
        super().draw_radius(win)
        super().draw(win)

        if self.inRange and not self.moving:
            self.animation_count += 1
            if self.animation_count >= len(self.animation_imgs) * 4:
                self.animation_count = len(self.animation_imgs)
        else:
            self.animation_count = 0

        shin = self.animation_imgs[self.animation_count // 4]

        # if self.left == True:
        #     add = -15
        # else:
        #     add = -shin.get_width() + 10
        # # win.blit(shin, ((self.x + add), (self.y - shin.get_height()-15)))
        # (shin)
        add_x = 2
        add_y = 5
        win.blit(shin, ((self.x - shin.get_width()/2 + add_x), (self.y - shin.get_height()/2 - add_y)))
        # pygame.draw.circle(win, (0, 255, 0), (self.x+12, self.y+25), self.range, 1)

    def change_range(self, r):
        """
        change range of shin tower
        :param r: int
        :return: None
        """
        self.range = r

    def attack(self, enemies):
        """
        attacks an enemy in the enemy list, modifies the list
        :param enemies: list of enemies
        :return: None
        """
        money = 0
        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
            correction = math.sqrt(2)
            x = enemy.x
            y = enemy.y - 36
            # dis = math.sqrt((self.x - enemy.img.get_width() / 2 - x) ** 2 + (self.y - enemy.img.get_height() / 2 - y) ** 2)
            dis = math.sqrt((self.x - x)**2 + (self.y - y)**2)
            if dis < self.range:
                self.inRange = True
                enemy_closest.append(enemy)

        enemy_closest.sort(key=lambda x: x.path_pos)
        enemy_closest = enemy_closest[::-1]
        if len(enemy_closest) > 0:
            first_enemy = enemy_closest[0]

            if self.animation_count == len(self.animation_imgs):
                pygame.mixer.Channel(1).play(pygame.mixer.Sound(os.path.join("game_assets/sounds/", self.sound)), maxtime=600)
                # self.timer = time.time()
                if first_enemy.hit(self.damage) == True:
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound(os.path.join("game_assets/sounds/", first_enemy.sound)), maxtime=600)
                    money = first_enemy.money * 2
                    enemies.remove(first_enemy)

        return money

# load base tower images and animation images 2
base_imgs2 = []
animation_imgs2 = []
for x in range(0,3):
    base_imgs2.append(pygame.image.load(os.path.join("game_assets/quin_towers/moubu_base", str(x) + ".png" )))
for x in range(0,26):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    animation_imgs2.append(pygame.image.load(os.path.join("game_assets/quin_towers/moubu_animation", "0" + add_str + ".png" )))


class MoubuTower(ShinTower):
    def __init__(self, x,y):
        super().__init__(x, y)
        self.base_imgs = base_imgs2[:]
        self.animation_imgs = animation_imgs2[:]
        self.animation_count = 0
        self.range = 65
        self.original_range = self.range
        self.inRange = False
        self.left = True
        self.damage = 2
        self.original_damage = self.damage
        self.menu = Menu(self, self.x, self.y, menu_bg, self.price)
        self.menu.add_btn(upgrade_btn, "Upgrade")
        self.menu.add_btn(sell_btn, "Sell")
        self.sound = "club.wav"
        self.name = "moubu"
        self.sell_price = [45, 75, 225]
        self.price = [100, 300, 9999]

# load base tower images and animation images 3
base_imgs3 = []
animation_imgs3 = []
for x in range(0,3):
    base_imgs3.append(pygame.image.load(os.path.join("game_assets/quin_towers/kanki_base", str(x) + ".png" )))
for x in range(0,17):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    animation_imgs3.append(pygame.image.load(os.path.join("game_assets/quin_towers/kanki_animation", "0" + add_str + ".png" )))

class KankiTower(ShinTower):
    def __init__(self, x,y):
        super().__init__(x, y)
        self.base_imgs = base_imgs3[:]
        self.animation_imgs = animation_imgs3[:]
        self.animation_count = 0
        self.range = 65
        self.original_range = self.range
        self.inRange = False
        self.left = True
        self.damage = 1
        self.original_damage = self.damage
        self.menu = Menu(self, self.x, self.y, menu_bg, self.price)
        self.menu.add_btn(upgrade_btn, "Upgrade")
        self.menu.add_btn(sell_btn, "Sell")
        self.sound = "sword2.wav"
        self.name = "kanki"
        self.sell_price = [30, 75, 225]
        self.price = [100, 300, 9999]