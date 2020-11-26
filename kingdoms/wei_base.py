import pygame
import os
from .kingdom import Kingdom
from tools.color import rgb
from menu.menu import Menu, Button

img_dir = "game_assets/kingdoms/"
img = pygame.image.load(os.path.join(img_dir, "wei_base.png"))
menu_bg = pygame.transform.scale(pygame.image.load(os.path.join(img_dir, "enemy_menu.png")),(180, 60))
catapult = pygame.image.load(os.path.join(img_dir, "catapult.png"))
balista = pygame.image.load(os.path.join(img_dir, "balista.png"))

class Wei_base(Kingdom):
	
	def __init__(self):
		super().__init__()

		self.img = img
		self.name = "wei_base"
		self.x = 660
		self.y = 318
		self.tile = [[460,244],[500,244],[540,244],[580,244],[620,244],[660,244],[700,244],[460,279],[500,279],[540,279],[580,279],[620,279],[660,279],[700,279],[500,313],[540,313],[580,313],[620,313],[660,313],[700,313],[500,349],[540,349],[580,349],[620,349],[660,349],[700,349],[500,383],[540,383],[580,383],[620,383],[660,383],[500,417],[540,417],[580,417],[620,417],[660,417]]
		self.rgb = rgb(254, 245, 134)
		self.menu = Menu(self, self.x, self.y, menu_bg, self.price)
		self.menu.add_btn(catapult, "kingdom")
		self.menu.add_btn(balista, "kingdom")

	def draw(self, win):
		super().draw(win)
		if self.selected:
			self.menu.x = self.x
			self.menu.y = self.y
			self.menu.update()
			self.menu.draw(win)