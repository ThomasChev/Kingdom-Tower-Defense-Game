import pygame
import os
from .kingdom import Kingdom

img = pygame.image.load(os.path.join("game_assets/kingdoms", "han_base.png"))

class Han_base(Kingdom):
	
	def __init__(self):
		super().__init__()

		self.img = img
		self.name = "han_base"
		self.x = 740
		self.y = 388