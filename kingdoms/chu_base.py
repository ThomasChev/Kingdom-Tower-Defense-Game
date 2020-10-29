import pygame
import os
from .kingdom import Kingdom
from game_assets.colors import rgb

img = pygame.image.load(os.path.join("game_assets/kingdoms", "chu_base.png"))

class Chu_base(Kingdom):
	
	def __init__(self):
		super().__init__()

		self.img = img
		self.name = "chu_base"
		self.x = 540
		self.y = 671
		self.tile = [[860,383],[900,383],[940,383],[980,383],[1020,383],[1060,383],[1100,383],[820,417],[860,417],[900,417],[940,417],[980,417],[1020,417],[1060,417],[1100,417],[500,453],[540,453],[580,453],[620,453],[660,453],[820,453],[860,453],[900,453],[940,453],[980,453],[1020,453],[1060,453],[1100,453],[500,489],[540,489],[580,489],[620,489],[660,489],[820,489],[860,489],[900,489],[940,489],[980,489],[1020,489],[1060,489],[1100,489],[140,523],[180,523],[220,523],[260,523],[300,523],[340,523],[380,523],[420,523],[460,523],[500,523],[540,523],[580,523],[620,523],[660,523],[780,523],[820,523],[860,523],[900,523],[940,523],[980,523],[1020,523],[1060,523],[1100,523],[20,559],[60,559],[100,559],[140,559],[180,559],[220,559],[260,559],[300,559],[340,559],[380,559],[420,559],[460,559],[500,559],[540,559],[580,559],[620,559],[660,559],[700,559],[740,559],[780,559],[820,559],[860,559],[900,559],[940,559],[980,559],[1020,559],[1060,559],[1100,559],[20,593],[60,593],[100,593],[140,593],[180,593],[220,593],[260,593],[300,593],[340,593],[380,593],[420,593],[460,593],[500,593],[540,593],[580,593],[620,593],[660,593],[700,593],[740,593],[780,593],[820,593],[860,593],[900,593],[940,593],[980,593],[1020,593],[1060,593],[1100,593],[20,627],[60,627],[100,627],[140,627],[180,627],[220,627],[260,627],[300,627],[340,627],[380,627],[420,627],[460,627],[500,627],[540,627],[580,627],[620,627],[660,627],[700,627],[740,627],[780,627],[820,627],[860,627],[900,627],[940,627],[980,627],[1020,627],[1060,627],[1100,627],[20,661],[60,661],[100,661],[140,661],[180,661],[220,661],[260,661],[300,661],[340,661],[380,661],[420,661],[460,661],[500,661],[540,661],[580,661],[620,661],[660,661],[700,661],[740,661],[780,661],[820,661],[860,661],[900,661],[940,661],[980,661],[1020,661],[1060,661],[1100,661]]
		self.rgb = rgb(176, 134, 105)