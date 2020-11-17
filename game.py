import pygame # pygame-1.9.6-cp38-cp38-win_amd64.whl
import os
import math
import time
import random
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
from collections import deque

# enemies
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

# towers
from towers.quinTower import ShinTower, MoubuTower, KankiTower, OuhonTower
from towers.supportTower import TenTower, KyoukaiTower, RyoTower
from towers.fortress import Fortress

# kingdoms
from kingdoms.quin_base import Quin_base
from kingdoms.zao_base import Zao_base
from kingdoms.yan_base import Yan_base
from kingdoms.qi_base import Qi_base
from kingdoms.wei_base import Wei_base
from kingdoms.han_base import Han_base
from kingdoms.chu_base import Chu_base
from kingdoms.chu2_base import Chu2_base
from kingdoms.chu3_base import Chu3_base
from menu.menu import VerticalMenu, PlayPauseButton, ReturnButton
from game_assets.colors import rgb

from explosions.explosion import Explosion 

pygame.font.init()
pygame.init()

# game images
img_dir = "game_assets/menu/"
lives_img = pygame.image.load(os.path.join(img_dir,"heart.png"))
money_img = pygame.image.load(os.path.join(img_dir,"star.png"))
side_img = pygame.image.load(os.path.join(img_dir,"side.png"))
side_btn = pygame.image.load(os.path.join(img_dir,"side_btn.png"))
gold_bag = pygame.image.load(os.path.join(img_dir, "gold_bag.png"))
wave_bg = pygame.image.load(os.path.join(img_dir,"wave_sign.png"))
alert_red = pygame.image.load(os.path.join(img_dir,"alert_red.png")) # red alert
alert_white = pygame.image.load(os.path.join(img_dir,"alert_white.png")) # white alert

# tower icons images
img_dir = "game_assets/"
buy_shin = pygame.image.load(os.path.join(img_dir + "quin_towers/shin_icon","buy_shin.png"))
buy_moubu = pygame.image.load(os.path.join(img_dir + "quin_towers/moubu_icon","buy_moubu.png"))
buy_kanki = pygame.image.load(os.path.join(img_dir + "quin_towers/kanki_icon","buy_kanki.png"))
buy_ouhon = pygame.image.load(os.path.join(img_dir + "quin_towers/ouhon_icon","buy_ouhon.png"))
buy_kyoukai = pygame.image.load(os.path.join(img_dir + "support_towers/kyoukai_icon","buy_kyoukai.png"))
buy_ten = pygame.image.load(os.path.join(img_dir + "support_towers/ten_icon","buy_ten.png"))
buy_ryo = pygame.image.load(os.path.join(img_dir + "support_towers/ryo_icon","buy_ryo.png"))
buy_fortress = pygame.image.load(os.path.join(img_dir + "fortress/fortress_icon","buy_fortress.png"))

# button images
img_dir = "game_assets/menu/"
play_btn = pygame.image.load(os.path.join(img_dir,"play_btn.png"))
pause_btn = pygame.image.load(os.path.join(img_dir,"pause_btn.png"))
speed1_btn = pygame.image.load(os.path.join(img_dir,"speed1_btn.png"))
speed2_btn = pygame.image.load(os.path.join(img_dir,"speed2_btn.png"))
speed3_btn = pygame.image.load(os.path.join(img_dir,"speed3_btn.png"))
sound_btn = pygame.image.load(os.path.join(img_dir,"music_btn.png"))
sound_btn_off= pygame.image.load(os.path.join(img_dir,"music_off_btn.png"))

# tower lists
attack_tower_names = ["shin", "moubu", "kanki", "ouhon"]
support_tower_names = ["ten", "kyoukai", "ryo"]
fortress_names = ["fortress"]

# initialize background music
SONG_END = pygame.USEREVENT + 1
pygame.mixer.pre_init()
pygame.mixer.init()
pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load(os.path.join("game_assets/sounds/", "loop0.wav"))
pygame.mixer.music.play()

# waves  list and enemies list
waves = [[3,1,0,0,0,0,0,0,0,0,1,0],[1,0,0,1,0,0,0,1,1,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1],[1,0,0,0,0,2,2,0,1,1,1,0], [1,1,1,1,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0], [1,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0], [1,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0]]
# waves = [[3,0,0,0,0,0,0,0,0,0,0,0],[6,0,0,0,0,0,0,0,0,0,0,0],[0,3,0,0,0,0,0,0,0,0,0,0],[0,5,0,0,0,0,0,0,0,0,0,0],[0,0,3,0,0,0,0,0,0,0,0,0],[0,0,6,0,0,0,0,0,0,0,0,0],[0,0,0,2,0,0,0,0,0,0,0,0],[0,0,0,4,0,0,0,0,0,0,0,0],[0,0,0,0,4,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,0,0,0,0],[0,0,0,0,0,4,0,0,0,0,0,0],[0,0,0,0,0,6,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0,0,0],[0,0,0,0,0,0,6,0,0,0,0,0],[0,0,0,0,0,0,0,2,0,0,0,0],[0,0,0,0,0,0,0,6,0,0,0,0],[0,0,0,0,0,0,0,0,2,0,0,0],[0,0,0,0,0,0,0,0,6,0,0,0],[0,0,0,0,0,0,0,0,0,2,0,0],[0,4,0,0,0,0,0,0,4,4,0,0],[0,0,0,0,0,0,0,0,0,0,2,0],[0,0,0,0,0,0,0,0,0,0,8,0],[9,0,0,0,0,0,0,0,0,0,0,0],[0,8,0,0,0,0,0,0,0,3,0,0],[0,0,9,0,0,0,0,0,0,0,4,0],[0,0,0,3,5,0,0,0,0,0,0,0],[0,0,0,0,0,14,0,0,0,0,0,0],[0,0,0,0,0,0,4,4,4,0,0,0],[5,5,5,0,0,0,0,0,0,0,0,0],[0,12,0,0,0,0,0,0,0,0,0,0],[3,3,3,0,0,3,6,0,0,0,0,0],[3,6,3,0,0,3,6,0,0,0,0,0],[0,0,0,0,0,10,8,0,0,0,0,0],[0,0,0,0,0,0,0,0,16,0,0,0],[0,0,0,0,0,0,0,0,0,18,0,0],[0,0,0,0,0,0,0,0,0,0,20,0],[0,0,0,0,0,0,0,0,12,6,6,0],[11,11,11,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,16,18,0,0,0,0,0],[8,8,10,0,0,10,8,0,0,0,0,0],[9,9,9,0,0,9,9,0,0,0,0,0],[0,25,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,12,12,0,0],[0,0,0,0,0,0,0,0,12,0,12,0],[0,0,0,0,0,0,0,0,12,8,8,0],[0,0,0,0,0,0,0,0,12,12,15,0],[18,12,0,0,0,0,0,0,0,0,0,0],[18,15,0,0,0,0,0,0,0,0,0,0],[0,0,12,8,12,0,0,4,0,0,0,0],[10,10,10,4,4,10,10,4,4,4,4,0],[10,10,10,6,6,10,10,4,4,4,4,0],[10,10,10,6,6,10,10,6,4,4,4,0],[10,10,10,6,6,10,10,6,6,6,6,0],[12,15,10,8,8,10,10,8,6,6,6,0],[12,20,10,8,8,10,10,12,6,6,6,1]]
enemy_nickname = ["Zao Warrior", "Yan Warrior", "Qi Warrior", "Wei Catapult", "Wei Balista", "Han Warrior", "Chu Warrior", "Chu Elephant", "Chu Boat", "Yan Boat", "Qi Boat", "Zao Riboku"]
spawn_rates = [1.5,0.2,1,3,3,1,1,5,2,2,2,1]
break_round = 10
all_sprites = pygame.sprite.Group()

class Game():
    def __init__(self, win):

        # Basics
        self.win = win
        self.width = 1200
        self.height = 700
        self.lives = 20
        self.money = 35000
        self.bg = pygame.image.load(os.path.join("game_assets/background/", "kingdom.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.clicks = [] # use to see clicks
        self.timer = time.time()
        self.go_lose = False
        self.go_win = False
        
        # Actors
        self.enemys = []
        self.attack_towers = []
        self.support_towers = []
        self.fortress = []
        self.fortress_sold = []
        self.selected_tower = None
        self.moving_object = None
        self.draw_drop = False
        self.drop_x = 0
        self.drop_y = 0
        self.reward = 0
        
        # Side Tower menu
        self.menu = VerticalMenu(self.width - 45, 46, side_img)
        self.menu.add_btn(buy_shin, "buy_shin", 40)
        self.menu.add_btn(buy_moubu, "buy_moubu", 120)
        self.menu.add_btn(buy_kanki, "buy_kanki", 80)
        self.menu.add_btn(buy_ouhon, "buy_ouhon", 150)
        self.menu.add_btn(buy_fortress, "buy_fortress", 200)
        self.menu.add_btn(buy_kyoukai, "buy_kyoukai", 100)
        self.menu.add_btn(buy_ten, "buy_ten", 100)
        self.menu.add_btn(buy_ryo, "buy_ryo", 100)

        # Buttons and options
        self.life_font = self.money_font = pygame.font.Font("game_assets/fonts/SF Atarian System.ttf", 32)
        self.wave_font = pygame.font.Font("game_assets/fonts/SF Atarian System.ttf", 18)
        self.wave_font2 = pygame.font.Font("game_assets/fonts/SF Atarian System.ttf", 72)
        self.playPauseButton = PlayPauseButton(play_btn, pause_btn, self.width/2 - 118, 0, False)
        self.soundButton = PlayPauseButton(sound_btn, sound_btn_off, self.width/2 + 88, 0, True)
        self.sideButton = PlayPauseButton(side_btn, side_btn, self.width - 33, 272, False)
        self.speedButton = ReturnButton(speed1_btn, speed2_btn, speed3_btn, self.width/2 - 170, 0)
        self.speed = 1
        self.shake_money = False
        self.shake_life = False
        self.change_sound = False
        
        # Fortress
        self.fortress_sound = False
        self.to_resist = []
        self.first_contact = True
        
        # Wave and Gen enemies
        self.wave = 0
        self.current_wave = waves[self.wave][:]
        self.spawn_rate = spawn_rates[:]
        self.current_spawn_rate = 1.5
        self.kingdom = [Quin_base(),Zao_base(),Yan_base(),Qi_base(),Wei_base(),Han_base(),Chu_base(),Chu2_base(),Chu3_base()]
        self.current_kingdom = self.kingdom[0]
        self.next_spawn = False
    
        # Game level
        self.level = ""
        self.lvl = {"Easy":0, "Medium":1, "Hard":2}
        self.coef_rate = 1

        # Graphs 
        self.start_ticks = 0
        self.seconds = 0
        # Plot-1
        self.df = pd.DataFrame()
        self.data_dict = {'seconds':[],'waves':[],'money':[], 'lives':[], 'money_earnt':[], 'money_spent':[],'shin':[], 'moubu':[], 'kanki':[], 'ouhon':[], 'ten':[], 'kyoukai':[], 'ryo':[],'fortress':[], 'towers':[]}
        self.counters = {'shin':0,'moubu':0, 'kanki':0, 'ouhon':0, 'ten':0, 'kyoukai':0, 'ryo':0 ,'fortress':0}
        self.money_earnt = 0
        self.money_spent = 0
        # Plot-2
        self.df_enemies = pd.DataFrame(data={'waves':[], 'spawned':[], 'killed':[],"Zao Warrior":[], "Yan Warrior":[], "Qi Warrior":[], "Wei Catapult":[], "Wei Balista":[], "Han Warrior":[], "Chu Warrior":[], "Chu Elephant":[], "Chu Boat":[], "Yan Boat":[], "Qi Boat":[], "Zao Riboku":[]})
        self.not_killed = {"zao_warrior":0, "yan_warrior":0, "qi_warrior":0, "wei_catapult":0, "wei_balista":0, "han_warrior":0, "chu_warrior":0, "chu_elephant":0, "chu_boat":0, "yan_boat":0, "qi_boat":0, "zao_riboku":0}
        self.counter_gold = {"Gold Earnt":[], "Enemies (Type)":[]}
        self.list_enemy_spawned = [0,0,0,0,0,0,0,0,0,0,0,0]
        self.not_kill_count = 0
        self.spawn_count = 0

    
    def gen_enemies(self):
        """
        generate the next enemy or enemies to show
        :return: enemy, kingdom
        """

        wave_compo = [(Zao_warrior(),Zao_base()), (Yan_warrior(),Yan_base()), (Qi_warrior(),Qi_base()), (Wei_catapult(),Wei_base()), (Wei_balista(),Wei_base()), (Han_warrior(),Han_base()), (Chu_warrior(),Chu_base()), (Chu_elephant(),Chu2_base()), (Chu_boat(),Chu3_base()), (Yan_boat(),Yan_base()), (Qi_boat(),Qi_base()), (Zao_riboku(),Zao_base())]
        
        # Wave has finished
        if sum(self.current_wave) == 0:
            self.next_spawn = True

            # go to next wave
            if len(self.enemys) == 0:
                self.wave += 1

                # Go to next wave
                if self.wave < len(waves):
                    next_wave = waves[self.wave][:]

                    # play sound, write wave number and shade
                    if self.wave > 0:
                        # change music (epic AOE) at wave 10
                        if not self.change_sound and self.wave >= break_round - 1:
                            pygame.mixer.music.stop()
                            self.change_sound = True
                            play_next_song()
                        if not self.change_sound:
                            play_sound(0,"next_round.wav")
                        next_intro = [w_comp[0] for w_comp,w in zip(wave_compo, next_wave) if w>0]
                        self.fade(self.width, self.height, rgb(0,0,0), 0, 50, 60, next_intro)  # (width, height, color, start=0, end=300, delay=1)
                    
                    # reset
                    self.fortress_sound = False
                    self.playPauseButton.on = False
                    self.current_wave = next_wave

                    # update dict for enemies graphs
                    spawned = self.spawn_count
                    not_killed = self.not_kill_count
                    killed = spawned - not_killed
                    self.df_enemies = self.df_enemies.append({'waves': self.wave, 'spawned':spawned, 'killed':killed, "Zao Warrior":waves[self.wave-1][0], "Yan Warrior":waves[self.wave-1][1], "Qi Warrior":waves[self.wave-1][2], "Wei Catapult":waves[self.wave-1][3], "Wei Balista":waves[self.wave-1][4], "Han Warrior":waves[self.wave-1][5], "Chu Warrior":waves[self.wave-1][6], "Chu Elephant":waves[self.wave-1][7], "Chu Boat":waves[self.wave-1][8], "Yan Boat":waves[self.wave-1][9], "Qi Boat":waves[self.wave-1][10], "Zao Riboku":waves[self.wave-1][11]}, ignore_index=True)
                    self.spawn_count = 0
                    self.not_kill_count = 0

                # No wave left, go_win
                else:
                    time.sleep(0.7)
                    self.go_win = True
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(os.path.join("game_assets/sounds/", "ending.mp3"))
                    pygame.mixer.music.play(loops=0)
                    time.sleep(0.4)
                    print("You Win")

        # Generates enemies of current wave, if wave is still going on
        else:

            # check if wave has just one type of enemy
            nb_0 = self.current_wave.count(0)
            if nb_0 == len(self.current_wave) - 1:
                one_type = True
            else:
                one_type = False

            # loop throw current wave to spawn enemies on by one
            for x in range(len(self.current_wave)):
                enemy_nb = self.current_wave[x]
                enemy_type = wave_compo[x][0]
                kingdom = wave_compo[x][1]
                
                # change to next enemy spawn
                if enemy_nb == 0:
                    self.next_spawn = True
                self.current_spawn_rate = enemy_type.rate*self.coef_rate

                # spawn one enemy
                if enemy_nb != 0:
                    enemy_type.scale_health(self.wave)
                    enemy_type.shield = self.shield
                    self.enemys.append(enemy_type)
                    self.current_kingdom = kingdom
                    self.current_wave[x] = self.current_wave[x] - 1
                    self.list_enemy_spawned[x] += 1
                    self.spawn_count += 1
                    self.next_spawn = False
                    # if wave has just one type of enemy, break for better spawn rates
                    if one_type:
                        break

    def run(self):

        # start playing the background music
        pygame.mixer.music.load(os.path.join("game_assets/sounds/", "loop0.wav"))
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(loops=-1) # loop forever
        wave_compo = [(Zao_warrior(),Zao_base()), (Yan_warrior(),Yan_base()), (Qi_warrior(),Qi_base()), (Wei_catapult(),Wei_base()), (Wei_balista(),Wei_base()), (Han_warrior(),Han_base()), (Chu_warrior(),Chu_base()), (Chu_elephant(),Chu2_base()), (Chu_boat(),Chu3_base()), (Yan_boat(),Yan_base()), (Qi_boat(),Qi_base()), (Zao_riboku(),Zao_base())]
        first_intro = [w_comp[0] for w_comp,w in zip(wave_compo, waves[0]) if w>0]
        self.fade(self.width, self.height, rgb(0,0,0), 0, 255, 10, first_intro) # (width, height, color, start=0, end=300, delay=1)
        
        # Before game initialisation :
        if self.wave == 0:
            self.initialise()

        # main run
        run = True
        clock = pygame.time.Clock()
        self.start_ticks = pygame.time.get_ticks() #starter tick

        while run:

            self.update_stat()
            clock.tick(400)

            # generates enemies at given rate if not pause
            if not self.playPauseButton.on_pause:
                if time.time() - self.timer >= self.current_spawn_rate:
                    self.timer = time.time()
                    self.gen_enemies()

            pos = pygame.mouse.get_pos()

            # check for moving object
            if self.moving_object:
                self.moving_object.move(pos[0], pos[1])
                tower_list = self.attack_towers[:] + self.support_towers[:] + self.fortress[:]
                collide = False
                for tower in tower_list:
                    if tower.collide(self.moving_object):
                        collide = True

            # main event loop
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.go_lose = True

                if event.type == SONG_END and self.change_sound and not self.go_win and self.wave != break_round - 1:
                    play_next_song()

                if event.type == pygame.MOUSEBUTTONUP:

                    # if you're moving an object and click it
                    if self.moving_object:
                        if self.moving_object.name in fortress_names:
                            tower_list = self.fortress[:]
                        else:
                            tower_list = self.attack_towers[:] + self.support_towers[:]
                        
                        not_allowed = False
                        # check if first tower of the game collides with forbidden tile
                        if not tower_list:
                            if self.moving_object.collide(self.moving_object):
                                not_allowed = True 
                                play_sound(1,"buzz.wav",600)
                        # check if moving object collides with towers, fortress or forbidden tile
                        for tower in tower_list:
                            if tower.collide(self.moving_object):
                                not_allowed = True
                                play_sound(1,"buzz.wav",600)
                        # add moving object if no collision with towers, fortress or forbidden tile
                        if not not_allowed:
                            self.add_obj(self.moving_object)
                            self.update_counter(self.moving_object, 1)
                            self.moving_object.moving = False
                            self.moving_object = None
                            play_sound(1,"put_tower.wav",600)

                    # if you click another object (not moving obj)
                    else:

                        # toggle play/pause
                        if self.playPauseButton.click(pos[0], pos[1]):
                            play_sound(1,"beep_menu.wav",300)
                            self.playPauseButton.toggle(opposite=True)

                        # toggle music
                        if self.soundButton.click(pos[0], pos[1]):
                            self.soundButton.toggle()
                            if self.soundButton.on:
                                pygame.mixer.music.unpause()
                            else:
                                pygame.mixer.music.pause()

                        # toggle side menu
                        if self.sideButton.click(pos[0], pos[1]):
                            play_sound(1,"toggle.wav", 600)
                            self.sideButton.toggle()
                            self.sideButton.play = pygame.transform.flip(self.sideButton.play, True, False)

                        # if you click on side menu and buttons
                        if self.sideButton.on:
                            side_menu_button = self.menu.get_clicked(pos[0], pos[1])
                            if side_menu_button:
                                self.menu.blink = True
                                cost = self.menu.get_item_cost(side_menu_button)
                                if self.money >= cost:
                                    play_sound(1,"buy.wav",600)
                                    self.spend(cost)
                                    self.add_tower(side_menu_button)
                                else:
                                    self.shake_money = True
                                    play_sound(1,"buzz.wav",600)

                        # if you click on speed-up, speed-down
                        if self.speedButton.click(pos[0], pos[1]):
                            play_sound(1,"beep_menu.wav", 300)
                            if self.speed < 3:
                                self.speed += 1
                            else:
                                self.speed = 1
                            self.speedButton.speed = self.speed

                        btn_clicked = None
                        # if you click on attack tower or support tower
                        if self.selected_tower:
                            btn_clicked = self.selected_tower.menu.get_clicked(pos[0], pos[1])
                            
                            # if you click on Upgrade button or Sell button
                            if btn_clicked:
                                # if you click on Upgrade button
                                if btn_clicked == "Upgrade":
                                    cost = self.selected_tower.get_upgrade_cost()
                                    if self.money >= cost:
                                        self.spend(cost)
                                        self.selected_tower.upgrade()
                                        play_sound(1,"buy.wav",600)
                                    else:
                                        self.shake_money = True
                                        play_sound(1,"buzz.wav",600)

                                # if you click on Sell button
                                if btn_clicked == "Sell":
                                    refund = self.selected_tower.sell()
                                    self.gain(refund)
                                    self.update_counter(self.selected_tower, -1)
                                    play_sound(1,"sell.wav",200)
                                    try:
                                        self.del_obj(self.selected_tower)
                                    except Exception as e:
                                        print("Sell Exception: " + str(e)) 

                        if not btn_clicked:

                            # check if you click on tower, fortress or kingdom, and select it
                            obj_list = [self.attack_towers, self.support_towers, self.fortress, self.kingdom]
                            for elem in obj_list:
                                self.check_click(pos, elem)

                            # if you click on reward
                            if self.draw_drop:
                                if self.click(gold_bag, self.drop_x, self.drop_y, pos[0], pos[1]):
                                    play_sound(0,"coin.wav",200)
                                    self.gain(self.reward)
                                    self.draw_drop = False

                        # self.clicks.append(pos)
                        # print(self.clicks)

            # do atoher actions: enemies(move), fortress(resist/collapse), towers(effect), lose lives
            if not self.playPauseButton.on_pause:
                to_del = []

                # loop through enemies
                for en in self.enemys:

                    # move enemies along the path, displayed at chosen game speed
                    en.speed = self.speed
                    en.move()
                    if en.x < 46:
                        to_del.append(en)
                        play_sound(1,"beep.wav",600)

                    # block enemies next to a fortress
                    for ft in self.fortress:
                        
                        # fortress loses health
                        if en.collide(ft):
                            self.fortress_sound = True
                            ft.collided.append(en)
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
                    self.lose_life(d)

                # loop through attack towers 
                for tw in self.attack_towers:
                    # attack, at chosen game speed
                    tw.speed = self.speed
                    money_before = self.money 
                    self.money += tw.attack(self.enemys)
                    value = self.money - money_before
                    self.money_earnt += value
                    en = tw.attacked_enemy
                    if en is not None:
                        expl = Explosion(en.x, en.y, 'sm')
                        all_sprites.add(expl)
                        self.update_counter_gold(en, value)

                    # check if you got a random gold_drop
                    if tw.gold_drop > 0:
                        self.dropped(tw)

                # loop through support towers and do effect
                for tw in self.support_towers:
                    tw.support(self.attack_towers)

                # loop through fortress, remove it if collapsed and move again enemies 
                for ft in self.fortress:
                    if ft.collapse:
                        self.fortress_sound = False
                        self.fortress.remove(ft)
                        for en in self.to_resist:
                            en.block = False
                for ft in self.fortress_sold:
                    for en in self.to_resist:
                        if en in ft.collided:
                            en.block = False
                    self.fortress_sold.remove(ft)

                # play fortress sound if fortress is still activated
                if self.fortress_sound:
                    if random.randint(0,60) == 10:
                        play_sound(1,"melee.wav",1600)

                # if you lose, go_lose
                if self.lives <= 0:
                    self.game_over()

                # stop run if game is over (win or lose)
                if self.go_win or self.go_lose:
                    
                    # load Plot-1 and Plot-2 windows
                    self.df = pd.DataFrame(data = self.data_dict)
                    self.df_gold = pd.DataFrame(data = self.counter_gold)
                    self.df_gold = self.df_gold.groupby(by=["Enemies (Type)"]).sum()
                    self.df_gold['Enemies (Type)'] = self.df_gold.index
                    self.fade(self.width, self.height, rgb(0,0,0), 0, 300, 4) # (width, height, color, start=0, end=300, delay=1)
                    try:
                        self.plot_towers(self.df)
                        self.plot_enemies(self.df_enemies, self.list_enemy_spawned, self.not_killed, self.df_gold)
                        plt.show()
                    except Exception as e:
                        print("Graph Exception: " + str(e))
                    
                    # game has finished
                    run = False

            # actualise pictures
            all_sprites.update()
            self.draw()

            # re init
            self.shake_money = False
            self.shake_life = False
            self.menu.blink = False


    def draw(self):
        self.win.blit(self.bg, (0, 0))

        # for p in self.clicks:
        # 	pygame.draw.circle(self.win, rgb(255, 0, 0), (p[0], p[1]), 5, 0)

        # draw kingdom's base
        for kingdoms in self.kingdom:
            kingdoms.draw(self.win)

        # draw random gold_drop
        if self.draw_drop:
            self.win.blit(gold_bag, (self.drop_x, self.drop_y))

        # draw towers and fortress, sorted by y position for no overlaying
        towers = self.attack_towers[:] + self.support_towers[:] + self.fortress[:]
        self.draw_towers(towers)

        # draw enemies
        for en in self.enemys:
            en.draw(self.win)

        # draw menu
        if self.sideButton.on:
            self.menu.draw(self.win)

        # draw side button
        if self.sideButton.on:
            self.sideButton.x = self.width - 116
            self.sideButton.y = 272
        else:
            self.sideButton.x = self.width - 33
            self.sideButton.y = 272
        self.sideButton.draw(self.win)

        # draw speed-up, speed-down button
        self.speedButton.draw(self.win)

        # draw play pause button
        self.playPauseButton.draw(self.win)

        # draw music toggle button
        self.soundButton.draw(self.win)

        # draw wave
        self.win.blit(wave_bg, (self.width - 90, self.height - 48))
        text = self.wave_font.render("Wave " + str(self.wave + 1), 2, rgb(255,255,255))
        self.win.blit(text, (self.width - 90 + wave_bg.get_width()/2 - text.get_width()/2, self.height - 47))

        # draw alert
        self.draw_alert(self.current_kingdom)
        
        # draw lives
        start_x = 10
        start_y = 0
        text = self.life_font.render(str(self.lives), 2, rgb(255, 255, 255))
        add_shake = 0
        if self.shake_life:
            add_shake = 18
        add_x = text.get_width() + 10
        add_y = 3
        self.win.blit(text, (start_x + add_shake, start_y))
        self.win.blit(lives_img, (start_x + add_x + add_shake, start_y + add_y))

        # draw money
        text = self.money_font.render(str(self.money), 2, rgb(255, 255, 255))
        add_shake = 0
        if self.shake_money:
            add_shake = 18
        start_x = self.width - money_img.get_width() - text.get_width() - 15
        start_y = 0
        add_x = 0 + add_shake
        self.win.blit(text, (start_x + add_x, start_y))
        add_x = text.get_width() + 10 + add_shake
        self.win.blit(money_img, (start_x + add_x, start_y))

        # draw moving object
        if self.moving_object:
            self.moving_object.draw(self.win)

        all_sprites.draw(self.win)

        pygame.display.update()


    def draw_alert(self, kingdom):
        """
        display blinking alert next to the kingdom when enemies spawn
        :param kingdom: Kingdom
        :return: None
        """
        x = kingdom.x - 72
        y = kingdom.y - 28
        timer = time.time() - self.timer
        rate = self.current_spawn_rate
        if not self.next_spawn:
            # randomly flashing
            if timer >= random.randrange(0, 1 + math.ceil(rate))/rate:
                self.win.blit(alert_red, (x, y))
            else:
                self.win.blit(alert_white, (x, y))


    def draw_towers(self, tower_list):
        """
        display towers and fortress, without overlaying
        :param tower_list: [attack_towers, support_towers, fortress] list of list of towers
        :return: None
        """
        tower_list.sort(key=lambda tw: tw.y)
        for tw in tower_list:
            tw.draw(self.win)


    def click (self, img, x, y, X, Y):
        """
        returns if img has been clicked on
        :param x, y, X, Y : int
        :return: bool
        """
        if X <= x + img.get_width() and X >= x:
            if Y <= y + img.get_height() and Y >= y:
                return True
        return False

    def add_tower(self, name):
        """
        add tower if clicked on its button
        """
        x, y = pygame.mouse.get_pos()
        name_list = ["buy_shin", "buy_moubu", "buy_kanki", "buy_ouhon", "buy_fortress", "buy_kyoukai", "buy_ten", "buy_ryo"]
        object_list = [ShinTower(x,y), MoubuTower(x, y), KankiTower(x, y), OuhonTower(x, y), Fortress(x, y), KyoukaiTower(x, y), TenTower(x, y), RyoTower(x, y)]
        try:
            obj = object_list[name_list.index(name)]
            self.moving_object = obj
            obj.moving = True
        except Exception as e:
            print(str(e) + "NOT VALID NAME")

    def add_obj(self, obj):
        """
        add tower or fortress to its corresponding list
        """
        if obj.name in attack_tower_names:
            self.attack_towers.append(obj)
        elif obj.name in support_tower_names:
            self.support_towers.append(obj)
        elif obj.name in fortress_names:
            self.fortress.append(obj)
            self.first_contact = True
        exp = Explosion(obj.x, obj.y, "tower")
        all_sprites.add(exp)

    def del_obj(self, obj):
        """
        removes tower or fortress
        """
        if obj.name in attack_tower_names:
            self.attack_towers.remove(obj)
        elif obj.name in support_tower_names:
            self.support_towers.remove(obj)
        elif obj.name in fortress_names:
            self.fortress_sound = False
            self.fortress_sold.append(obj)
            self.fortress.remove(obj)

    def check_click(self, pos, elem):
        """
        select obj if clicked
        """
        for obj in elem:
            if obj.click(pos[0], pos[1]):
                obj.selected = True
                if elem != self.kingdom:
                    self.selected_tower = obj
            else:
                obj.selected = False

    def update_counter(self, obj, sign):
        """
        update dict for graphs
        """
        self.counters[obj.name] = self.counters[obj.name] + sign

    def update_counter_gold(self, obj, value):
        """
        update dict for enemy graphs
        """
        self.counter_gold["Gold Earnt"].append(value)
        self.counter_gold["Enemies (Type)"].append(obj.nickname)

    def spend(self, cost):
        """
        update money
        """
        self.money -= cost
        self.money_spent += cost

    def gain(self, cost):
        """
        update money
        """
        self.money += cost
        self.money_earnt += cost

    def lose_life(self, enemy):
        """
        update enemy counters, lose 1 live, do animation
        """
        self.not_killed[enemy.name] +=1
        self.not_kill_count += 1
        self.lives -= 1
        self.shake_life = True
        expl = Explosion(enemy.x, enemy.y, 'lg')
        all_sprites.add(expl)
        self.enemys.remove(enemy)

    def dropped(self, tower):
        """
        gives reward and drop coordinates
        """
        self.reward = tower.gold_drop
        self.drop_x = tower.coord[0] - gold_bag.get_width() / 2
        self.drop_y = tower.coord[1] - gold_bag.get_height() / 2 - 35
        self.draw_drop = True

    def getUniqueEnemies(self, l):
        """
        create a list of unique enemies based on their type
        """
        result = []
        temp = []
        for item in l:
            if item.type not in temp:
                result.append(item)
                temp.append(item.type)
        return result

    def flipDict(self, d):
        """
        flip keys and values
        """
        result = {}
        for key, value in d.items(): 
            if value not in result: 
                result[value] = [key] 
            else: 
                result[value].append(key)
        return result

    def game_over(self):
        """
        transition to end game
        """
        play_sound(1,"beep.wav",600)
        self.shake_life = False
        self.draw()
        time.sleep(0.7)
        pygame.mixer.music.pause()
        play_sound(0,"game_over.wav")
        time.sleep(2.4)
        print("You Lose")
        self.go_lose = True
        pygame.mixer.music.load(os.path.join("game_assets/sounds/", "melody.wav"))
        pygame.mixer.music.play(loops=-1)


    def fade(self, width, height, color, start=0, end=300, delay=1, en_intro=[]):
        """
        transition to next scene
        """ 

        fade = pygame.Surface((width, height))
        fade.fill(color)

        if self.wave == break_round - 1:
            delay = round(delay*1.5)

        for alpha in range(start, end):
            fade.set_alpha(alpha)

            # draw wave number
            wave_text = self.drawWaveNumber(fade, self.wave_font2)

            # draw enemies intro images and texts under the wave text:
            self.drawEnemiesIntro(wave_text, en_intro)

            pygame.display.update()
            pygame.time.delay(delay)

        # longer transition for the upcoming special wave
        if self.wave == break_round - 1:
            pygame.time.delay(5000)

    def drawWaveNumber(self, srfc, font):
        """
        draw wave texts based on game status (run, go_win, go_lose) and return the text
        """

        self.win.blit(srfc, (0,0))
        if self.go_win: 
            text = font.render("Win", 2, rgb(255,255,255))
        elif self.go_lose:
            text = font.render("Game Over", 2, rgb(255,255,255))
        else:
            text = font.render("Wave " + str(self.wave + 1), 2, rgb(255,255,255))
        self.win.blit(text, (self.width/2 - text.get_width()/2, self.height/2 - text.get_height()/2))
        return text

    def drawEnemiesIntro(self, text, l):
        """
        draw images next to each others, and texts under the images
        """

        # create flipped dict with enemies type as keys, enemies nickname as values, and list
        key = [en.nickname for en in l]
        value = [en.type for en in l]
        ini_dict = dict(zip(key, value))
        flipped = self.flipDict(ini_dict)
        en_txt = [[key,value] for key, value in flipped.items()]

        # create a list of unique enemy types 
        en_obj = self.getUniqueEnemies(l)

        # draw loop : draw images next to each others, and texts under images
        type_nb = len(en_obj)
        img_width = 120 # en.intro.get_width()
        img_height = 120 
        pad = 10
        x = self.width/2 -((type_nb/2)*img_width +(type_nb-1)*pad)
        y = self.height/2 + text.get_height()/2
        for en, txt in zip(en_obj, en_txt):
            # draw images
            self.win.blit(en.intro, (x,y))
            # draw texts
            for i, t in enumerate(txt[1]):
                text_en = self.wave_font.render(t, 2, rgb(255,255,255))
                self.win.blit(text_en, (x+img_width/2-text_en.get_width()/2, y+img_height+pad+i*text_en.get_height()))
            x += img_width + 2*pad


    def initialise(self):
        """
        Initialise based on diffculty
        """

        # add additional money based on game level (+10, +20, +30)
        coef = 3 - self.lvl[self.level]
        self.money = self.money + self.money*coef

        # reduce spaw rates based on game level (-0%, -20%, -40%) TO DO
        coef = 1 - 0.2*self.lvl[self.level]
        self.coef_rate = coef

        # balance enemies strengh based on game level
        coef = self.lvl[self.level]/5
        self.shield = 2 + coef

    def update_stat(self):
        """
        update dict every 2 seconds for end game statistics
        """

        # seconds ticking
        self.seconds = (pygame.time.get_ticks()-self.start_ticks)/1000

        # calculate total towers number
        towers_nb = sum(self.counters.values())
        
        # store data every 2 seconds (+- 0.01)
        list_keys = list(self.data_dict.keys())
        list_items = [round(self.seconds), self.wave + 1 , self.money, self.lives, self.money_earnt,  self.money_spent,self.counters['shin'],  self.counters['moubu'],  self.counters['kanki'],  self.counters['ouhon'],  self.counters['ten'],  self.counters['kyoukai'], self.counters['ryo'],  self.counters['fortress'], towers_nb] 
        rest = math.fmod(self.seconds, 2)
        if rest <= 0.01:
            for key, item in zip(list_keys, list_items):
                self.data_dict[key].append(item)


    def plot_towers(self, df):
        """
        plot end game statistics : 4 graphs (money, attack towers, lives, support towers)
        """

        # Plot-1 configuration
        fig, axes = plt.subplots(2, 2, figsize=(14, 14))
        sns.set(style="whitegrid")

        # axe (0,0) : Seaborn lineplot
        data_preproc = pd.DataFrame({'Waves (Nb)': df['waves'].values, 'Money Spent': df['money_spent'].values,'Money Earnt': df['money_earnt'].values,'Money': df['money'].values})
        data = pd.melt(data_preproc, ['Waves (Nb)'])
        data = data.rename(columns={"value": "Money ($)"})
        sns.lineplot(x='Waves (Nb)', y='Money ($)', hue='variable', data=data, ci=None, markers=True, style = 'variable', palette=['#E33B24', '#2EB4F6', '#797979'], ax=axes[0,0])
        axes[0,0].legend(loc='upper left')

        # axe (0,1) : Matplotlib stackplot
        x = df['waves'].values
        y = [df['shin'].values, df['moubu'].values, df['kanki'].values, df['ouhon'].values]
        label = ["Shin", "Moubu", "Kanki", "Ouhon"]
        color = ['#2EB4F6', '#F2801B', '#6412CA', '#AAAAAA']
        axes[0,1].stackplot(x, y, labels=label, baseline ='zero', colors=color)
        axes[0,1].legend(loc='upper left')
        axes[0,1].set_xlabel('Waves (Nb)')
        axes[0,1].set_ylabel('Attack Towers (Nb)')

        # axe (1,0) : Seaborn lineplot
        color = '#E33B24'
        data = pd.DataFrame({'Waves (Nb)': df['waves'].values, 'Lives (Nb)': df['lives'].values})
        sns.lineplot(x='Waves (Nb)', y='Lives (Nb)', data=data, ci=None, markers=True, color=color, ax=axes[1,0])
        
        # axe (1,1) : Matplotlib stackplot
        x = df['waves'].values
        y = [df['kyoukai'].values, df['ten'].values, df['ryo'].values, df['fortress'].values]
        label = ["Kyoukai", "Ten", "Ryo", "Fortress"]
        color = ['#E33B24', '#2EB4F6', '#EECE1A', '#AAAAAA']
        axes[1,1].stackplot(x, y, labels=label, baseline ='zero', colors=color)
        axes[1,1].legend(loc='upper left')
        axes[1,1].set_xlabel('Waves (Nb)')
        axes[1,1].set_ylabel('Support Towers (Nb)')
            
    def plot_enemies(self, df, spawned, alive, df_gold): 
        """
        plot end game statistics : 4 graphs (enemies killes, not killed, money earnt)
        """ 

        # Plot-2 configuration
        fig, axes = plt.subplots(2, 2, figsize=(14, 14))
        sns.set(style="whitegrid")

        # data
        not_killed  = [x[1] for x in alive.items()]
        killed = [x-y for (x,y) in zip(spawned, not_killed)]
        waves = df['waves'].values
        spawned_count = df['spawned'].values
        kill_count = df['killed'].values

        # colors
        color_red = '#E33B24'
        color_blue = '#2EB4F6'
        color_green = '#6EF95F'

        # axe (0,0) : Seaborn barplot
        x_red = spawned
        x_blue = killed
        y = enemy_nickname
        data_red = pd.DataFrame({'Enemies': y, 'Number': x_red})
        data_blue = pd.DataFrame({'Enemies': y, 'Number': x_blue})
        sns.barplot(x='Number', y='Enemies', data=data_red, ci=None, color=color_red, orient = 'h', ax=axes[0,0])
        sns.barplot(x='Number', y='Enemies', data=data_blue, ci=None, color=color_blue, orient = 'h', ax=axes[0,0])
        axes[0,0].legend(loc='lower right', labels=['Not Killed', 'Killed'])
        axes[0,0].set_xlabel('Enemies (Nb)')
        axes[0,0].set_ylabel('Enemies (Type)')

        # axe (0,1) : Seaborn barplot
        df2 = df.drop(['spawned', 'killed'], axis=1)
        df2 = df2.sort_values('waves', ascending=False)
        df2.set_index('waves').plot(kind='barh', stacked=True, ax=axes[0,1])
        axes[0,1].set_xlabel('Enemies (Nb)')
        axes[0,1].set_ylabel('Waves (Nb)')

        # axe (1,0) : Seaborn barplot
        x_red = spawned_count
        x_blue = kill_count
        y = waves
        data_red = pd.DataFrame({'Waves': y, 'Number': x_red})
        data_blue = pd.DataFrame({'Waves': y, 'Number': x_blue})
        sns.barplot(x='Number', y='Waves', data=data_red, ci=None, color=color_red, orient = 'h', ax=axes[1,0])
        sns.barplot(x='Number', y='Waves', data=data_blue, ci=None, color=color_green, orient = 'h', ax=axes[1,0])
        axes[1,0].legend(loc='upper right', labels=['Not Killed', 'Killed'])
        axes[1,0].set_xlabel('Enemies (Nb)')
        axes[1,0].set_ylabel('Waves (Nb)')

        # axe (1,1) : Seaborn barplot
        sns.barplot(x='Gold Earnt', y='Enemies (Type)', data=df_gold, ci=None, orient = 'h', ax=axes[1,1])
        axes[1,1].legend(loc='lower right')

def play_sound(*args):
    """
    call pygame.mixer fonction with sounds in "game_assets/sounds/"
    """ 

    if len(args) == 3:
        a,b,c = args[0],args[1],args[2]
        pygame.mixer.Channel(a).play(pygame.mixer.Sound(os.path.join("game_assets/sounds/", b)), maxtime=c)
    elif len(args) == 2:
        a,b = args[0],args[1]
        pygame.mixer.Channel(a).play(pygame.mixer.Sound(os.path.join("game_assets/sounds/", b)))


_songs = deque([os.path.join("game_assets/sounds/", "13_Tazer.mp3"), os.path.join("game_assets/sounds/", "08_T_Station.mp3"), os.path.join("game_assets/sounds/", "04_Shamburger.mp3")])
def play_next_song():
    """
    change sound when previous sound is finished
    """ 
    global _songs
    _songs.rotate(-1) # move current song to the back of the list (equal to: _songs = _songs[1:] + [_songs[0]])
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()

def getUniqueItems(d):
    result = {}
    for key,value in d.items():
        if value not in result.values():
            result[key] = value
    return result

