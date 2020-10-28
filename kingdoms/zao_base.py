import pygame
import os
from .kingdom import Kingdom

img = pygame.image.load(os.path.join("game_assets/kingdoms", "zao_base.png"))

class Zao_base(Kingdom):
	
	def __init__(self):
		super().__init__()

		self.img = img
		self.name = "zao_base"
		self.x = 700
		self.y = 145