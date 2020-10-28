import pygame # pygame-1.9.6-cp38-cp38-win_amd64.whl
import os

from enemies.zao_warrior import Zao_warrior
from enemies.yan_warrior import Yan_warrior
from enemies.qi_warrior import Qi_warrior
from enemies.wei_catapult import Wei_catapult
from enemies.wei_balista import Wei_balista
from enemies.han_warrior import Han_warrior
from enemies.chu_warrior import Chu_warrior
from enemies.chu_elephant import Chu_elephant
from enemies.chu_boat import Chu_boat
from enemies.yan_boat import Yan_boat
from enemies.qi_boat import Qi_boat
from enemies.zao_riboku import Zao_riboku
from towers.quinTower import ShinTower, MoubuTower, KankiTower
from towers.supportTower import TenTower, KyoukaiTower
from towers.fortress import Fortress
from kingdoms.quin_base import Quin_base
from kingdoms.zao_base import Zao_base
from kingdoms.yan_base import Yan_base
from kingdoms.qi_base import Qi_base
from kingdoms.wei_base import Wei_base
from kingdoms.han_base import Han_base
from kingdoms.chu_base import Chu_base
from kingdoms.chu2_base import Chu2_base
from kingdoms.chu3_base import Chu3_base
from menu.menu import VerticalMenu, PlayPauseButton

import time
import random

pygame.font.init()
pygame.init()


lives_img = pygame.image.load(os.path.join("game_assets/menu/","heart.png"))
money_img = pygame.image.load(os.path.join("game_assets/menu/","star.png"))
side_img = pygame.image.load(os.path.join("game_assets/menu/","side.png"))
side_btn = pygame.image.load(os.path.join("game_assets/menu/","side_btn.png"))

buy_shin = pygame.image.load(os.path.join("game_assets/quin_towers/shin_icon","buy_shin.png"))
buy_moubu = pygame.image.load(os.path.join("game_assets/quin_towers/moubu_icon","buy_moubu.png"))
buy_kanki = pygame.image.load(os.path.join("game_assets/quin_towers/kanki_icon","buy_kanki.png"))
buy_kyoukai = pygame.image.load(os.path.join("game_assets/support_towers/kyoukai_icon","buy_kyoukai.png"))
buy_ten = pygame.image.load(os.path.join("game_assets/support_towers/ten_icon","buy_ten.png"))
buy_fortress = pygame.image.load(os.path.join("game_assets/fortress/fortress_icon","buy_fortress.png"))

play_btn = pygame.image.load(os.path.join("game_assets/menu/","play_btn.png"))
pause_btn = pygame.image.load(os.path.join("game_assets/menu/","pause_btn.png"))
sound_btn = pygame.image.load(os.path.join("game_assets/menu/","music_btn.png"))
sound_btn_off= pygame.image.load(os.path.join("game_assets/menu/","music_off_btn.png"))

wave_bg = pygame.image.load(os.path.join("game_assets/menu/","wave.png"))

attack_tower_names = ["shin", "moubu", "kanki"]
support_tower_names = ["ten", "kyoukai"]
fortress_names = ["fortress"]

# initialize background music
pygame.mixer.pre_init()
pygame.mixer.init()
pygame.mixer.music.load(os.path.join("game_assets/sounds/", "loop0.wav"))
# pygame.mixer.music.load(os.path.join("game_assets/sounds/", "ending.mp3"))
pygame.mixer.music.set_volume(0.4)

# frequency of enemies [Zao_w, Yan_w, Qi_w, Wei_c, Wei_b, Han_w, Chu_w, Chu_e, Chu_b, Yan_b, Qi_b, Zao_r]
waves = [[3,0,0,3,3,3,0,0,0,0,0,0],[3,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0,0,0],[0,3,0,0,0,0,0,0,0,0,0,0],[0,0,2,0,0,0,0,0,0,0,0,0],[0,0,4,0,0,0,0,0,0,0,0,0],[0,0,0,2,0,0,0,0,0,0,0,0],[0,0,0,4,0,0,0,0,0,0,0,0],[0,0,0,0,4,0,0,0,0,0,0,0],[0,0,0,0,6,0,0,0,0,0,0,0],[0,0,0,0,0,4,0,0,0,0,0,0],[0,0,0,0,0,6,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0,0,0],[0,0,0,0,0,0,6,0,0,0,0,0],[0,0,0,0,0,0,0,2,0,0,0,0],[0,0,0,0,0,0,0,6,0,0,0,0],[0,0,0,0,0,0,0,0,2,0,0,0],[0,0,0,0,0,0,0,0,6,0,0,0],[0,0,0,0,0,0,0,0,0,2,0,0],[0,0,0,0,0,0,0,0,0,10,0,0],[0,0,0,0,0,0,0,0,0,0,2,0],[0,0,0,0,0,0,0,0,0,0,8,0],[9,0,0,0,0,0,0,0,0,0,0,0],[0,7,0,0,0,0,0,0,0,3,0,0],[0,0,9,0,0,0,0,0,0,0,4,0],[0,0,0,5,5,0,0,0,0,0,0,0],[0,0,0,0,0,14,0,0,0,0,0,0],[0,0,0,0,0,0,4,4,4,0,0,0],[5,5,5,0,0,0,0,0,0,0,0,0],[0,18,0,0,0,0,0,0,0,0,0,0],[3,3,3,0,0,3,6,0,0,0,0,0],[3,6,3,0,0,3,6,0,0,0,0,0],[0,0,0,0,0,10,8,0,0,0,0,0],[0,0,0,0,0,0,0,0,16,0,0,0],[0,0,0,0,0,0,0,0,0,18,0,0],[0,0,0,0,0,0,0,0,0,0,20,0],[0,0,0,0,0,0,0,0,12,6,6,0],[11,11,11,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,16,18,0,0,0,0,0],[8,8,10,0,0,10,8,0,0,0,0,0],[9,9,9,0,0,9,9,0,0,0,0,0],[0,35,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,35,0,0,0],[0,0,0,0,0,0,0,0,0,35,0,0],[0,0,0,0,0,0,0,0,0,0,33,0],[0,0,0,0,0,0,0,0,12,12,15,0],[35,0,0,0,0,0,0,0,0,0,0,0],[0,29,0,0,0,0,0,0,0,0,0,0],[0,0,12,10,12,0,0,4,0,0,0,0],[10,10,10,4,4,10,10,4,4,4,4,0],[10,10,10,6,6,10,10,4,4,4,4,0],[10,10,10,6,6,10,10,6,4,4,4,0],[10,10,10,6,6,10,10,6,6,6,6,0],[12,15,10,8,8,10,10,8,6,6,6,0],[12,20,10,8,8,10,10,10,6,6,6,1]]
waves = [[1,0,1,0,0,0,0,0,0,0,0,0]]
spawn_rates = [2,0.2,1,3,3,1,1,5,2,2,2,1]
class Game():
    def __init__(self, win):
        self.width = 1200
        self.height = 700
        self.win = win
        self.enemys = []
        self.attack_towers = []
        self.support_towers = []
        self.fortress = []
        self.lives = 10
        self.money = 125
        self.bg = pygame.image.load(os.path.join("game_assets/background/", "kingdom.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.clicks = [] # remove
        self.timer = time.time()
        self.life_font = pygame.font.Font("game_assets/fonts/ZealotCollege-8v9g.ttf", 28)
        self.money_font = pygame.font.Font("game_assets/fonts/UDDigiKyokashoN-R.ttc", 32)
        self.wave_font = pygame.font.Font("game_assets/fonts/UDDigiKyokashoN-R.ttc", 16)
        self.selected_tower = None
        self.menu = VerticalMenu(self.width - 62, 125, side_img)
        self.menu.add_btn(buy_shin, "buy_shin", 20)
        self.menu.add_btn(buy_moubu, "buy_moubu", 60)
        self.menu.add_btn(buy_kanki, "buy_kanki", 40)
        self.menu.add_btn(buy_fortress, "buy_fortress", 500)
        self.menu.add_btn(buy_kyoukai, "buy_kyoukai", 150)
        self.menu.add_btn(buy_ten, "buy_ten", 150)
        self.moving_object = None
        self.wave = 0
        self.current_wave = waves[self.wave][:]
        self.pause = False
        self.playPauseButton = PlayPauseButton(play_btn, pause_btn, self.width/2 - 118, 0)
        self.soundButton = PlayPauseButton(sound_btn, sound_btn_off, self.width/2 + 88, 0)
        self.sideButton = PlayPauseButton(side_btn, side_btn, self.width - 40, 272)
        self.music_on = True
        self.menu_on = False
        self.shake = False
        self.current_spawn_rate = 0.5
        self.spawn_rate = spawn_rates[:]
        self.fortress_sound = False
        self.to_resist = []
        self.first_contact = True
        self.go_lose = False
        self.go_win = False
        self.kingdom = [Quin_base(), 
                        Zao_base(), 
                        Yan_base(), 
                        Qi_base(), 
                        Wei_base(), 
                        Han_base(), 
                        Chu_base(), 
                        Chu2_base(), 
                        Chu3_base()]

    def gen_enemies(self):
        """
        generate the next enemy or enemies to show
        :return: enemy
        """
        if sum(self.current_wave) == 0:
            if len(self.enemys) == 0:
                self.wave += 1
                if self.wave < len(waves):
                    play_sound(1,"next_round.wav")
                    self.fortress_sound = False
                    self.pause = True
                    self.playPauseButton.paused = self.pause
                    self.current_wave = waves[self.wave]
                else:
                    time.sleep(0.7)
                    self.go_win = True
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(os.path.join("game_assets/sounds/", "ending.mp3"))
                    pygame.mixer.music.play(loops=0)
                    time.sleep(0.4)
  
                    print("You Win")
        else:
            wave_enemies = [Zao_warrior(),
                            Yan_warrior(),
                            Qi_warrior(),
                            Wei_catapult(),
                            Wei_balista(),
                            Han_warrior(),
                            Chu_warrior(),
                            Chu_elephant(),
                            Chu_boat(),
                            Yan_boat(),
                            Qi_boat(),
                            Zao_riboku()
                            ]
            for x in range(len(self.current_wave)):
                self.current_spawn_rate = self.spawn_rate[x]
                if self.current_wave[x] != 0:
                    self.enemys.append(wave_enemies[x])
                    self.current_wave[x] = self.current_wave[x] - 1
                    break

    def run(self):
        # start playing the background music
        pygame.mixer.music.load(os.path.join("game_assets/sounds/", "loop0.wav"))
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(loops=-1) # loop forever
        self.fade(self.width, self.height, (0,0,0), 1)

        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(400)
            
            if self.pause == False:
                # gen monsters
                if time.time() - self.timer >= self.current_spawn_rate: # if time.time() - self.timer >= random.randrange(1,5)/2:
                    self.timer = time.time()
                    self.gen_enemies()  # self.enemys.append(random.choice([Zao_warrior(), Yan_warrior(), Qi_warrior(), Han_warrior(), Chu_warrior()]))

            pos = pygame.mouse.get_pos()
            # check for moving object
            if self.moving_object:
                self.moving_object.move(pos[0], pos[1])
                tower_list = self.attack_towers[:] + self.support_towers[:] + self.fortress[:]
                collide = False
                for tower in tower_list:
                    if tower.collide(self.moving_object):
                        collide = True
                    #     tower.place_color = (255, 0, 0, 100)
                    #     self.moving_object.place_color = (255, 0, 0, 100)
                    # else:
                    #     tower.place_color = (0, 0, 255, 100)
                    #     if not collide:
                    #         self.moving_object.place_color = (0, 0, 255, 100)


            # main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONUP:

                    # if you're moving an object and click it
                    if self.moving_object:
                        if self.moving_object.name in fortress_names:
                            tower_list = self.fortress[:]
                        else:
                            tower_list = self.attack_towers[:] + self.support_towers[:]
                        
                        not_allowed = False
                        if not tower_list:
                            if self.moving_object.collide(self.moving_object):
                                not_allowed = True 
                                play_sound(1,"buzz.wav",600)
                        for tower in tower_list:
                            if tower.collide(self.moving_object):
                                not_allowed = True
                                play_sound(1,"buzz.wav",600)
                        if not not_allowed and self.point_to_line(self.moving_object):
                            if self.moving_object.name in attack_tower_names:
                                self.attack_towers.append(self.moving_object)
                            elif self.moving_object.name in support_tower_names:
                                self.support_towers.append(self.moving_object)
                            elif self.moving_object.name in fortress_names:
                                self.fortress.append(self.moving_object)
                                self.first_contact = True
                            self.moving_object.moving = False
                            self.moving_object = None
                            play_sound(1,"put_tower.wav",600)

                    else:
                        # toggle play/pause
                        if self.playPauseButton.click(pos[0], pos[1]):
                            play_sound(1,"play_pause.wav",300)
                            self.pause = not(self.pause)
                            self.playPauseButton.paused = self.pause

                        # toggle music
                        if self.soundButton.click(pos[0], pos[1]):
                            self.music_on = not(self.music_on)
                            self.soundButton.paused = self.music_on
                            if self.music_on:
                                pygame.mixer.music.unpause()
                            else:
                                pygame.mixer.music.pause()

                        # toggle side menu
                        if self.sideButton.click(pos[0], pos[1]):
                            play_sound(1,"toggle.wav",600)
                            self.menu_on = not(self.menu_on)
                            self.sideButton.paused = self.menu_on
                            self.sideButton.play = pygame.transform.flip(self.sideButton.play, True, False)

                            
                        # look if you click on side menu
                        if self.menu_on:
                            side_menu_button = self.menu.get_clicked(pos[0], pos[1])
                            if side_menu_button:
                                cost = self.menu.get_item_cost(side_menu_button)
                                if self.money >= cost:
                                    play_sound(1,"buy.wav",600)
                                    self.money -= cost
                                    self.add_tower(side_menu_button)
                                else:
                                    self.shake = True
                                    play_sound(1,"buzz.wav",600)

                        # look if you clicked on attack tower or support tower
                        btn_clicked = None
                        if self.selected_tower:
                            btn_clicked = self.selected_tower.menu.get_clicked(pos[0], pos[1])
                            if btn_clicked:
                                if btn_clicked == "Upgrade":
                                    cost = self.selected_tower.get_upgrade_cost()
                                    if self.money >= cost:
                                        self.money -= cost
                                        self.selected_tower.upgrade()
                                        play_sound(1,"buy.wav",600)
                                    else:
                                        self.shake = True
                                        play_sound(1,"buzz.wav",600)
                                if btn_clicked == "Sell":
                                    refund = self.selected_tower.sell()
                                    self.money += refund
                                    play_sound(1,"sell.wav",200)
                                    if self.selected_tower.name in attack_tower_names:
                                        self.attack_towers.remove(self.selected_tower)
                                    elif self.selected_tower.name in support_tower_names:
                                        self.support_towers.remove(self.selected_tower)


                        if not btn_clicked:
                            # look if you clicked on attack tower
                            for tw in self.attack_towers:
                                if tw.click(pos[0], pos[1]):
                                    tw.selected = True
                                    self.selected_tower = tw
                                else:
                                    tw.selected = False

                            # look if you clicked on support tower
                            for tw in self.support_towers:
                                if tw.click(pos[0], pos[1]):
                                    tw.selected = True
                                    self.selected_tower = tw
                                else:
                                    tw.selected = False

                            # look if you clicked on fortress
                            for ft in self.fortress:
                                if ft.click(pos[0], pos[1]):
                                    ft.selected = True
                                    self.selected_tower = ft
                                else:
                                    ft.selected = False

                            # look if you clicked on kingdom's base
                            for base in self.kingdom:
                                if base.click(pos[0], pos[1]):
                                    base.selected = True
                                    # self.selected_tower = ft
                                else:
                                    base.selected = False

                        # self.clicks.append(pos)
                        # print(self.clicks)

            if not self.pause:
                to_del = []
                # to_resist = []

                # loop through enemies
                for en in self.enemys:
                    # move enemies along the path
                    en.move()
                    if en.x < 46:
                        to_del.append(en)
                        play_sound(1,"beep.wav",600)

                    # loop through fortress
                    for ft in self.fortress:
                        # block enemies next to a fortress, and the fortress loses health
                        if en.collide(ft):
                            self.fortress_sound = True
                            if self.first_contact:
                                play_sound(1,"melee.wav",1600)
                                self.first_contact = False
                            self.to_resist.append(en)
                            ft.resist(en)
                            # check if the fortress has collapsed
                            if not ft.resist(en):
                                play_sound(1,"collapse.wav",1600)
                                ft.collapse = True
                                self.first_contact = True

                # delete all enemies off the screen
                for d in to_del:
                    self.lives -= 1
                    self.enemys.remove(d)

                # loop through attack towers
                for tw in self.attack_towers:
                    self.money += tw.attack(self.enemys)

                # loop through support towers
                for tw in self.support_towers:
                    tw.support(self.attack_towers)

                # loop through fortress, remove it if collapsed and move enemies 
                for ft in self.fortress:
                    if ft.collapse:
                        self.fortress_sound = False
                        self.fortress.remove(ft)
                        for en in self.to_resist:
                            en.block = False
                
                # play fortress sound if activated
                if self.fortress_sound:
                    if random.randint(0,60) == 10:
                        play_sound(1,"melee.wav",1600)

                # if you lose
                if self.lives <= 0:
                    play_sound(1,"beep.wav",600)
                    time.sleep(0.7)
                    pygame.mixer.music.pause()
                    play_sound(1,"game_over.wav")
                    time.sleep(2.4)
                    print("You Lose")
                    self.go_lose = True
                    pygame.mixer.music.load(os.path.join("game_assets/sounds/", "melody.wav"))
                    pygame.mixer.music.play(loops=-1)

                if self.go_win or self.go_lose:
                    self.fade(self.width, self.height, (0,0,0), 8)
                    run = False

            self.draw()
            self.shake = False

        # pygame.quit()



    def point_to_line(self, tower):
        """
        returns if you can place tower based on distance from
        path
        :param tower: Tower
        :return: Bool
        """
        # find two closest points
        return True

    def draw(self):
        self.win.blit(self.bg, (0, 0))

        # for p in self.clicks:
        # 	pygame.draw.circle(self.win, (255, 0, 0), (p[0], p[1]), 5, 0)

        # draw placement rings
        # if self.moving_object:
        #     for tower in self.attack_towers:
        #         tower.draw_placement(self.win)

        #     for tower in self.support_towers:
        #         tower.draw_placement(self.win)

        #     self.moving_object.draw_placement(self.win)

        # draw kingdom's base
        for kingdoms in self.kingdom:
            kingdoms.draw(self.win)

        # draw attack towers
        for tw in self.attack_towers:
            tw.draw(self.win)

        # draw support towers
        for tw in self.support_towers:
            tw.draw(self.win)

        # draw fortress
        for ft in self.fortress:
            ft.draw(self.win)

        # draw enemies
        for en in self.enemys:
            en.draw(self.win)

        # draw moving object
        if self.moving_object:
            self.moving_object.draw(self.win)

        # draw menu
        if self.menu_on:
            self.menu.draw(self.win)

        # draw side button
        if self.menu_on:
            self.sideButton.x = self.width - 128
            self.sideButton.y = 272
        else:
            self.sideButton.x = self.width - 40
            self.sideButton.y = 272
        self.sideButton.draw(self.win)

        # draw play pause button
        self.playPauseButton.draw(self.win)

        # draw music toggle button
        self.soundButton.draw(self.win)

        # draw wave
        self.win.blit(wave_bg, (self.width - 100, self.height - 48))
        text = self.wave_font.render("Wave " + str(self.wave), 2, (255,255,255))
        self.win.blit(text, (self.width - 100 + wave_bg.get_width()/2 - text.get_width()/2, self.height - 45))

        # draw lives
        start_x = 10
        start_y = 0
        text = self.life_font.render(str(self.lives), 2, (255, 255, 255))
        add_x = text.get_width() + 10
        add_y = 3
        self.win.blit(text, (start_x, start_y))
        self.win.blit(lives_img, (start_x + add_x, start_y + add_y))

        # draw money
        text = self.money_font.render(str(self.money), 2, (255, 255, 255))
        add_shake = 0
        if self.shake:
            add_shake = 18
        start_x = self.width - money_img.get_width() - text.get_width() - 15
        start_y = 0
        add_x = 0 + add_shake
        self.win.blit(text, (start_x + add_x, start_y))
        add_x = text.get_width() + 10 + add_shake
        self.win.blit(money_img, (start_x + add_x, start_y))

        pygame.display.update()

    def add_tower(self, name):
        x, y = pygame.mouse.get_pos()
        name_list = ["buy_shin", "buy_moubu", "buy_kanki", "buy_fortress", "buy_kyoukai", "buy_ten",]
        object_list = [ShinTower(x,y), MoubuTower(x, y), KankiTower(x, y), Fortress(x, y), KyoukaiTower(x, y), TenTower(x, y)]

        try:
            obj = object_list[name_list.index(name)]
            self.moving_object = obj
            obj.moving = True
        except Exception as e:
            print(str(e) + "NOT VALID NAME")


    def show_info(self):
        self.win.blit(self.bg, (0, 0))
    
    def fade(self, width, height, color, speed): 
        fade = pygame.Surface((width, height))
        fade.fill(color)
        for alpha in range(0, 300):
            fade.set_alpha(alpha)
            # redrawWindow()
            self.win.blit(fade, (0,0))
            pygame.display.update()
            pygame.time.delay(speed)

def play_sound(*args):
    if len(args) == 3:
        a,b,c = args[0],args[1],args[2]
        pygame.mixer.Channel(a).play(pygame.mixer.Sound(os.path.join("game_assets/sounds/", b)), maxtime=c)
    elif len(args) == 2:
        a,b = args[0],args[1]
        pygame.mixer.Channel(a).play(pygame.mixer.Sound(os.path.join("game_assets/sounds/", b)))



# win = pygame.display.set_mode((1200, 700))
# g = Game(win)
# g.run()