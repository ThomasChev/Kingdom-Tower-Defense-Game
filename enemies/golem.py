import pygame
import os
from .enemy import Enemy

imgs = []
for x in range(18):
			add_str = str(x)
			if x < 10:
				add_str = "0" + add_str
			imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/enemies/golem", "5_enemies_1_run_0" + add_str + ".png" )), (48, 48)))

class Golem(Enemy):
	
	def __init__(self):
		super().__init__()

		self.imgs = imgs[:]
		self.name = "golem"
		self.money = 5
		self.max_health = 5
		self.health = self.max_health
		self.sound = "die_soldier.wav"