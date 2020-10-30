import pygame
from menu.menu import Menu
from game_assets.colors import rgb
import os
import math

menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/menu/", "red_menu.png")),(171, 50))
upgrade_btn = pygame.image.load(os.path.join("game_assets/menu/", "upgrade_btn.png"))
sell_btn = pygame.image.load(os.path.join("game_assets/menu/", "sell_btn.png"))

tile_x = [4,60,100,140,180,220,260,300,340,380,420,460,500,540,580,620,660,700,740,780,820,860,900,940,980,1020,1060,1100,1140,1180]
tile_y = [40,74,108,142,176,210,244,279,313,349,383,417,453,489,523,559,593,627,661]
dict_tile = {}
dict_tile_fortress = {}
# create dict of tiles, set busy tiles to 1
for x in tile_x:
    for y in tile_y:
        key = (x, y)
        dict_tile[key] = 1
        dict_tile_fortress[key] = 1
# set available tiles to 0
tile_empty = [[340,40],[380,40],[500,40],[540,40],[580,40],[620,40],[660,40],[780,40],[820,40],[1060,40],[1100,40],[340,74],[380,74],[420,74],[460,74],[500,74],[580,74],[620,74],[660,74],[700,74],[780,74],[820,74],[860,74],[900,74],[940,74],[1100,74],[340,108],[380,108],[420,108],[460,108],[500,108],[620,108],[660,108],[700,108],[740,108],[780,108],[820,108],[860,108],[900,108],[100,142],[140,142],[180,142],[300,142],[340,142],[380,142],[420,142],[460,142],[500,142],[620,142],[660,142],[740,142],[780,142],[820,142],[860,142],[180,176],[220,176],[260,176],[300,176],[340,176],[380,176],[620,176],[660,176],[740,176],[780,176],[820,176],[860,176],[940,176],[1100,176],[220,210],[260,210],[300,210],[340,210],[380,210],[460,210],[660,210],[740,210],[780,210],[820,210],[860,210],[940,210],[1020,210],[1060,210],[1100,210],[220,244],[260,244],[300,244],[340,244],[380,244],[460,244],[940,244],[1020,244],[220,279],[260,279],[300,279],[340,279],[1020,279],[540,313],[580,313],[620,313],[700,313],[740,313],[780,313],[860,313],[900,313],[940,313],[1020,313],[100,349],[180,349],[220,349],[260,349],[340,349],[380,349],[420,349],[460,349],[540,349],[580,349],[620,349],[700,349],[740,349],[780,349],[100,383],[140,383],[180,383],[220,383],[260,383],[540,383],[580,383],[620,383],[700,383],[780,383],[820,383],[860,383],[900,383],[940,383],[980,383],[220,417],[260,417],[380,417],[420,417],[460,417],[500,417],[540,417],[580,417],[620,417],[700,417],[780,417],[820,417],[860,417],[900,417],[940,417],[980,417],[1020,417],[100,453],[140,453],[780,453],[820,453],[860,453],[900,453],[940,453],[980,453],[1020,453],[60,489],[100,489],[140,489],[180,489],[220,489],[340,489],[380,489],[420,489],[460,489],[500,489],[540,489],[580,489],[620,489],[660,489],[700,489],[740,489],[780,489],[820,489],[860,489],[900,489],[940,489],[980,489],[1020,489],[4,523],[60,523],[100,523],[140,523],[180,523],[220,523],[340,523],[380,523],[420,523],[460,523],[700,523],[740,523],[1020,523],[540,559],[580,559],[620,559],[180,593],[220,593],[980,593],[1020,593],[1060,593],[140,627],[260,627],[300,627],[340,627],[380,627],[420,627],[460,627],[500,627],[580,627],[620,627],[660,627],[700,627],[740,627],[780,627],[820,627],[900,627],[100,661],[140,661],[220,661],[260,661],[300,661],[340,661],[380,661],[420,661],[460,661],[500,661],[580,661],[620,661],[660,661],[700,661],[740,661],[780,661],[900,661]]
tile_empty_fortress = [[900,142],[940,142],[420,176],[460,176],[500,176],[700,176],[900,176],[420,210],[500,210],[700,210],[900,210],[420,244],[500,244],[540,244],[580,244],[620,244],[660,244],[700,244],[740,244],[780,244],[820,244],[860,244],[900,244],[420,279],[820,279],[60,313],[420,313],[460,313],[500,313],[820,313],[60,349],[500,349],[660,349],[820,349],[860,349],[900,349],[940,349],[980,349],[60,383],[340,383],[380,383],[420,383],[460,383],[500,383],[660,383],[60,417],[100,417],[140,417],[180,417],[340,417],[660,417],[740,417],[180,453],[220,453],[260,453],[300,453],[340,453],[380,453],[420,453],[460,453],[500,453],[540,453],[580,453],[620,453],[660,453],[700,453],[740,453],[260,489],[260,523],[260,559],[860,559],[900,559],[940,559],[260,593],[300,593],[340,593],[380,593],[420,593],[460,593],[500,593],[540,593],[580,593],[620,593],[660,593],[700,593],[740,593],[780,593],[820,593],[860,593],[940,593],[540,627],[940,627]]
for tile in tile_empty:
    x = tile[0]
    y = tile[1]
    key = (x, y)
    dict_tile[key] = 0
for tile in tile_empty_fortress:
    x = tile[0]
    y = tile[1]
    key = (x, y)
    dict_tile_fortress[key] = 0
# for key, value in dict_tile.items() :
#     print (key, value)

class Tower:
    """
    Abstract class for towers
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.sell_price = [0,0,0]
        self.price = [100, 300, 9999]
        self.level = 1
        self.selected = False
        self.menu = Menu(self, self.x, self.y, menu_bg, self.price)
        self.menu.add_btn(upgrade_btn, "Upgrade")
        self.menu.add_btn(sell_btn, "Sell")
        self.base_imgs = []
        self.animation_imgs = []
        self.damage = 1

    def draw (self, win):
        """
        draws the tower
        :param win: surface
        :return: None
        """
        img = self.base_imgs[self.level-1]
        # find the closest tile
        self.x = min(tile_x, key=lambda x:abs(x-self.x))
        self.y = min(tile_y, key=lambda y:abs(y-self.y))
        tile_key = (self.x, self.y)
        if self.name == "fortress":
            if dict_tile_fortress[tile_key] == 0:
                win.blit(img, (self.x - img.get_width() // 2, self.y - img.get_height() // 2))
        else:
            if dict_tile[tile_key] == 0:
                win.blit(img, (self.x - img.get_width() // 2, self.y - img.get_height() // 2))

        # draw menu
        # print("tower self.y: ", self.y)
        if self.selected:
            #self.menu.draw(win, self.range)
            self.menu.draw(win)

    def draw_radius(self, win):
        if self.selected:
            # draw range circle
            size = (self.range*2, self.range*2)
            radius = self.range
            surface = pygame.Surface(size, pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, rgb(204,255,255), (radius, radius), radius, 0)
            win.blit(surface, (self.x - radius, self.y - radius))
            
    def draw_rectangle(self, win):
        if self.selected:
            # draw range rectangle
            surface = pygame.Surface((self.range*4, self.range*4), pygame.SRCALPHA, 32)
            pygame.draw.rect(surface, rgb(204,255,255), (self.range*2, self.range*2, self.range*2, self.range*1.8), 0)
            win.blit(surface, (self.x - 3*self.range, self.y - 2.6*self.range))

    # def draw_placement(self,win):
    #     # draw range circle
    #     surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
    #     pygame.draw.circle(surface, self.place_color, (50,50), 50, 0)

    #     win.blit(surface, (self.x - 50, self.y - 50))

    def click (self, X, Y):
        """
        returns if tower has been clicked on
        and selects tower if it was clicked
        :param X: int
        :param Y: int
        :return: bool
        """
        img = self.base_imgs[self.level - 1]
        if X <= self.x - img.get_width()//2 + self.width and X >= self.x - img.get_width()//2:
            if Y <= self.y + self.height - img.get_height()//2 and Y >= self.y - img.get_height()//2:
                return True
        return False

    def sell (self):
        """
        call to sell the tower, returns sell price
        :return: int
        """
        return self.sell_price[self.level-1]

    def upgrade (self):
        """
        upgrades the tower for a given cost
        :return: None
        """
        if self.name == "fortress":
            if self.level < len(self.animation_imgs):
                self.level += 1
                self.max_health += self.max_health
                self.health += self.health
        else:
            if self.level < len(self.base_imgs):
                self.level += 1
                self.damage += 1

    def get_upgrade_cost(self):
        """
        returns the upgrade cost, if 0 then can't upgrade anymore
        :return: int
        """
        return self.price[self.level-1]

    def move (self, x , y):
        """
        moves tower to given x and y
        :param x: int
        :param y: int
        :return: None
        """
        self.x = x
        self.y = y
        self.menu.x = x
        self.menu.y = y
        self.menu.update()

    def collide(self, otherTower):
        x2 = otherTower.x
        y2 = otherTower.y

        # find closest tile
        x2 = min(tile_x, key=lambda x:abs(x-x2)) # set x2 at the x coordinate of tyle_x which has the minimum distance from x2
        y2 = min(tile_y, key=lambda y:abs(y-y2)) # set y2 the y coordinate of tyle_y which has the minimum distance from y2
        tile_key = (x2, y2)

        # distance between the object and the closest tile
        dis = math.sqrt((x2 - self.x)**2 + (y2 - self.y)**2)
        
        # check if first tower of the game collides with forbidden tile
        if self == otherTower:
            if self.name == "fortress":
                # tile is available
                if dict_tile_fortress[tile_key] == 0:
                    return False # collide == False
                # tile is not available (collision with outside path)
                else:
                    return True # collide == True
            else:
                # tile is available
                if dict_tile[tile_key] == 0:
                    return False # collide == False
                # tile is not available (collision with path)
                else:
                    return True # collide == True

        # check if moving object collides with towers, fortress or forbidden tile 
        else:
            if self.name == "fortress":
                # tile is possibly available
                if dict_tile_fortress[tile_key] == 0:
                    # when not already occupied by another fortress
                    if dis >= 10:
                        return False # collide == False
                    # tile is already occupied by another fortress
                    else:
                        return True # collide == True
               # tile is not available (collision with outside path)
                else:
                    return True # collide == True
            else:
                # tile is possibly available
                if dict_tile[tile_key] == 0:
                    # when not already occupied by another object
                    if dis >= 10:
                        return False # collide == False
                    # tile is already occupied by another object
                    else:
                        return True # collide == True
                # tile is not available (collision with path)
                else:
                    return True # collide == True
