import pygame
import os

tile_x = [4,60,100,140,180,220,260,300,340,380,420,460,500,540,580,620,660,700,740,780,820,860,900,940,980,1020,1060,1100,1140,1180]
tile_y = [40,74,108,142,176,210,244,279,313,349,383,417,453,489,523,559,593,627,661]

explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []

for key in explosion_anim:
    img_dir = "game_assets/enemies/explosion/" + key + "/"
    explosion_anim[key] = [pygame.image.load(os.path.join(img_dir, f'regularExplosion0{i}.png')) for i in range(0, 9)]

explosion_anim['tower'] = []
img_dir = "game_assets/quin_towers/explosion/"
explosion_anim['tower'] = [pygame.image.load(os.path.join(img_dir, f'regularExplosion0{i}.png')) for i in range(0, 4)]


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, style):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.style = style
        self.image = explosion_anim[self.style][0]
        self.rect = self.image.get_rect()
        self.corr_x = 0
        self.corr_y = -30
        self.rect.center = (self.x + self.corr_x, self.y + self.corr_y)
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        
        self.corr_x = 0
        self.corr_y = -30
        self.adjust()

        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.style]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.style][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

    def adjust(self):

        self.x = min(tile_x, key=lambda x:abs(x-self.x))
        self.y = min(tile_y, key=lambda y:abs(y-self.y))

        if self.style == "tower":
            self.corr_x = self.corr_x
            self.corr_y = self.corr_y + 60
            self.frame_rate = 75

        self.rect.center = (self.x + self.corr_x, self.y + self.corr_y)