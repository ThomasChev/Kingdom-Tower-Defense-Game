from matplotlib import pyplot as plt
import os

class Graph:
	def __init__(self):
		self.data_x = []
		self.data_y = []
		self.name = os.path.join("graphs/fig/","plot_money.png")
		self.label = "money"
		self.style = 'fivethirtyeight'
		self.xlabel = 'Time (s)'
		self.ylabel = 'Money ($)'
		self.title = 'Money = f(t)'
		self.lines = {}
		self.nrow = 2
		self.ncol = 2
		self.ax_dict = {}
		self.obj = {}
		self.attack_towers = ["Shin", "Moubu", "Kanki", "Ouhon", "Ten", "Kyoukai", "Ryo", "Fortress"]
		self.support_towers = ["Ten", "Kyoukai", "Ryo", "Fortress"]
		self.ys = []
		self.linestyle = ['solid', 'solid', 'dotted']

	def plot(self):

		plt.style.use(self.style)

		fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=self.nrow, ncols=self.ncol)
		self.obj['ax1'] = ax1
		self.obj['ax2'] = ax2
		self.obj['ax3'] = ax3
		self.obj['ax4'] = ax4

		# elem, ax_dict[key] du type : 
		# elem = [self.df['seconds'], self.df['money'], 'money', 'Money = f(t)', 'Time (s)' , 'Money ($)']
		# ax_dict[key] = [self.graph[0].lines['money'], self.graph[0].lines['money/2']]
		for key in self.obj: 
			ax = self.obj[key]
			for i, elem in enumerate(self.ax_dict[key]): 
				self.data_x = elem[0]   
				self.data_y = elem[1]
				self.label = elem[2]
				self.title = elem[3]
				self.xlabel = elem[4]
				self.ylabel = elem[5]
				if key == 'ax1' or key == 'ax3':
					ax.plot(self.data_x, self.data_y, label=self.label, linestyle=self.linestyle[i])
				else:

					if key == 'ax2':
						label = self.attack_towers
					if key == 'ax4':
						label = self.support_towers
					
					self.ys = []
					for k, y in enumerate(elem[6]):
						self.ys.append(y)
					ax.stackplot(self.data_x, self.ys[0], self.ys[1], self.ys[2], self.ys[3], labels=label, baseline ='zero')
			self.set_up(ax)
		
		plt.tight_layout()
		plt.show()
		

	def set_up(self, ax):
		ax.legend(loc='upper left')
		# ax.set_title(self.title)
		ax.set_xlabel(self.xlabel)
		ax.set_ylabel(self.ylabel)
		# plt.savefig(self.name)


