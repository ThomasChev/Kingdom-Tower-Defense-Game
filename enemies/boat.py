import pygame
import os
from .enemy import Enemy

imgs = []
for x in range(1,18):
	imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/enemies/boat", str(x) + ".png" )), (48, 43)))

class Boat(Enemy):
	
	def __init__(self):
		super().__init__()

		self.imgs = imgs[:]
		self.name = "boat"
		self.money = 5
		self.max_health = 5
		self.health = self.max_health
		self.sound = "die_boat.wav"
		
		