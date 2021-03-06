import pygame
import os
from .enemy import Enemy

img_dir = "game_assets/enemies/"
imgs = []
imgs = [pygame.image.load(os.path.join(img_dir, f"zao_riboku/{i}.png")) for i in range(0,16)]
img_pres = pygame.transform.scale(pygame.image.load(os.path.join(img_dir, "intro/intro_riboku.png")),(120, 120))

class Zao_riboku(Enemy):
	
	def __init__(self):
		super().__init__()

		self.imgs = imgs[:]
		self.name = "zao_riboku"
		self.nickname = "Zao Riboku"
		self.max_health = 500
		self.vel = 1
		self.money = 50
		self.health = self.max_health
		self.sound = "die_soldier.wav"
		self.path = [(700,176),(700,210),(700,244),(700,278),(660,278),(620,278),(580,278),(540,278),(500,278),(500,244),(500,210),(460,210),(420,210),(420,244),(420,278),(420,313),(420,347),(460,347),(500,347),(500,383),(500,417),(460,417),(420,417),(380,417),(340,417),(340,451),(340,485),(300,485),(260,485),(220,485),(180,485),(180,451),(140,451),(100,451),(60,451),(60,417),(60,383),(60,347),(4,347),(-20,347),(-75,347),(-100,347)]
		self.x = self.path[0][0]
		self.y = self.path[0][1]
		self.speed = 1
		self.rate = 1
		self.intro = img_pres
		self.type = "riboku"