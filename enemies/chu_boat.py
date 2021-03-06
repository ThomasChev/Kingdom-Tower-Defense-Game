import pygame
import os
from .enemy import Enemy

img_dir = "game_assets/enemies/"
imgs = []
imgs = [pygame.image.load(os.path.join(img_dir, f"chu_boat/{i}.png")) for i in range(1,18)]
img_pres = pygame.transform.scale(pygame.image.load(os.path.join(img_dir, "intro/intro_boat.png")),(120, 120))


class Chu_boat(Enemy):
	
	def __init__(self):
		super().__init__()

		self.imgs = imgs[:]
		self.name = "chu_boat"
		self.nickname = "Chu Boat"
		self.max_health = 4
		self.vel = 1.5
		self.money = 6
		self.health = self.max_health
		self.sound = "die_boat.wav"
		self.path = [(820,591),(820,555),(780,555),(780,591),(740,591),(700,591),(660,591),(660,555),(620,555),(580,555),(540,555),(500,555),(500,591),(460,591),(420,591),(380,591),(340,591),(300,591),(300,555),(300,521),(300,485),(300,451),(300,417),(300,383),(300,347),(260,347),(220,347),(180,347),(140,347),(100,347),(100,313),(60,313),(4,313),(-20,347),(-75,347),(-100,347)]
		self.x = self.path[0][0]
		self.y = self.path[0][1]
		self.speed = 1
		self.rate = 2
		self.intro = img_pres
		self.type = "boat"