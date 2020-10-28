import pygame
import os
from .kingdom import Kingdom

img = pygame.image.load(os.path.join("game_assets/kingdoms", "qi_base.png"))

class Qi_base(Kingdom):
	
	def __init__(self):
		super().__init__()

		self.img = img
		self.name = "qi_base"
		self.x = 980
		self.y = 318