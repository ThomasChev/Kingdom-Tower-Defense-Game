import pygame
import os
from .kingdom import Kingdom

img = pygame.image.load(os.path.join("game_assets/kingdoms", "yan_base.png"))

class Yan_base(Kingdom):
	
	def __init__(self):
		super().__init__()

		self.img = img
		self.name = "yan_base"
		self.x = 940
		self.y = 111