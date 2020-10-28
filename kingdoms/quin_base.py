import pygame
import os
from .kingdom import Kingdom

img = pygame.image.load(os.path.join("game_assets/kingdoms", "quin_base.png"))

class Quin_base(Kingdom):
	
	def __init__(self):
		super().__init__()

		self.img = img
		self.name = "quin_base"
		self.x = 22
		self.y = 319