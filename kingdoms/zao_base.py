import pygame
import os
from .kingdom import Kingdom
from tools.color import rgb
from menu.menu import Menu, Button

img_dir = "game_assets/kingdoms/"
img = pygame.image.load(os.path.join(img_dir, "zao_base.png"))
menu_bg = pygame.transform.scale(pygame.image.load(os.path.join(img_dir, "enemy_menu.png")),(180, 60))
warrior = pygame.image.load(os.path.join(img_dir, "warrior.png"))
riboku = pygame.image.load(os.path.join(img_dir, "riboku.png"))

class Zao_base(Kingdom):
	
	def __init__(self):
		super().__init__()

		self.img = img
		self.name = "zao_base"
		self.x = 700
		self.y = 145
		self.tile = [[20,40],[60,40],[100,40],[140,40],[180,40],[220,40],[260,40],[300,40],[340,40],[380,40],[420,40],[460,40],[500,40],[540,40],[580,40],[620,40],[660,40],[700,40],[740,40],[20,74],[60,74],[100,74],[140,74],[180,74],[220,74],[260,74],[300,74],[340,74],[380,74],[420,74],[460,74],[500,74],[540,74],[580,74],[620,74],[660,74],[700,74],[740,74],[20,108],[60,108],[100,108],[140,108],[180,108],[220,108],[260,108],[300,108],[340,108],[540,108],[580,108],[620,108],[660,108],[700,108],[740,108],[540,142],[580,142],[620,142],[660,142],[700,142],[740,142],[540,176],[580,176],[620,176],[660,176],[700,176],[740,176],[540,210],[580,210],[620,210],[660,210],[700,210],[740,210],[780,210],[820,210],[740,244],[780,244],[820,244],[740,279],[780,279],[820,279],[740,313],[780,313],[820,313],[740,349],[780,349],[820,349],[820,383]]
		self.rgb = rgb(250, 160, 150)
		self.menu = Menu(self, self.x, self.y, menu_bg, self.price)
		self.menu.add_btn(warrior, "kingdom")
		self.menu.add_btn(riboku, "kingdom")

	def draw(self, win):
		super().draw(win)
		if self.selected:
			self.menu.x = self.x
			self.menu.y = self.y
			self.menu.update()
			self.menu.draw(win)