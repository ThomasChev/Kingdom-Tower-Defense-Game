import pygame
import os
from .enemy import Enemy

imgs = []
for x in range(1,25):
	imgs.append(pygame.image.load(os.path.join("game_assets/enemies/balista", str(x) + ".png")))

class Wei_balista(Enemy):
	
	def __init__(self):
		super().__init__()

		self.imgs = imgs[:]
		self.name = "wei_balista"
		self.max_health = 4
		self.vel = 2
		self.money = 8
		self.health = self.max_health
		self.sound = "die_siege.wav"
		self.path = [(660,347),(660,383),(660,417),(660,451),(660,485),(620,485),(580,485),(540,485),(500,485),(460,485),(420,485),(380,485),(340,485),(300,485),(260,485),(220,485),(180,485),(180,451),(140,451),(100,451),(60,451),(60,417),(60,383),(60,347),(4,347),(-20,347),(-75,347),(-100,347)]
		self.x = self.path[0][0]
		self.y = self.path[0][1]