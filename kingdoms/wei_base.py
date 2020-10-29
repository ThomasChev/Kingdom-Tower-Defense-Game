import pygame
import os
from .kingdom import Kingdom
from game_assets.colors import rgb

img = pygame.image.load(os.path.join("game_assets/kingdoms", "wei_base.png"))

class Wei_base(Kingdom):
	
	def __init__(self):
		super().__init__()

		self.img = img
		self.name = "wei_base"
		self.x = 660
		self.y = 318
		self.tile = [[460,244],[500,244],[540,244],[580,244],[620,244],[660,244],[700,244],[460,279],[500,279],[540,279],[580,279],[620,279],[660,279],[700,279],[500,313],[540,313],[580,313],[620,313],[660,313],[700,313],[500,349],[540,349],[580,349],[620,349],[660,349],[700,349],[500,383],[540,383],[580,383],[620,383],[660,383],[500,417],[540,417],[580,417],[620,417],[660,417]]
		self.rgb = rgb(254, 245, 134)