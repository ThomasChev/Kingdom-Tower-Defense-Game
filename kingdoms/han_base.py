import pygame
import os
from .kingdom import Kingdom
from game_assets.colors import rgb

img = pygame.image.load(os.path.join("game_assets/kingdoms", "han_base.png"))

class Han_base(Kingdom):
	
	def __init__(self):
		super().__init__()

		self.img = img
		self.name = "han_base"
		self.x = 740
		self.y = 388
		self.tile = [[700,383],[740,383],[780,383],[700,417],[740,417],[780,417],[700,453],[740,453],[780,453],[700,489],[740,489],[780,489],[700,523],[740,523]]
		self.rgb = rgb(253, 143, 66)