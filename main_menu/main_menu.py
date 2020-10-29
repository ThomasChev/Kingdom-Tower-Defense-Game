from game import Game
import pygame
import os
import time

start_btn = pygame.image.load(os.path.join("game_assets/menu/", "play_big_btn.png"))
lore_btn = pygame.image.load(os.path.join("game_assets/menu/", "lore_btn.png"))
lore_img = pygame.image.load(os.path.join("game_assets/menu/", "lore.png"))
info_btn = pygame.image.load(os.path.join("game_assets/menu/", "info_btn.png"))
info_shin_img = pygame.image.load(os.path.join("game_assets/menu/", "info_shin.png"))
info_moubu_img = pygame.image.load(os.path.join("game_assets/menu/", "info_shin.png"))
info_kanki_img = pygame.image.load(os.path.join("game_assets/menu/", "info_shin.png"))
info_fortress_img = pygame.image.load(os.path.join("game_assets/menu/", "info_fortress.png"))
info_kyoukai_img = pygame.image.load(os.path.join("game_assets/menu/", "info_shin.png"))
info_ten_img = pygame.image.load(os.path.join("game_assets/menu/", "info_shin.png"))

pygame.mixer.pre_init()
pygame.mixer.init()

class MainMenu:
    def __init__(self, win):
        self.width = 1200
        self.height = 700
        self.bg = pygame.image.load(os.path.join("game_assets/background/", "kingdom_menu.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.win = win
        self.btn = (self.width/2 - start_btn.get_width()/2, 225, start_btn.get_width(), start_btn.get_height())
        self.lore = (self.width/2 - lore_btn.get_width()/2, 300, lore_btn.get_width(), lore_btn.get_height())
        self.info = (self.width/2 - info_btn.get_width()/2, 375, info_btn.get_width(), info_btn.get_height())
        self.show_lore = False
        self.show_info = False

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
                    # check if hit start btn
                    x, y = pygame.mouse.get_pos()

                    if self.btn[0] <= x <= self.btn[0] + self.btn[2]:
                        if self.btn[1] <= y <= self.btn[1] + self.btn[3]:
                            pygame.mixer.music.stop()
                            play_sound(1,"next_round.wav")
                            game = Game(self.win)
                            game.run()
                            self.show_lore = False
                            self.show_info = False
                            del game
                    if self.lore[0] <= x <= self.lore[0] + self.lore[2]:
                        if self.lore[1] <= y <= self.lore[1] + self.lore[3]:
                            self.show_info = False
                            self.show_lore = not(self.show_lore)
                    if self.info[0] <= x <= self.info[0] + self.info[2]:
                        if self.info[1] <= y <= self.info[1] + self.info[3]:
                            self.show_lore = False
                            self.show_info = not(self.show_info)

            self.draw()

        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0,0))

        self.win.blit(start_btn, (self.btn[0], self.btn[1]))
        self.win.blit(lore_btn, (self.lore[0], self.lore[1]))
        self.win.blit(info_btn, (self.info[0], self.info[1]))

        pad_x = 75
        pad_y = 5
        if self.show_lore:
            x = self.lore[0] + pad_x
            y = self.lore[1]
            self.win.blit(lore_img, (x, y))
        if self.show_info:
            x = self.info[0] + pad_x
            y = self.info[1]
            add_x = -(2*pad_x + info_shin_img.get_width())
            add_y = info_shin_img.get_height() + pad_y
            self.win.blit(info_shin_img, (x + add_x, y + 0*add_y ))
            self.win.blit(info_moubu_img, (x + add_x, y + 1*add_y ))
            self.win.blit(info_kanki_img, (x + add_x, y + 2*add_y ))
            self.win.blit(info_fortress_img, (x, y + 0*add_y ))
            self.win.blit(info_kyoukai_img, (x, y + 1*add_y ))
            self.win.blit(info_ten_img, (x, y + 2*add_y ))

        pygame.display.update()


def play_sound(*args):
    if len(args) == 3:
        a,b,c = args[0],args[1],args[2]
        pygame.mixer.Channel(a).play(pygame.mixer.Sound(os.path.join("game_assets/sounds/", b)), maxtime=c)
    elif len(args) == 2:
        a,b = args[0],args[1]
        pygame.mixer.Channel(a).play(pygame.mixer.Sound(os.path.join("game_assets/sounds/", b)))
