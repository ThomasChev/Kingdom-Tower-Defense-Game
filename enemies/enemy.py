import pygame
import math
import random
import os
from game_assets.colors import rgb

img_dir = "game_assets/enemies/"
ices = []
ices = [pygame.image.load(os.path.join(img_dir, f"freeze/{i}.png")) for i in range(0,56)]
img_pres = pygame.transform.scale(pygame.image.load(os.path.join(img_dir, "intro/intro_warrior.png")),(120, 120))


class Enemy:

    def __init__(self):
        self.width = 64
        self.height = 64
        self.animation_count = 0
        self.ice_count = 0
        self.health = 1
        self.img = None
        self.dis = 0
        self.path_pos = 0
        self.move_dist = 0
        self.imgs = []
        self.flipped = False
        self.flip_again = False
        self.flip_first = True # True for right to left maps
        self.max_health = 0
        self.block = False
        self.frozen = False
        self.speed = 1 # game speed
        self.shield = 2
        # kanki affects wei, moubu affects chu, shin affects riboku by +20%
        self.chu_special = ["chu_warrior", "chu_elephant", "chu_boat"]
        self.wei_special = ["wei_catapult", "wei_balista"]
        self.zao_special = ["zao_riboku"]
        self.rate = 1.5
        self.intro = img_pres
        self.type = "warrior"

    def draw(self, win):
        """
        Draws the enemy with the given images
        :param win: surface
        :return: None
        """
        # for dot in self.path:
        # 	pygame.draw.circle(win, (255,0,0), dot, 5, 1)
        self.img = self.imgs[self.animation_count]
        ice = ices[self.ice_count]
        win.blit(self.img, (self.x - self.img.get_width() / 2, self.y - self.img.get_height() / 2 - 35))

        # draw ice when hit by OuhonTower
        if self.frozen:
            win.blit(ice, (self.x - ice.get_width() / 2, self.y - ice.get_height() / 2 - 35))
            
        self.draw_health_bar(win)

    def draw_health_bar(self, win):
        """
        draw health bar above enemy
        :param win: surface
        :return: None
        """
        length = 30
        health_bar = length*(1-((self.max_health-self.health)/self.max_health))
        if self.name =="zao_riboku":
            add_y = -10
        else:
            add_y = 0
        pygame.draw.rect(win, rgb(255, 26, 26), (self.x - 13, self.y - 55 + add_y, length, 5), 0) # attacked rectangle
        pygame.draw.rect(win, rgb(102, 255, 51), (self.x - 13, self.y - 55 + add_y, health_bar, 5), 0) # health rectangle
        pygame.draw.rect(win, rgb(77, 77, 77), (self.x - 13, self.y - 55 + add_y, health_bar, 5), 1) # rectangle border

    def move(self):
        """
        Move enemy
        :return: None
        """
        if not self.block:
            
            # animation counters
            self.animation_count += 1
            if self.animation_count >= len(self.imgs):
                self.animation_count = 0
            self.ice_count += 1
            if self.ice_count >= len(ices):
                self.ice_count = 0

            # To move object1 to object2:
            if self.path_pos + 1 >= len(self.path):
                x2, y2 = (-10, 346)
            else:
                x2, y2 = self.path[self.path_pos+1]
            # distances between objects
            dx = x2 - self.x
            dy = y2 - self.y
            # actual distance between objects(direct line)
            d = math.sqrt(dx** 2 + dy** 2)
            # calculate the distance allowed to move
            normal = (0.3*self.vel/d)*self.speed
            # finally move
            self.x = self.x + dx*normal
            self.y = self.y + dy*normal

            # 1st flip for right to left maps
            if self.flip_first:
                self.flip_first = False
                self.flipped = False
                for x, img in enumerate(self.imgs):
                    self.imgs[x] = pygame.transform.flip(img, True, False)

            # flips when change direction
            if dx < 0 and not (self.flipped) and self.flip_first:
                self.flipped = True
                self.flip_again = True
                for x, img in enumerate(self.imgs):
                    self.imgs[x] = pygame.transform.flip(img, True, False)

            if dx > 0 and (self.flip_again or not (self.flip_first)):
                self.flip_again = False
                self.flipped = False
                self.flip_first = True
                for x, img in enumerate(self.imgs):
                    self.imgs[x] = pygame.transform.flip(img, True, False)

            # Go to next point
            if dx >= 0:  # moving right
                if dy >= 0:  # moving down
                    if self.x >= x2 and self.y >= y2:
                        self.path_pos += 1
                        self.x, self.y = self.path[self.path_pos]
                else:
                    if self.x >= x2 and self.y <= y2:
                        self.path_pos += 1
                        self.x, self.y = self.path[self.path_pos]
            else:  # moving left
                if dy >= 0:  # moving down
                    if self.x <= x2 and self.y >= y2:
                        self.path_pos += 1
                        self.x, self.y = self.path[self.path_pos]
                else:
                    if self.x <= x2 and self.y <= y2:
                        self.path_pos += 1
                        self.x, self.y = self.path[self.path_pos]

    def hit(self, damage, tower):
        """
        Returns if an enemy has died and removes health each call
        based on tower damage and special ability
        :return: Bool
        """
        # kanki affects wei, moubu affects chu, shin affects riboku by +20%
        if tower == "kanki" and self.name in self.wei_special:
            coef = 1.2
        elif tower == "moubu" and self.name in self.chu_special:
            coef = 1.2
        elif tower == "shin" and self.name in self.zao_special:
            coef = 1.2
        else:
            coef = 1
        self.health -= damage*coef/self.shield
        self.health = self.truncate(self.health)

        if self.health <= 0:
            return True
        return False

    def scale_health(self, wave):
        self.max_health += 0.01*wave**2 # health scaling with waves
        self.health = self.max_health

        # L = wave + 1
        # La = 0
        # Lb = 4
        # Lc = 6
        # Ld = 8
        # Da = self.init_max_health + 0/100 * self.init_max_health
        # Db = self.init_max_health + 20/100 * self.init_max_health
        # Dc = self.init_max_health + 80/100 * self.init_max_health
        # Dd = self.init_max_health + 110/100 * self.init_max_health
        # Gk = (Dc-Db)/(Lc-Lb)

        # if (L<=Lb):
        #     #Intro Phase
        #     self.max_health = Da + (Db-Da)/(L-La)
        # elif (L<=Lc):
        #     #Learning Phase
        #     self.max_health = Db + (Dc-Db)/(L-Lb)
        # elif (L<=Ld):
        #     #Progress Phase
        #     self.max_health = Dc + (Dd-Dc)/(L-Lc)
        # else:
        #     #Kill-off phase
        #     self.max_health = Dd + Gk*(L-Ld)

        # print("init_h", self.init_max_health)
        # print("max_health", self.max_health)

        # self.health = self.max_health

    def collide(self, otherTower):
        x2 = otherTower.x
        y2 = otherTower.y
        y2_corr = y2 + 34
        dis = math.sqrt((x2 - self.x)**2 + (y2_corr - self.y)**2)
        if otherTower.name == "fortress":
            if dis >= random.randrange(12,27):
                return False
            else:
                self.block = True
                return True

    def round_up(self, n, decimals=0):
        multiplier = 10 ** decimals
        return math.ceil(n * multiplier) / multiplier

    def truncate(self, n):
        return int(n * 10000) / 10000