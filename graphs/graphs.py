# from matplotlib import pyplot as plt
# import os


#

# # plot Tower Graphs and Enemy bar
# graph_1 = Graph()
# graph_1.name = os.path.join("graphs/fig/","plot_towers.png")
# graph_1.write_line(self.df, 'waves')
# graph_1.plot(0)

# graph_2 = Graph()
# graph_2.name = os.path.join("graphs/fig/","plot_enemies.png")
# graph_2.import_bar(self.list_enemy_spawned, killed)
# graph_2.plot(1)

# plt.show()

# class Graph:
# 	def __init__(self):
# 		self.data_x = []
# 		self.data_y = []
# 		self.name = os.path.join("graphs/fig/","plot_money.png")
# 		self.label = "money"
# 		self.style = 'fivethirtyeight'
# 		self.xlabel = 'Time (s)'
# 		self.ylabel = 'Money ($)'
# 		self.title = 'Money = f(t)'
# 		self.lines = {}
# 		self.nrow = 2
# 		self.ncol = 2
# 		self.ax_dict = {}
# 		self.obj = {}
# 		self.attack_towers = ["Shin", "Moubu", "Kanki", "Ouhon", "Ten", "Kyoukai", "Ryo", "Fortress"]
# 		self.support_towers = ["Ten", "Kyoukai", "Ryo", "Fortress"]
# 		self.enemies = ["Zao Warrior", "Yan Warrior", "Qi Warrior", "Wei Catapult", "Wei Balista", "Han Warrior", "Chu Warrior", "Chu Elephant", "Chu Boat", "Yan Boat", "Qi Boat", "Riboku"]
# 		self.linestyle = ['solid', 'solid', 'dotted']
# 		self.ys = []

# 	def plot(self, nb):

# 		if nb == 0:
# 			fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=self.nrow, ncols=self.ncol)
# 			self.obj['ax1'] = ax1
# 			self.obj['ax2'] = ax2
# 			self.obj['ax3'] = ax3
# 			self.obj['ax4'] = ax4

# 			for key in self.obj: 
# 				ax = self.obj[key]
# 				for i, elem in enumerate(self.ax_dict[key]): 
# 					self.data_x = elem[0]   
# 					self.data_y = elem[1]
# 					self.label = elem[2]
# 					self.title = elem[3]
# 					self.xlabel = elem[4]
# 					self.ylabel = elem[5]
# 					if key == 'ax1' or key == 'ax3':
# 						ax.plot(self.data_x, self.data_y, label=self.label, linestyle=self.linestyle[i])
# 					else:
# 						if key == 'ax2':
# 							label = self.attack_towers
# 						if key == 'ax4':
# 							label = self.support_towers
# 						self.ys = []
# 						for k, y in enumerate(elem[6]):
# 							self.ys.append(y)
# 						ax.stackplot(self.data_x, self.ys[0], self.ys[1], self.ys[2], self.ys[3], labels=label, baseline ='zero')
# 				ax.legend(loc='upper left')
# 				ax.set_xlabel(self.xlabel)
# 				ax.set_ylabel(self.ylabel)

# 		if nb == 1:
# 			fig, ax = plt.subplots(nrows=1, ncols=1)
# 			width = 0.2
# 			ax.barh(self.data_x, self.data_all, width, color='#FF2700')
# 			ax.barh(self.data_x, self.data_killed, width, color='#008FD5')
# 			ax.set_ylabel('Enemies')
# 			ax.set_xlabel('Number')
# 			ax.set_title('Game Enemy Distribution')
# 			ax.legend(labels=['Killed', 'Not Killed'])
# 			plt.style.use(self.style)
# 			plt.tight_layout()
# 			plt.show()

# 			# plt.barh(self.data_x, self.data_y)

# 	def write_line(self, df, param_x):
		
# 		if param_x == 'waves':
# 			titre_x = "f(wave)"
# 			x = 'Wave'
# 		elif param_x == "seconds":
# 			titre_x = "f(t)"
# 			x =  'Time (s)'

# 		# line = [x, y, label, title, xlabel, ylabel]
# 		self.lines['1a'] = [df[param_x], df['money_spent'], 'spent', 'Money = ' + titre_x, x , 'Money ($)']
# 		self.lines['1b'] = [df[param_x], df['money_earnt'], 'earnt', 'Money = ' + titre_x, x, 'Money ($)']
# 		self.lines['1c'] = [df[param_x], df['money'], 'money', 'Money = ' + titre_x, x, 'Money ($)']
# 		self.lines['2a'] = [df[param_x], df['towers'], 'towers', 'Towers = ' + titre_x, x, 'Attack Towers', [df['shin'],  df['moubu'],  df['kanki'],  df['ouhon']]]
# 		self.lines['3a'] = [df[param_x], df['lives'], 'lives', 'Lives = ' + titre_x, x, 'Lives (nb)']
# 		self.lines['4a'] = [df[param_x], df['towers'], 'towers', 'Towers = ' + titre_x, x, 'Support Towers', [df['ten'],  df['kyoukai'],  df['ryo'], df['fortress']]]
# 		# ax = [line1, line2...]
# 		self.ax_dict['ax1'] = [self.lines['1a'], self.lines['1b'], self.lines['1c']]
# 		self.ax_dict['ax2'] = [self.lines['2a']]
# 		self.ax_dict['ax3'] = [self.lines['3a']]
# 		self.ax_dict['ax4'] = [self.lines['4a']]

# 	def import_bar(self, population, killed):
# 		self.data_x = self.enemies[:]
# 		self.data_all = population[:]
# 		self.data_killed = killed[:]
# 		self.data_x.reverse()
# 		self.data_all.reverse()
# 		self.data_killed.reverse()


		


       