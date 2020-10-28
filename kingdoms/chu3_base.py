import pygame
import os
from .kingdom import Kingdom

img = pygame.image.load(os.path.join("game_assets/kingdoms", "chu_base.png"))

class Chu3_base(Kingdom):
	
	def __init__(self):
		super().__init__()

		self.img = img
		self.name = "chu3_base"
		self.x = 820
		self.y = 564