from game import Game
from slotmachine import Casino
import pygame
import os
import time
from game_assets.colors import rgb
pygame.font.init()

casino_btn = pygame.image.load(os.path.join("game_assets/menu/", "casino_btn.png"))
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
img_shin = pygame.image.load(os.path.join("game_assets/quin_towers/shin_info/", "shin_img.png"))
img_moubu = pygame.image.load(os.path.join("game_assets/quin_towers/moubu_info/", "moubu_img.png"))
img_kanki = pygame.image.load(os.path.join("game_assets/quin_towers/kanki_info/", "kanki_img.png"))
img_ouhon = pygame.image.load(os.path.join("game_assets/quin_towers/ouhon_info/", "ouhon_img.png"))
info_shin = pygame.image.load(os.path.join("game_assets/quin_towers/shin_info/", "shin_info.png"))
info_moubu = pygame.image.load(os.path.join("game_assets/quin_towers/moubu_info/", "moubu_info.png"))
info_kanki = pygame.image.load(os.path.join("game_assets/quin_towers/kanki_info/", "kanki_info.png"))
info_ouhon = pygame.image.load(os.path.join("game_assets/quin_towers/ouhon_info/", "ouhon_info.png"))

# Support Towers + Fortress
img_fortress = pygame.image.load(os.path.join("game_assets/fortress/fortress_info/", "fortress_img.png"))
img_kyoukai = pygame.image.load(os.path.join("game_assets/support_towers/kyoukai_info/", "kyoukai_img.png"))
img_ten = pygame.image.load(os.path.join("game_assets/support_towers/ten_info/", "ten_img.png"))
img_ryo = pygame.image.load(os.path.join("game_assets/support_towers/ryo_info/", "ryo_img.png"))
info_fortress = pygame.image.load(os.path.join("game_assets/fortress/fortress_info/", "fortress_info.png"))
info_kyoukai = pygame.image.load(os.path.join("game_assets/support_towers/kyoukai_info/", "kyoukai_info.png"))
info_ten = pygame.image.load(os.path.join("game_assets/support_towers/ten_info/", "ten_info.png"))
info_ryo = pygame.image.load(os.path.join("game_assets/support_towers/ryo_info/", "ryo_info.png"))

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
        self.font_20 = pygame.font.Font("game_assets/fonts/SF Atarian System.ttf", 18)

        # play
        self.btn = (self.width/2 - start_btn.get_width()/2, 225, start_btn.get_width(), start_btn.get_height())

        # casino mini-game
        self.slot = (self.width/2 + start_btn.get_width()/2 + pad_x/2, 225, casino_btn.get_width(), casino_btn.get_height())
        
        # get lore info
        self.lore = (self.width/2 - lore_btn.get_width()/2, 300, lore_btn.get_width(), lore_btn.get_height())
        
        # get character infos
        self.info = (self.width/2 - info_btn.get_width()/2, 375, info_btn.get_width(), info_btn.get_height())
        self.x = self.info[0] - pad_x - info_shin.get_width() + info_btn.get_width()
        self.y = self.info[1]
        self.add_y = info_shin.get_height() + pad_y
        self.shin = (self.x, self.y + 0*self.add_y, info_shin.get_width(), info_shin.get_height())
        self.moubu = (self.x, self.y + 1*self.add_y, info_moubu.get_width(), info_moubu.get_height())
        self.kanki = (self.x, self.y + 2*self.add_y, info_kanki.get_width(), info_kanki.get_height())
        self.ouhon = (self.x, self.y + 3*self.add_y, info_ouhon.get_width(), info_ouhon.get_height())
        self.fortress = (self.info[0] + pad_x, self.y + 0*self.add_y, info_fortress.get_width(), info_fortress.get_height())
        self.kyoukai = (self.info[0] + pad_x, self.y + 1*self.add_y, info_kyoukai.get_width(), info_kyoukai.get_height())
        self.ten = (self.info[0] + pad_x, self.y + 2*self.add_y, info_ten.get_width(), info_ten.get_height())
        self.ryo = (self.info[0] + pad_x, self.y + 3*self.add_y, info_ryo.get_width(), info_ryo.get_height())

        self.img_names = ['shin', 'moubu', 'kanki', 'ouhon', 'fortress', 'kyoukai', 'ten', 'ryo']
        self.character_infos = [self.shin, self.moubu, self.kanki, self.ouhon, self.fortress, self.kyoukai, self.ten, self.ryo]
        self.info_imgs = [info_shin, info_moubu, info_kanki, info_ouhon, info_fortress, info_kyoukai, info_ten, info_ryo]
        self.character_imgs = [(img_shin, (900, 225), text_shin, (700,225)), (img_moubu, (870, 225), text_moubu, (670,225)), (img_kanki, (900, 225), text_kanki, (700,225)), (img_ouhon, (845, 225), text_ouhon, (645,225)), (img_fortress, (5, 325), text_fortress, (-80,325)), (img_kyoukai, (48, 225), text_kyoukai, (48, 225)), (img_ten, (57, 225), text_ten, (57, 225)), (img_ryo, (31, 225), text_ryo, (31, 225))]
        
        # change level
        self.level = (self.width/2 - level_btn.get_width()/2, 450, level_btn.get_width(), level_btn.get_height())
        self.easy = (self.width/2 - easy_btn.get_width()/2, 525, easy_btn.get_width(), easy_btn.get_height())
        self.medium = (self.width/2 - medium_btn.get_width()/2, 560, medium_btn.get_width(), medium_btn.get_height())
        self.hard = (self.width/2 - hard_btn.get_width()/2, 595, hard_btn.get_width(), hard_btn.get_height())
        self.game_level = "Easy"
        self.lvls = ["Easy", "Medium", "Hard"]
        self.levels = [self.easy, self.medium, self.hard]
        
        self.btn_names = ["lore", "info", "level"]
        self.buttons = [self.lore, self.info, self.level]
        self.show_lore = False
        self.show_info = False
        self.show_level = False
        self.show_shin = False
        self.show_moubu = False
        self.show_kanki = False
        self.show_ouhon = False
        self.show_fortress = False
        self.show_kyoukai = False
        self.show_ten = False
        self.show_ryo = False
        self.show_img = False
        self.shows = {"lore" : self.show_lore, "info":self.show_info, "level":self.show_level, 'shin':self.show_shin, 'moubu':self.show_moubu, 'kanki':self.show_kanki, 'ouhon':self.show_ouhon, 'fortress':self.show_fortress, 'kyoukai':self.show_kyoukai, 'ten':self.show_ten, 'ryo':self.show_ryo, 'img':self.show_img}
        self.right = False
        self.left = False

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

                    if self.click(self.slot, x, y):
                        pygame.mixer.music.stop()
                        play_sound(1,"slot/jackpot.wav")
                        mini_game = Casino()

                    # if you click on other buttons
                    for button, name in zip(self.buttons, self.btn_names):
                        if self.click(button, x, y):
                            play_sound(1,"toggle.wav", 600)
                            for key in self.shows:
                                if key != name:
                                    self.shows[key] = False
                            self.shows[name] = not(self.shows[name])
                            break

                    # if you click on Character imgs
                    if self.shows["info"]:
                        for button, name in zip(self.character_infos, self.img_names):
                            if self.click(button, x, y):
                                play_sound(1,"beep_menu.wav",300)
                                for key in self.shows:
                                    if key != name:
                                        self.shows[key] = False
                                self.shows["info"] = True
                                self.shows["img"] = True
                                self.shows[name] = not(self.shows[name])

                                if x < self.width/2:
                                    self.left = True
                                    self.right = False
                                elif x >= self.width/2:
                                    self.right = True
                                    self.left = False
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

        # draw background and text
        self.win.blit(self.bg, (0,0))
        text = self.font.render(self.game_level, 2, rgb(255,255,255))
        self.win.blit(text, (self.width/2 - text.get_width()/2, self.height - 10 - text.get_height()))
        
        # draw mini-game button
        self.win.blit(casino_btn, (self.slot[0], self.slot[1]))

        # draw Start, Lore, Info, Level buttons
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

        # draw lore imgs
        if self.shows["lore"]:
            # right img
            x = self.lore[0] + pad_x
            y = self.lore[1]
            self.win.blit(lore_img, (x, y))

            # left img
            x = self.lore[0] - pad_x - lore2_img.get_width() + lore_btn.get_width()
            y = self.lore[1]
            self.win.blit(lore2_img, (x, y))

        # draw character infos, attack Towers (left), support Towers (right)
        if self.shows["info"] and not self.shows['img']:
            for button, img in zip(self.character_infos, self.info_imgs):
                self.win.blit(img, (button[0], button[1]))

        # draw characters
        corr = 0
        for name, img in zip(self.img_names, self.character_imgs):
            if self.shows[name]:
                x = img[1][0]
                y = img[1][1]
                self.win.blit(img[0], (x, y))

                if self.right:           
                    corr = img[0].get_width() + 10
                
                size = (900, 50)
                text = img[2]
                x = img[3][0] + corr
                y = img[3][1]
                self.blit_text(size, text, (x, y), self.font_20, rgb(255,255,255))

                for i, (button, info) in enumerate(zip(self.character_infos, self.info_imgs)):
                    if self.left:
                        if i >= 4 :
                            pass
                        else:
                            self.win.blit(info, (button[0], button[1]))
                    if self.right:
                        if i < 4:
                            pass
                        else:
                            self.win.blit(info, (button[0], button[1]))

        # draw level buttons
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

    def blit_text(self, surface, text, pos, font, color=pygame.Color('black')):
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = surface[0], surface[1]
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                self.win.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.

def play_sound(*args):
    if len(args) == 3:
        a,b,c = args[0],args[1],args[2]
        pygame.mixer.Channel(a).play(pygame.mixer.Sound(os.path.join("game_assets/sounds/", b)), maxtime=c)
    elif len(args) == 2:
        a,b = args[0],args[1]
        pygame.mixer.Channel(a).play(pygame.mixer.Sound(os.path.join("game_assets/sounds/", b)))


#### TEXT ####

text_shin = "Shin is the main protagonist of Kingdom. \nHe is a General of Qin and the leader of the Hi Shin Army.\n" \
        "\n" \
        "Swordman: he is able to easily cut down a large number of soldiers.\n" \
        "\n" \
        " - Damage: Low\n" \
        " - Range: Long\n" \
        " - Cost : Cheap\n" \
        " - Ability: None"

text_moubu = "Mou Bu is a Great General of Qin, the leader of Mou Bu Army, " \
        "and the head of the Mou Family, also a former member of the 'Four Pillars' of Ryo Fui.\n" \
        "Mou Bu has been called the 'Unrivaled Strongest Man in Qin' because of his brute force approach to battle.\n" \
        "\n" \
        "Mace User: he is able to easily cut down armor soldiers and Chu's Units.\n" \
        "\n" \
        " - Damage: High\n" \
        " - Range: Short\n" \
        " - Cost: Expensive\n" \
        " - Ability: Special Damage to Chu's Units (Warriors, Elephants, Boats)"

text_kanki = "Kan Ki is a General of Qin and the leader of Kan Ki Army. In the past he was a bandit leader with a penchant " \
        "for decapitation, which earned him the moniker 'The Beheader'.\n" \
        "\n" \
        "Swordman: he is able to easily cut down several units and Wei's Siege Units.\n" \
        "\n" \
        " - Damage: High Attack Speed\n" \
        " - Range: Short\n" \
        " - Cost: Medium\n" \
        " - Ability: Special Damage to Wei's Siege Units (Catapult, Balista)"

text_ouhon = "Ou Hon is a General of Qin. He is also the son of General Ou Sen, " \
        "a relative to the late Great General Ou Ki and the heir to the Ou Family.\n" \
        "\n" \
        "Spearman: he is able to freeze soldiers.\n" \
        "\n" \
        " - Damage: None\n" \
        " - Range: Short\n" \
        " - Cost : Expensive\n" \
        " - Ability: Freeze"

text_fortress = "Qin City, must be besieged by \n" \
        "enemies along their path.\n" \
        "\n" \
        " - Health: 500/1000/1500\n" \
        " - Weakness: Wei Siege Units\n" \

text_kyoukai = "Kyou Kai is a 5000-Man Commander and a \n lieutenant in the Hi Shin Unit, in which she \nconsiders herself, " \
        "and her unit, bound to. \n" \
        "Kyou Kai is also a former member of the \n legendary assassin Clan Shiyuu.\n" \
        "\n" \
        "Swordman: enhances towers' damage.\n" \
        "\n" \
        " - Damage: None\n" \
        " - Range: Short\n" \
        " - Cost : Expensive\n" \
        " - Ability: Enhance Tower Damage"

text_ten = "Ka Ryo Ten is the Strategist of the Hi Shin\n Unit and one of the best strategists \n" \
        "for the state of Qin. She is an orphan and\n the last descendant of a large mountain\n tribe.\n" \
        "\n" \
        "Blowgun: enhances towers' range.\n" \
        "\n" \
        " - Damage: None\n" \
        " - Range: Short\n" \
        " - Cost : Expensive\n" \
        " - Ability: Enhance Tower Range"

text_ryo = "Ryo Fui is a very powerful merchant and\n politic of the state of Qin. A former\n" \
        "Chancellor of the Right and later\n Chancellor of State of Qin, he was\n the leader of the Ryo Fui Faction\n" \
        "at the beginning of Ei Sei's reign.\n" \
        "\n" \
        " - Damage: None\n" \
        " - Range: Long\n" \
        " - Cost : Expensive\n" \
        " - Ability: Enhance Tower Gold Drops"