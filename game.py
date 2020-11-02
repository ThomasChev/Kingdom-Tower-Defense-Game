import pygame # pygame-1.9.6-cp38-cp38-win_amd64.whl
import os
import math
import time
import random
import pandas as pd

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
from towers.quinTower import ShinTower, MoubuTower, KankiTower, OuhonTower
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
from graphs.graphs import Graph
from game_assets.colors import rgb

pygame.font.init()
pygame.init()


lives_img = pygame.image.load(os.path.join("game_assets/menu/","heart.png"))
money_img = pygame.image.load(os.path.join("game_assets/menu/","star.png"))
side_img = pygame.image.load(os.path.join("game_assets/menu/","side.png"))
side_btn = pygame.image.load(os.path.join("game_assets/menu/","side_btn.png"))

buy_shin = pygame.image.load(os.path.join("game_assets/quin_towers/shin_icon","buy_shin.png"))
buy_moubu = pygame.image.load(os.path.join("game_assets/quin_towers/moubu_icon","buy_moubu.png"))
buy_kanki = pygame.image.load(os.path.join("game_assets/quin_towers/kanki_icon","buy_kanki.png"))
buy_ouhon = pygame.image.load(os.path.join("game_assets/quin_towers/ouhon_icon","buy_ouhon.png"))
buy_kyoukai = pygame.image.load(os.path.join("game_assets/support_towers/kyoukai_icon","buy_kyoukai.png"))
buy_ten = pygame.image.load(os.path.join("game_assets/support_towers/ten_icon","buy_ten.png"))
buy_fortress = pygame.image.load(os.path.join("game_assets/fortress/fortress_icon","buy_fortress.png"))

play_btn = pygame.image.load(os.path.join("game_assets/menu/","play_btn.png"))
pause_btn = pygame.image.load(os.path.join("game_assets/menu/","pause_btn.png"))
sound_btn = pygame.image.load(os.path.join("game_assets/menu/","music_btn.png"))
sound_btn_off= pygame.image.load(os.path.join("game_assets/menu/","music_off_btn.png"))
gold_bag = pygame.image.load(os.path.join("game_assets/menu/", "gold_bag.png"))

wave_bg = pygame.image.load(os.path.join("game_assets/menu/","wave_sign.png"))
alert_red = pygame.image.load(os.path.join("game_assets/menu/","alert_red.png")) # red alert
alert_white = pygame.image.load(os.path.join("game_assets/menu/","alert_white.png")) # white alert

attack_tower_names = ["shin", "moubu", "kanki", "ouhon"]
support_tower_names = ["ten", "kyoukai"]
fortress_names = ["fortress"]

# initialize background music
pygame.mixer.pre_init()
pygame.mixer.init()
pygame.mixer.music.load(os.path.join("game_assets/sounds/", "loop0.wav"))
pygame.mixer.music.set_volume(0.4)

# frequency of enemies [Zao_w, Yan_w, Qi_w, Wei_c, Wei_b, Han_w, Chu_w, Chu_e, Chu_b, Yan_b, Qi_b, Zao_r]
waves = [[3,0,0,3,3,3,0,0,0,0,0,0],[3,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0,0,0],[0,3,0,0,0,0,0,0,0,0,0,0],[0,0,2,0,0,0,0,0,0,0,0,0],[0,0,4,0,0,0,0,0,0,0,0,0],[0,0,0,2,0,0,0,0,0,0,0,0],[0,0,0,4,0,0,0,0,0,0,0,0],[0,0,0,0,4,0,0,0,0,0,0,0],[0,0,0,0,6,0,0,0,0,0,0,0],[0,0,0,0,0,4,0,0,0,0,0,0],[0,0,0,0,0,6,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0,0,0],[0,0,0,0,0,0,6,0,0,0,0,0],[0,0,0,0,0,0,0,2,0,0,0,0],[0,0,0,0,0,0,0,6,0,0,0,0],[0,0,0,0,0,0,0,0,2,0,0,0],[0,0,0,0,0,0,0,0,6,0,0,0],[0,0,0,0,0,0,0,0,0,2,0,0],[0,0,0,0,0,0,0,0,0,10,0,0],[0,0,0,0,0,0,0,0,0,0,2,0],[0,0,0,0,0,0,0,0,0,0,8,0],[9,0,0,0,0,0,0,0,0,0,0,0],[0,7,0,0,0,0,0,0,0,3,0,0],[0,0,9,0,0,0,0,0,0,0,4,0],[0,0,0,5,5,0,0,0,0,0,0,0],[0,0,0,0,0,14,0,0,0,0,0,0],[0,0,0,0,0,0,4,4,4,0,0,0],[5,5,5,0,0,0,0,0,0,0,0,0],[0,18,0,0,0,0,0,0,0,0,0,0],[3,3,3,0,0,3,6,0,0,0,0,0],[3,6,3,0,0,3,6,0,0,0,0,0],[0,0,0,0,0,10,8,0,0,0,0,0],[0,0,0,0,0,0,0,0,16,0,0,0],[0,0,0,0,0,0,0,0,0,18,0,0],[0,0,0,0,0,0,0,0,0,0,20,0],[0,0,0,0,0,0,0,0,12,6,6,0],[11,11,11,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,16,18,0,0,0,0,0],[8,8,10,0,0,10,8,0,0,0,0,0],[9,9,9,0,0,9,9,0,0,0,0,0],[0,35,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,35,0,0,0],[0,0,0,0,0,0,0,0,0,35,0,0],[0,0,0,0,0,0,0,0,0,0,33,0],[0,0,0,0,0,0,0,0,12,12,15,0],[35,0,0,0,0,0,0,0,0,0,0,0],[0,29,0,0,0,0,0,0,0,0,0,0],[0,0,12,10,12,0,0,4,0,0,0,0],[10,10,10,4,4,10,10,4,4,4,4,0],[10,10,10,6,6,10,10,4,4,4,4,0],[10,10,10,6,6,10,10,6,4,4,4,0],[10,10,10,6,6,10,10,6,6,6,6,0],[12,15,10,8,8,10,10,8,6,6,6,0],[12,20,10,8,8,10,10,10,6,6,6,1]]
waves = [[1,2,0,0,0,0,0,0,0,0,0,0], [1,1,1,0,0,0,0,0,0,0,0,0],[0,0,2,0,0,0,0,0,0,0,0,0], [2,0,0,0,0,0,0,0,0,0,0,0], [4,4,4,4,4,4,4,4,4,4,4,1], [0,0,0,0,0,0,0,0,0,0,0,0]]
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
        self.lives = 200
        self.money = 1000
        self.bg = pygame.image.load(os.path.join("game_assets/background/", "kingdom.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.clicks = [] # use to see clicks
        self.timer = time.time()
        self.life_font = self.money_font = pygame.font.Font("game_assets/fonts/SF Atarian System.ttf", 32)
        self.wave_font = pygame.font.Font("game_assets/fonts/SF Atarian System.ttf", 18)
        self.wave_font2 = pygame.font.Font("game_assets/fonts/SF Atarian System.ttf", 72)
        self.selected_tower = None
        self.menu = VerticalMenu(self.width - 62, 125, side_img)
        self.menu.add_btn(buy_shin, "buy_shin", 20)
        self.menu.add_btn(buy_moubu, "buy_moubu", 60)
        self.menu.add_btn(buy_kanki, "buy_kanki", 40)
        self.menu.add_btn(buy_ouhon, "buy_ouhon", 150)
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
        self.shake_money = False
        self.shake_life = False
        self.spawn_rate = spawn_rates[:]
        self.current_spawn_rate = 1.5
        self.fortress_sound = False
        self.to_resist = []
        self.first_contact = True
        self.go_lose = False
        self.go_win = False
        self.kingdom = [Quin_base(),Zao_base(),Yan_base(),Qi_base(),Wei_base(),Han_base(),Chu_base(),Chu2_base(),Chu3_base()]
        self.current_kingdom = self.kingdom[0]
        self.next_spawn = False
        self.draw_drop = False
        self.drop_x = 0
        self.drop_y = 0
        self.reward = 0
        self.start_ticks = 0
        self.seconds = 0
        self.data_dict = {'seconds':[], 'waves':[], 'money':[], 'lives':[], 'money2':[]}
        self.df = pd.DataFrame()
        self.graphs = [Graph()]

    def gen_enemies(self):
        """
        generate the next enemy or enemies to show
        :return: enemy, kingdom
        """
        wave_compo = [(Zao_warrior(),Zao_base()), 
                        (Yan_warrior(),Yan_base()), 
                        (Qi_warrior(),Qi_base()), 
                        (Wei_catapult(),Wei_base()), 
                        (Wei_balista(),Wei_base()), 
                        (Han_warrior(),Han_base()), 
                        (Chu_warrior(),Chu_base()), 
                        (Chu_elephant(),Chu_base()), 
                        (Chu_boat(),Chu_base()), 
                        (Yan_boat(),Yan_base()), 
                        (Qi_boat(),Qi_base()), 
                        (Zao_riboku(),Zao_base())]
        # Wave has finished
        if sum(self.current_wave) == 0:
            self.next_spawn = True

            if len(self.enemys) == 0:
                self.wave += 1

                # Go to next wave
                if self.wave < len(waves):
                    # play sound, write wave number and shade
                    if self.wave > 0:
                        play_sound(0,"next_round.wav")
                        self.fade(self.width, self.height, rgb(0,0,0), 0, 50, 60)  # (width, height, color, start=0, end=300, delay=1)
                    # reset
                    self.fortress_sound = False
                    self.pause = False
                    self.playPauseButton.paused = self.pause
                    self.current_wave = waves[self.wave]
                    
                
                # No wave left, go_win
                else:
                    time.sleep(0.7)
                    self.go_win = True
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(os.path.join("game_assets/sounds/", "ending.mp3"))
                    pygame.mixer.music.play(loops=0)
                    time.sleep(0.4)
                    print("You Win")

        # Generates enemies of current wave 
        else:
            for x in range(len(self.current_wave)):
                enemy_nb = self.current_wave[x]
                enemy_type = wave_compo[x][0]
                kingdom = wave_compo[x][1]

                if enemy_nb == 0:
                    self.next_spawn = True
                self.current_spawn_rate = self.spawn_rate[x]
                if enemy_nb != 0:
                    self.enemys.append(enemy_type)
                    self.current_kingdom = kingdom
                    self.current_wave[x] = self.current_wave[x] - 1
                    self.next_spawn = False
                    break # comment to spawn the current_wave[x] enemies all together

    def run(self):

        # start playing the background music
        pygame.mixer.music.load(os.path.join("game_assets/sounds/", "loop0.wav"))
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(loops=-1) # loop forever
        self.fade(self.width, self.height, rgb(0,0,0), 0, 255, 10) # (width, height, color, start=0, end=300, delay=1)

        # main run
        run = True
        clock = pygame.time.Clock()
        self.start_ticks = pygame.time.get_ticks() #starter tick

        while run:

            self.update_stat()
            clock.tick(400)

            # generates enemies at given rate if not pause
            if not self.pause:
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
                    #run = False

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
                        # add it if doesnt collide with towers, fortress or forbidden tile
                        if not not_allowed:
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

                    # if you click another object (NOT moving)
                    else:

                        # toggle play/pause
                        if self.playPauseButton.click(pos[0], pos[1]):
                            play_sound(1,"beep_menu.wav",300)
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

                        # if you click on side menu and buttons
                        if self.menu_on:
                            side_menu_button = self.menu.get_clicked(pos[0], pos[1])
                            if side_menu_button:
                                self.menu.blink = True
                                cost = self.menu.get_item_cost(side_menu_button)
                                if self.money >= cost:
                                    play_sound(1,"buy.wav",600)
                                    self.money -= cost
                                    self.add_tower(side_menu_button)
                                else:
                                    self.shake_money = True
                                    play_sound(1,"buzz.wav",600)

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
                                        self.money -= cost
                                        self.selected_tower.upgrade()
                                        play_sound(1,"buy.wav",600)
                                    else:
                                        self.shake_money = True
                                        play_sound(1,"buzz.wav",600)

                                # if you click on Sell button
                                if btn_clicked == "Sell":
                                    refund = self.selected_tower.sell()
                                    self.money += refund
                                    play_sound(1,"sell.wav",200)
                                    if self.selected_tower.name in attack_tower_names:
                                        self.attack_towers.remove(self.selected_tower)
                                    elif self.selected_tower.name in support_tower_names:
                                        self.support_towers.remove(self.selected_tower)
                                    elif self.selected_tower.name in fortress_names:
                                        self.fortress.remove(self.selected_tower)

                        if not btn_clicked:
                            # if you click on attack tower
                            for tw in self.attack_towers:
                                if tw.click(pos[0], pos[1]):
                                    tw.selected = True
                                    self.selected_tower = tw
                                else:
                                    tw.selected = False

                            # if you click on support tower
                            for tw in self.support_towers:
                                if tw.click(pos[0], pos[1]):
                                    tw.selected = True
                                    self.selected_tower = tw
                                else:
                                    tw.selected = False

                            # if you click on fortress
                            for ft in self.fortress:
                                if ft.click(pos[0], pos[1]):
                                    ft.selected = True
                                    self.selected_tower = ft
                                else:
                                    ft.selected = False

                            # if you clicked on kingdom's base
                            for base in self.kingdom:
                                if base.click(pos[0], pos[1]):
                                    base.selected = True
                                    # self.selected_tower = ft
                                else:
                                    base.selected = False

                            # if you click on reward
                            if self.draw_drop:
                                if self.click(gold_bag, self.drop_x, self.drop_y, pos[0], pos[1]):
                                    play_sound(0,"coin.wav",200)
                                    self.money += self.reward
                                    self.draw_drop = False

                        # self.clicks.append(pos)
                        # print(self.clicks)

            # do atoher actions: enemies(move), fortress(resist/collapse), towers(effect), lose lives
            if not self.pause:
                to_del = []

                # loop through enemies
                for en in self.enemys:
                    
                    # move enemies along the path
                    en.move()
                    if en.x < 46:
                        to_del.append(en)
                        play_sound(1,"beep.wav",600)

                    # block enemies next to a fortress
                    for ft in self.fortress:
                        
                        # fortress loses health
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
                    self.shake_life = True
                    self.enemys.remove(d)

                # loop through attack towers 
                for tw in self.attack_towers:

                        # attack
                        self.money += tw.attack(self.enemys)

                        # check if you got a random gold_drop
                        if tw.gold_drop > 0:
                            self.reward = tw.gold_drop
                            self.drop_x = tw.coord[0] - gold_bag.get_width() / 2
                            self.drop_y = tw.coord[1] - gold_bag.get_height() / 2 - 35
                            self.draw_drop = True

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
                
                # play fortress sound if activated
                if self.fortress_sound:
                    if random.randint(0,60) == 10:
                        play_sound(1,"melee.wav",1600)

                # if you lose, go_lose
                if self.lives <= 0:
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

                # stop run if game is over (win or lose)
                if self.go_win or self.go_lose:
                    self.df = pd.DataFrame(data = self.data_dict)
                    self.fade(self.width, self.height, rgb(0,0,0), 0, 300, 4) # (width, height, color, start=0, end=300, delay=1)
                    print(self.df)

                    # graph = self.graphs[0]
                    graph = Graph()
                    graph.name = os.path.join("graphs/fig/","plot_money.png")

                    # line = [x, y, label, title, xlabel, ylabel]
                    graph.lines['money'] = [self.df['seconds'], self.df['money'], 'money', 'Money = f(t)', 'Time (s)' , 'Money ($)']
                    graph.lines['money/2'] = [self.df['seconds'], self.df['money2'], 'money/2', 'Money = f(t)', 'Time (s)', 'Money ($)']
                    graph.lines['lives'] = [self.df['seconds'], self.df['lives'], 'lives', 'Lives = f(t)', 'Time (s)', 'Lives (nb)']

                    # ax = [line1, line2...]
                    graph.ax_dict['ax1'] = [graph.lines['money'], graph.lines['money/2']]
                    graph.ax_dict['ax2'] = [graph.lines['lives']]

                    graph.lines['money_2'] = [self.df['waves'], self.df['money'], 'money', 'Money = f(wave)', 'Wave' , 'Money ($)']
                    graph.lines['money/2_2'] = [self.df['waves'], self.df['money2'], 'money/2', 'Money = f(wave)', 'Wave', 'Money ($)']
                    graph.lines['lives_2'] = [self.df['waves'], self.df['lives'], 'lives', 'Lives = f(t)', 'Wave', 'Lives (nb)']

                    graph.ax_dict['ax3'] = [graph.lines['money_2'], graph.lines['money/2_2']]
                    graph.ax_dict['ax4'] = [graph.lines['lives_2']]

                    graph.plot()
                    
                    run = False

            self.draw()
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
        if self.menu_on:
            self.menu.draw(self.win)

        # draw side button
        if self.menu_on:
            self.sideButton.x = self.width - 133
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
        text = self.wave_font.render("Wave " + str(self.wave + 1), 2, rgb(255,255,255))
        self.win.blit(text, (self.width - 100 + wave_bg.get_width()/2 - text.get_width()/2, self.height - 47))

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

        pygame.display.update()


    def add_tower(self, name):
        x, y = pygame.mouse.get_pos()
        name_list = ["buy_shin", "buy_moubu", "buy_kanki", "buy_ouhon", "buy_fortress", "buy_kyoukai", "buy_ten"]
        object_list = [ShinTower(x,y), MoubuTower(x, y), KankiTower(x, y), OuhonTower(x, y), Fortress(x, y), KyoukaiTower(x, y), TenTower(x, y)]

        try:
            obj = object_list[name_list.index(name)]
            self.moving_object = obj
            obj.moving = True
        except Exception as e:
            print(str(e) + "NOT VALID NAME")

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

    def fade(self, width, height, color, start=0, end=300, delay=1): 
        fade = pygame.Surface((width, height))
        fade.fill(color)
        for alpha in range(start, end):
            fade.set_alpha(alpha)
            # redrawWindow()
            self.win.blit(fade, (0,0))
            if self.go_win: 
                text = self.wave_font2.render("Win", 2, rgb(255,255,255))
            elif self.go_lose:
                text = self.wave_font2.render("Game Over", 2, rgb(255,255,255))
            else:
                text = text = self.wave_font2.render("Wave " + str(self.wave + 1), 2, rgb(255,255,255))
            self.win.blit(text, (self.width/2 - text.get_width()/2, self.height/2 - text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(delay)

    def update_stat(self):

        # seconds ticking
        self.seconds = (pygame.time.get_ticks()-self.start_ticks)/1000
        list_keys = ['seconds', 'waves', 'money', 'lives', 'money2']
        list_items = [round(self.seconds), self.wave + 1 ,self.money, self.lives, self.money/2]

        # store data every 2 seconds
        rest = math.fmod(self.seconds, 2)
        if rest <= 0.01:
            for key, item in zip(list_keys, list_items):
                self.data_dict[key].append(item)

def play_sound(*args):
    if len(args) == 3:
        a,b,c = args[0],args[1],args[2]
        pygame.mixer.Channel(a).play(pygame.mixer.Sound(os.path.join("game_assets/sounds/", b)), maxtime=c)
    elif len(args) == 2:
        a,b = args[0],args[1]
        pygame.mixer.Channel(a).play(pygame.mixer.Sound(os.path.join("game_assets/sounds/", b)))
