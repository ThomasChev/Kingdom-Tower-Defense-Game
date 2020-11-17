import pygame
import os
from .kingdom import Kingdom
from game_assets.colors import rgb
from menu.menu import Menu, Button

img_dir = "game_assets/kingdoms/"
img = pygame.image.load(os.path.join(img_dir, "han_base.png"))
menu_bg = pygame.transform.scale(pygame.image.load(os.path.join(img_dir, "enemy_menu.png")),(120, 60))
warrior = pygame.image.load(os.path.join(img_dir, "warrior.jpg"))

class Han_base(Kingdom):
	
	def __init__(self):
		super().__init__()

		self.img = img
		self.name = "han_base"
		self.x = 740
		self.y = 388
		self.tile = [[700,383],[740,383],[780,383],[700,417],[740,417],[780,417],[700,453],[740,453],[780,453],[700,489],[740,489],[780,489],[700,523],[740,523]]
		self.rgb = rgb(253, 143, 66)
		self.menu = Menu(self, self.x, self.y, menu_bg, self.price)
		self.menu.add_btn(warrior, "kingdom2")

	def draw(self, win):
		super().draw(win)
		if self.selected:
			self.menu.x = self.x
			self.menu.y = self.y
			self.menu.update()
			self.menu.draw(win)