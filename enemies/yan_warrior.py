import pygame
import os
from .enemy import Enemy

imgs = []
for x in range(0,16):
	imgs.append(pygame.image.load(os.path.join("game_assets/enemies/yan_warrior", str(x) + ".png")))

class Yan_warrior(Enemy):
	
	def __init__(self):
		super().__init__()

		self.imgs = imgs[:]
		self.name = "yan_warrior"
		self.nickname = "Yan Warrior"
		self.max_health = 1
		self.vel = 5
		self.money = 6
		self.health = self.max_health
		self.sound = "die_soldier.wav"
		self.path = [(940,142),(940,176),(900,176),(900,210),(900,244),(900,278),(860,278),(820,278),(780,278),(740,278),(700,278),(660,278),(620,278),(580,278),(540,278),(500,278),(500,244),(500,210),(460,210),(420,210),(420,244),(420,278),(420,313),(420,347),(460,347),(500,347),(500,383),(500,417),(460,417),(420,417),(380,417),(340,417),(340,451),(340,485),(300,485),(260,485),(220,485),(180,485),(180,451),(140,451),(100,451),(60,451),(60,417),(60,383),(60,347),(4,347),(-20,347),(-75,347),(-100,347)]
		self.x = self.path[0][0]
		self.y = self.path[0][1]
		self.speed = 1
		self.rate = 0.2