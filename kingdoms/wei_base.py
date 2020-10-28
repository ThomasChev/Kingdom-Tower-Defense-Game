import pygame
import os
from .kingdom import Kingdom

img = pygame.image.load(os.path.join("game_assets/kingdoms", "wei_base.png"))

class Wei_base(Kingdom):
	
	def __init__(self):
		super().__init__()

		self.img = img
		self.name = "wei_base"
		self.x = 660
		self.y = 318