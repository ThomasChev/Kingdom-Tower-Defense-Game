import pygame
import os
import math
import random
import time
from .tower import Tower
from menu.menu import Menu

menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/menu/", "red_menu.png")),(171, 50))
upgrade_btn = pygame.image.load(os.path.join("game_assets/menu/", "upgrade_btn.png"))
sell_btn = pygame.image.load(os.path.join("game_assets/menu/", "sell_btn.png"))
img_dir = "game_assets/quin_towers/"

# load base tower images and animation images 1
base_imgs1 = []
animation_imgs1 = []
base_imgs1 = [pygame.image.load(os.path.join(img_dir, f"shin_base/{i}.png")) for i in range(0,3)]
animation_imgs1 = [pygame.image.load(os.path.join(img_dir, f"shin_animation/00{i}.png")) if i <=9 else pygame.image.load(os.path.join(img_dir, f"shin_animation/0{i}.png")) for i in range(0,24)]

class ShinTower(Tower):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.base_imgs = base_imgs1[:]
        self.animation_imgs = animation_imgs1[:]
        self.animation_count = 0
        self.range = 85
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
        self.sell_price = [30, 80, 200]
        self.price = [100, 300, 9999]
        self.distribution = [0.89, 0.1, 0.01]
        self.original_distribution = self.distribution[:]
        self.gold_drop = 0
        self.coord = (0, 0)
        self.speed = 4
        self.attacked_enemy = None

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
            if self.animation_count >= len(self.animation_imgs) * (5-self.speed):
                self.animation_count = len(self.animation_imgs)
        else:
            self.animation_count = 0

        shin = self.animation_imgs[self.animation_count // (5-self.speed)]
        add_x = 2
        add_y = 5
        win.blit(shin, ((self.x - shin.get_width()/2 + add_x), (self.y - shin.get_height()/2 - add_y)))

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
        self.attacked_enemy = None
        self.gold_drop = 0

        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
            x = enemy.x
            y = enemy.y - 36
            dis = math.sqrt((self.x - x)**2 + (self.y - y)**2)
            if dis < self.range:
                self.inRange = True
                enemy_closest.append(enemy)

        enemy_closest.sort(key=lambda x: x.path_pos)
        enemy_closest = enemy_closest[::-1]
        if len(enemy_closest) > 0:
            first_enemy = enemy_closest[0]

            if self.animation_count == len(self.animation_imgs):

                if self.name == "ouhon":
                    if not first_enemy.frozen:
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound(os.path.join("game_assets/sounds/", self.sound)), maxtime=600)
                        first_enemy.frozen = True
                        first_enemy.vel = first_enemy.vel/self.freeze_power
                else:
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound(os.path.join("game_assets/sounds/", self.sound)), maxtime=600)

                if first_enemy.hit(self.damage, self.name) == True:
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound(os.path.join("game_assets/sounds/", first_enemy.sound)), maxtime=600)
                    
                    # give money, drop reward (low probability), remove died enemy
                    self.attacked_enemy = first_enemy
                    money = first_enemy.money * 2
                    self.random_reward(first_enemy)
                    if self.gold_drop > 0:
                        self.coord = (first_enemy.x, first_enemy.y)
                    enemies.remove(first_enemy)
        
        return money

    def random_reward(self, enemy):
        """
        Return an amount of reward, with low probability
        :return: 1-sized list   
        """
        gold_list = [0, enemy.money, enemy.money*3]
        drop = random.choices(gold_list, self.distribution)
        self.gold_drop = drop[0]
        return self.gold_drop

# load base tower images and animation images 2
base_imgs2 = []
animation_imgs2 = []
base_imgs2 = [pygame.image.load(os.path.join(img_dir, f"moubu_base/{i}.png")) for i in range(0,3)]
animation_imgs2 = [pygame.image.load(os.path.join(img_dir, f"moubu_animation/00{i}.png")) if i <=9 else pygame.image.load(os.path.join(img_dir, f"moubu_animation/0{i}.png")) for i in range(0,26)]


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
        self.sell_price = [90, 150, 200]
        self.price = [180, 300, 9999]
        self.distribution = [0.89, 0.1, 0.01]
        self.original_distribution = self.distribution[:]

# load base tower images and animation images 3
base_imgs3 = []
animation_imgs3 = []
base_imgs3 = [pygame.image.load(os.path.join(img_dir, f"kanki_base/{i}.png")) for i in range(0,3)]
animation_imgs3 = [pygame.image.load(os.path.join(img_dir, f"kanki_animation/00{i}.png")) if i <=9 else pygame.image.load(os.path.join(img_dir, f"kanki_animation/0{i}.png")) for i in range(0,17)]


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
        self.sell_price = [60, 100, 200]
        self.price = [120, 250, 9999]
        self.distribution = [0.89, 0.1, 0.01]


# load base tower images and animation images 4
base_imgs4 = []
animation_imgs4 = []
base_imgs4 = [pygame.image.load(os.path.join(img_dir, f"ouhon_base/{i}.png")) for i in range(0,3)]
animation_imgs4 = [pygame.image.load(os.path.join(img_dir, f"ouhon_animation/00{i}.png")) if i <=9 else pygame.image.load(os.path.join(img_dir, f"ouhon_animation/0{i}.png")) for i in range(0,55)]


class OuhonTower(ShinTower):
    def __init__(self, x,y):
        super().__init__(x, y)
        self.base_imgs = base_imgs4[:]
        self.animation_imgs = animation_imgs4[:]
        self.animation_count = 0
        self.range = 65
        self.original_range = self.range
        self.inRange = False
        self.left = True
        self.damage = 0
        self.freeze_power = 2
        self.original_damage = self.damage
        self.menu = Menu(self, self.x, self.y, menu_bg, self.price)
        self.menu.add_btn(upgrade_btn, "Upgrade")
        self.menu.add_btn(sell_btn, "Sell")
        self.sound = "ice.wav"
        self.name = "ouhon"
        self.sell_price = [100, 150, 200]
        self.price = [200, 300, 9999]
        self.distribution = [0.89, 0.1, 0.01]
        self.original_distribution = self.distribution[:]