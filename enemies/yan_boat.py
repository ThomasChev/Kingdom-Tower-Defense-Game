import pygame
import os
from .enemy import Enemy

img_dir = "game_assets/enemies/"
imgs = []
imgs = [pygame.image.load(os.path.join(img_dir, f"yan_boat/{i}.png")) for i in range(1,18)]
img_pres = pygame.transform.scale(pygame.image.load(os.path.join(img_dir, "intro/intro_boat.png")),(120, 120))

class Yan_boat(Enemy):
	
	def __init__(self):
		super().__init__()

		self.imgs = imgs[:]
		self.name = "yan_boat"
		self.nickname = "Yan Boat"
		self.max_health = 3
		self.vel = 2
		self.money = 6
		self.health = self.max_health
		self.sound = "die_boat.wav"
		self.path = [(940,142),(980,142),(980,176),(980,210),(980,244),(980,278),(980,313),(940,313),(900,313),(860,313),(820,313),(780,313),(740,313),(700,313),(660,313),(620,313),(580,313),(540,313),(500,313),(460,313),(420,313),(380,313),(380,347),(340,347),(300,347),(260,347),(220,347),(180,347),(140,347),(100,347),(100,313),(60,313),(4,313),(-20,347),(-75,347),(-100,347)]
		self.x = self.path[0][0]
		self.y = self.path[0][1]
		self.speed = 1
		self.rate = 2
		self.intro = img_pres
		self.type = "boat"