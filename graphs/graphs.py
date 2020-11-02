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
		self.towers = ["Shin", "Moubu", "Kanki", "Ouhon", "Ten", "Kyoukai", "Fortress"]
		self.ys = []

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
			for elem in self.ax_dict[key]: 
				self.data_x = elem[0]   
				self.data_y = elem[1]
				self.label = elem[2]
				self.title = elem[3]
				self.xlabel = elem[4]
				self.ylabel = elem[5]
				if key != 'ax4':
					ax.plot(self.data_x, self.data_y, label=self.label)
				else:
					for y in elem[6]:
						self.ys.append(y)
					ax.stackplot(self.data_x, self.ys[0], self.ys[1], self.ys[2], self.ys[3], self.ys[4], self.ys[5], self.ys[6], labels=self.towers, baseline ='zero')
			self.set_up(ax)
		
		plt.tight_layout()
		plt.show()

	# def add_line(self, ax, x, y, name):
	# 	ax.plot(x, y, label=name)

	def set_up(self, ax):
		ax.legend(loc='upper left')
		# ax.set_title(self.title)
		ax.set_xlabel(self.xlabel)
		ax.set_ylabel(self.ylabel)
		# plt.savefig(self.name)

	# def add_ax(self, *args)
	# 	fig, ax1, ax2 = args[0], args[1],args[2]
	# 	fig, (ax1, ax2) = plt.subplots(nrows=self.nrow, ncols=self.ncol)
		# try:
	 #    	fig, ax1, ax2 = args[0], args[1],args[2]
		# 	fig, (ax1, ax2) = plt.subplots(nrows=self.nrow, ncols=self.ncol)
		# except:
		# 	print('error in add_ax')


