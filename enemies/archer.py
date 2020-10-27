import pygame
import os
from .enemy import Enemy

imgs = []
for x in range(0,20):
	imgs.append(pygame.image.load(os.path.join("game_assets/enemies/archer", str(x) + ".png")))

class Archer(Enemy):
	
	def __init__(self):
		super().__init__()

		self.imgs = imgs[:]
		self.name = "archer"
		self.money = 1
		self.max_health = 1
		self.health = self.max_health
		self.sound = "die_soldier.wav"