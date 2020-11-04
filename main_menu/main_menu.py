from game import Game
import pygame
import os
import time
from game_assets.colors import rgb
pygame.font.init()

start_btn = pygame.image.load(os.path.join("game_assets/menu/", "play_big_btn.png"))
lore_btn = pygame.image.load(os.path.join("game_assets/menu/", "lore_btn.png"))
lore_img = pygame.image.load(os.path.join("game_assets/menu/", "lore.png"))
lore2_img = pygame.image.load(os.path.join("game_assets/menu/", "lore2.png"))
info_btn = pygame.image.load(os.path.join("game_assets/menu/", "info_btn.png"))
level_btn = pygame.image.load(os.path.join("game_assets/menu/", "level1_btn.png"))
easy_btn = pygame.image.load(os.path.join("game_assets/menu/", "easy_btn.png"))
medium_btn = pygame.image.load(os.path.join("game_assets/menu/", "medium_btn.png"))
hard_btn = pygame.image.load(os.path.join("game_assets/menu/", "hard_btn.png"))

# Attack Towers
info_shin_img = pygame.image.load(os.path.join("game_assets/menu/", "info_shin.png"))
info_moubu_img = pygame.image.load(os.path.join("game_assets/menu/", "info_moubu.png"))
info_kanki_img = pygame.image.load(os.path.join("game_assets/menu/", "info_kanki.png"))
info_ouhon_img = pygame.image.load(os.path.join("game_assets/menu/", "info_ouhon.png"))

# Support Towers + Fortress
info_fortress_img = pygame.image.load(os.path.join("game_assets/menu/", "info_fortress.png"))
info_kyoukai_img = pygame.image.load(os.path.join("game_assets/menu/", "info_kyoukai.png"))
info_ten_img = pygame.image.load(os.path.join("game_assets/menu/", "info_ten.png"))
info_ryo_img = pygame.image.load(os.path.join("game_assets/menu/", "info_ryo.png"))

pygame.mixer.pre_init()
pygame.mixer.init()

pad_x = 75
pad_y = 5

class MainMenu:
    def __init__(self, win):
        self.width = 1200
        self.height = 700
        self.bg = pygame.image.load(os.path.join("game_assets/background/", "kingdom_menu.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.win = win
        self.font = pygame.font.Font("game_assets/fonts/SF Atarian System.ttf", 48)
        
        self.btn = (self.width/2 - start_btn.get_width()/2, 225, start_btn.get_width(), start_btn.get_height())
        self.lore = (self.width/2 - lore_btn.get_width()/2, 300, lore_btn.get_width(), lore_btn.get_height())
        self.info = (self.width/2 - info_btn.get_width()/2, 375, info_btn.get_width(), info_btn.get_height())
        self.level = (self.width/2 - level_btn.get_width()/2, 450, level_btn.get_width(), level_btn.get_height())
        self.easy = (self.width/2 - easy_btn.get_width()/2, 525, easy_btn.get_width(), easy_btn.get_height())
        self.medium = (self.width/2 - medium_btn.get_width()/2, 560, medium_btn.get_width(), medium_btn.get_height())
        self.hard = (self.width/2 - hard_btn.get_width()/2, 595, hard_btn.get_width(), hard_btn.get_height())
        
        self.game_level = "Easy"
        self.lvls = ["Easy", "Medium", "Hard"]
        self.levels = [self.easy, self.medium, self.hard]
        self.buttons = [self.lore, self.info, self.level]
        self.btn_names = ["lore", "info", "level"]

        self.show_lore = False
        self.show_info = False
        self.show_level = False
        self.shows = {"lore" : self.show_lore, "info":self.show_info, "level":self.show_level}

    def run(self):
        pygame.mixer.music.load(os.path.join("game_assets/sounds/", "melody.wav"))
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(loops=-1) # loop forever
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONUP:

                    # check if hit buttons
                    x, y = pygame.mouse.get_pos()

                    # if you click on Play button
                    if self.click(self.btn, x, y):
                        pygame.mixer.music.stop()
                        play_sound(1,"next_round.wav")
                        game = Game(self.win)
                        game.level = self.game_level
                        game.run()
                        self.show_lore = False
                        self.show_info = False
                        self.show_level = False
                        del game

                    # if you click on other buttons
                    for i, (button, name) in enumerate(zip(self.buttons, self.btn_names)):
                        if self.click(button, x, y):
                            play_sound(1,"toggle.wav", 600)
                            for key in self.shows:
                                if key != name:
                                    self.shows[key] = False
                            self.shows[name] = not(self.shows[name])
                            break

                    # if you click on Easy/Medium/Hard buttons
                    if self.shows["level"]:
                        for lvl, level in zip(self.lvls, self.levels):
                            if self.click(level, x, y):
                                play_sound(1,"beep_menu.wav",300)
                                self.game_level = lvl

            self.draw()

        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0,0))
        text = self.font.render(self.game_level, 2, rgb(255,255,255))
        self.win.blit(text, (self.width/2 - text.get_width()/2, self.height - 10 - text.get_height()))
        self.win.blit(start_btn, (self.btn[0], self.btn[1]))
        self.win.blit(lore_btn, (self.lore[0], self.lore[1]))
        self.win.blit(info_btn, (self.info[0], self.info[1]))
        
        if self.game_level == "Easy":
            level_btn = pygame.image.load(os.path.join("game_assets/menu/", "level1_btn.png"))
        elif self.game_level == "Medium":
            level_btn = pygame.image.load(os.path.join("game_assets/menu/", "level2_btn.png"))
        elif self.game_level == "Hard":
            level_btn = pygame.image.load(os.path.join("game_assets/menu/", "level3_btn.png"))
        self.win.blit(level_btn, (self.level[0], self.level[1]))

        # print("at draw:", self.shows)
        if self.shows["lore"]:
            print("lore")
            # right image
            x = self.lore[0] + pad_x
            y = self.lore[1]
            self.win.blit(lore_img, (x, y))

            # left image
            x = self.lore[0] - pad_x - lore2_img.get_width() + lore_btn.get_width()
            y = self.lore[1]
            self.win.blit(lore2_img, (x, y))

        if self.shows["info"]:
            
            # Support Towers + Fortress, right images
            x = self.info[0] + pad_x
            y = self.info[1]
            add_y = info_shin_img.get_height() + pad_y
            self.win.blit(info_fortress_img, (x, y + 0*add_y ))
            self.win.blit(info_kyoukai_img, (x, y + 1*add_y ))
            self.win.blit(info_ten_img, (x, y + 2*add_y ))
            self.win.blit(info_ryo_img, (x, y + 3*add_y ))

            # Attack Towers, left images
            x = self.info[0] - pad_x - info_shin_img.get_width() + info_btn.get_width()
            y = self.info[1]
            add_y = info_shin_img.get_height() + pad_y
            self.win.blit(info_shin_img, (x, y + 0*add_y ))
            self.win.blit(info_moubu_img, (x, y + 1*add_y ))
            self.win.blit(info_kanki_img, (x, y + 2*add_y ))
            self.win.blit(info_ouhon_img, (x, y + 3*add_y ))

        if self.shows["level"]:
            x = self.easy[0]
            y = self.easy[1]
            add_y = easy_btn.get_height() + pad_y
            self.win.blit(easy_btn, (x, y + 0*add_y))
            self.win.blit(medium_btn, (x, y + 1*add_y))
            self.win.blit(hard_btn, (x, y + 2*add_y))

        pygame.display.update()

    def click(self, button, x, y):
        """
        returns if click on button
        :param x: btn: list
        :param x: int
        :param y: int
        :return: bool
        """
        if button[0] <= x <= button[0] + button[2]:
            if button[1] <= y <= button[1] + button[3]:
                return True
        return False

def play_sound(*args):
    if len(args) == 3:
        a,b,c = args[0],args[1],args[2]
        pygame.mixer.Channel(a).play(pygame.mixer.Sound(os.path.join("game_assets/sounds/", b)), maxtime=c)
    elif len(args) == 2:
        a,b = args[0],args[1]
        pygame.mixer.Channel(a).play(pygame.mixer.Sound(os.path.join("game_assets/sounds/", b)))
