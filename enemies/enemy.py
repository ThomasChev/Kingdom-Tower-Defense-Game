import pygame
import math
import random

class Enemy:

    def __init__(self):
        self.width = 64
        self.height = 64
        self.animation_count = 0
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

    def draw(self, win):
        """
        Draws the enemy with the given images
        :param win: surface
        :return: None
        """

        # for dot in self.path:
        # 	pygame.draw.circle(win, (255,0,0), dot, 5, 1)

        self.img = self.imgs[self.animation_count]
        win.blit(self.img, (self.x - self.img.get_width() / 2, self.y - self.img.get_height() / 2 - 35))
        self.draw_health_bar(win)

    def draw_health_bar(self, win):
        """
        draw health bar above enemy
        :param win: surface
        :return: None
        """
        length = 30
        # move_by = round(length / self.max_health)
        # health_bar = move_by * self.health
        health_bar = length*(1-((self.max_health-self.health)/self.max_health))
        if self.name =="zao_riboku":
            add_y = -10
        else:
            add_y = 0
        pygame.draw.rect(win, (255, 26, 26), (self.x - 13, self.y - 55 + add_y, length, 5), 0) # red rectangle
        pygame.draw.rect(win, (102, 255, 51), (self.x - 13, self.y - 55 + add_y, health_bar, 5), 0) # green rectangle
        pygame.draw.rect(win, (77, 77, 77), (self.x - 13, self.y - 55 + add_y, health_bar, 5), 1) # grey rectangle border

    # def collide(self, X, Y):
    #     """
    #     Returns if position has hit enemy
    #     :param x: int
    #     :param y: int
    #     :return: Bool
    #     """
    #     if X<= self.x + self.width and X >= self.x:
    #         if Y <= self.y + self.height and Y >= self.y:
    #             return True
    #     return False


    def move(self):
        """
        Move enemy
        :return: None
        """
        if not self.block:
            self.animation_count += 1
            if self.animation_count >= len(self.imgs):
                self.animation_count = 0

            # To move object1 to object2:
            # x1, y1 = self.path[self.path_pos]
            if self.path_pos + 1 >= len(self.path):
                x2, y2 = (-10, 346)
            else:
                x2, y2 = self.path[self.path_pos+1]
            # distances between objects...
            dx = x2 - self.x
            dy = y2 - self.y
            # actual distance between objects(direct line)
            d = math.sqrt(dx** 2 + dy** 2)
            # calculate the distance allowed to move
            normal = 0.3*self.vel/d
            # finally move ;)
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

    def hit(self, damage):
        """
        Returns if an enemy has died and removes one health
        each call
        :return: Bool
        """

        self.health -= damage/2
        if self.health <= 0:
            return True
        return False

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



