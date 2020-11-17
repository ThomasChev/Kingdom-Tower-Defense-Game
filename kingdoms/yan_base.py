import pygame
import os
from .kingdom import Kingdom
from game_assets.colors import rgb
from menu.menu import Menu, Button

img_dir = "game_assets/kingdoms/"
img = pygame.image.load(os.path.join(img_dir, "yan_base.png"))
menu_bg = pygame.transform.scale(pygame.image.load(os.path.join(img_dir, "enemy_menu.png")),(180, 60))
warrior = pygame.image.load(os.path.join(img_dir, "warrior.png"))
boat = pygame.image.load(os.path.join(img_dir, "boat.png"))

class Yan_base(Kingdom):
	
	def __init__(self):
		super().__init__()

		self.img = img
		self.name = "yan_base"
		self.x = 940
		self.y = 111
		self.tile = [[780,40],[820,40],[860,40],[900,40],[940,40],[980,40],[1020,40],[1060,40],[1100,40],[780,74],[820,74],[860,74],[900,74],[940,74],[980,74],[1020,74],[1060,74],[1100,74],[780,108],[820,108],[860,108],[900,108],[940,108],[980,108],[1020,108],[1060,108],[1100,108],[780,142],[820,142],[860,142],[900,142],[940,142],[980,142],[1020,142],[1060,142],[1100,142],[780,176],[820,176],[860,176],[900,176],[940,176],[980,176],[1020,176],[1060,176],[860,210],[900,210],[940,210],[980,210]]
		self.rgb = rgb(170, 250, 140)
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