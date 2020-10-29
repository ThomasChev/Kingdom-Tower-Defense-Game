import pygame
import os
from .kingdom import Kingdom
from game_assets.colors import rgb

img = pygame.image.load(os.path.join("game_assets/kingdoms", "qi_base.png"))

class Qi_base(Kingdom):
	
	def __init__(self):
		super().__init__()

		self.img = img
		self.name = "qi_base"
		self.x = 980
		self.y = 318
		self.tile = [[1100,176],[1020,210],[1060,210],[1100,210],[860,244],[900,244],[940,244],[980,244],[1020,244],[1060,244],[1100,244],[860,279],[900,279],[940,279],[980,279],[1020,279],[1060,279],[1100,279],[860,313],[900,313],[940,313],[980,313],[1020,313],[1060,313],[1100,313],[860,349],[900,349],[940,349],[980,349],[1020,349],[1060,349],[1100,349]]
		self.rgb = rgb(254, 234, 178)