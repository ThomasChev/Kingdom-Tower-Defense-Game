import pygame
import os
from .enemy import Enemy

imgs = []
for x in range(0,20):
	imgs.append(pygame.image.load(os.path.join("game_assets/enemies/chu_warrior", str(x) + ".png")))

class Chu_warrior(Enemy):
	
	def __init__(self):
		super().__init__()

		self.imgs = imgs[:]
		self.name = "chu_warrior"
		self.max_health = 3
		self.vel = 2
		self.money = 5
		self.health = self.max_health
		self.sound = "die_soldier.wav"
		self.path = [(540,693),(540,659),(540,625),(500,625),(460,625),(420,625),(380,625),(340,625),(300,625),(260,625),(260,591),(260,555),(260,521),(260,485),(220,485),(180,485),(180,451),(140,451),(100,451),(60,451),(60,417),(60,383),(60,347),(4,347),(-20,347),(-75,347),(-100,347)]
		self.x = self.path[0][0]
		self.y = self.path[0][1]