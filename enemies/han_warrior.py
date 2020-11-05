import pygame
import os
from .enemy import Enemy

imgs = []
for x in range(0,15):
	imgs.append(pygame.image.load(os.path.join("game_assets/enemies/han_warrior", str(x) + ".png")))

class Han_warrior(Enemy):
	
	def __init__(self):
		super().__init__()

		self.imgs = imgs[:]
		self.name = "han_warrior"
		self.max_health = 3
		self.vel = 2
		self.money = 2
		self.health = self.max_health
		self.sound = "die_soldier.wav"
		self.path = [(740,417),(740,451),(740,485),(700,485),(660,485),(620,485),(580,485),(540,485),(500,485),(460,485),(420,485),(380,485),(340,485),(300,485),(260,485),(220,485),(180,485),(180,451),(140,451),(100,451),(60,451),(60,417),(60,383),(60,347),(4,347),(-20,347),(-75,347),(-100,347)]
		self.x = self.path[0][0]
		self.y = self.path[0][1]
		self.speed = 1