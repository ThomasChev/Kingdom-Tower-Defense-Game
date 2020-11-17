import pygame
import os
from .kingdom import Kingdom
from game_assets.colors import rgb
from menu.menu import Menu, Button

img_dir = "game_assets/kingdoms/"
img = pygame.image.load(os.path.join(img_dir, "qi_base.png"))
menu_bg = pygame.transform.scale(pygame.image.load(os.path.join(img_dir, "enemy_menu.png")),(180, 60))
warrior = pygame.image.load(os.path.join(img_dir, "warrior.png"))
boat = pygame.image.load(os.path.join(img_dir, "boat.png"))

class Qi_base(Kingdom):
	
	def __init__(self):
		super().__init__()

		self.img = img
		self.name = "qi_base"
		self.x = 980
		self.y = 318
		self.tile = [[1100,176],[1020,210],[1060,210],[1100,210],[860,244],[900,244],[940,244],[980,244],[1020,244],[1060,244],[1100,244],[860,279],[900,279],[940,279],[980,279],[1020,279],[1060,279],[1100,279],[860,313],[900,313],[940,313],[980,313],[1020,313],[1060,313],[1100,313],[860,349],[900,349],[940,349],[980,349],[1020,349],[1060,349],[1100,349]]
		self.rgb = rgb(254, 234, 178)
		self.menu = Menu(self, self.x, self.y, menu_bg, self.price)
		self.menu.add_btn(warrior, "kingdom")
		self.menu.add_btn(boat, "kingdom")

	def draw(self, win):
		super().draw(win)
		if self.selected:
			self.menu.x = self.x
			self.menu.y = self.y
			self.menu.update()
			self.menu.draw(win)