import pygame
import os
from .enemy import Enemy

img_dir = "game_assets/enemies/"
imgs = []
imgs = [pygame.image.load(os.path.join(img_dir, f"elephant/{i}.png")) for i in range(1,19)]
img_pres = pygame.transform.scale(pygame.image.load(os.path.join(img_dir, "intro/intro_elephant.png")),(120, 120))

class Chu_elephant(Enemy):
	
	def __init__(self):
		super().__init__()

		self.imgs = imgs[:]
		self.name = "chu_elephant"
		self.nickname = "Chu Elephant"
		self.max_health = 12
		self.vel = 1
		self.money = 10
		self.health = self.max_health
		self.sound = "die_elephant_lower.wav"
		self.path = [(940,693),(940,659),(940,625),(940,591),(900,591),(860,591),(860,625),(820,625),(780,625),(740,625),(700,625),(660,625),(620,625),(580,625),(540,625),(500,625),(460,625),(420,625),(380,625),(340,625),(300,625),(260,625),(260,591),(260,555),(260,521),(260,485),(220,485),(180,485),(180,451),(140,451),(100,451),(60,451),(60,417),(60,383),(60,347),(4,347),(-20,347),(-75,347),(-100,347)]
		self.x = self.path[0][0]
		self.y = self.path[0][1]
		self.speed = 1
		self.rate = 5
		self.intro = img_pres
		self.type = "elephant"