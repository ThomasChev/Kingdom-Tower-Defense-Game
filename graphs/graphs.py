from matplotlib import pyplot as plt
import os

ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]

py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666, 84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]

# js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000,
#             78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]
# plt.plot(ages_x, js_dev_y, label='JavaScript')

# dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232,
#          78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]
# plt.plot(ages_x, dev_y, color='#444444', linestyle='--', label='All Devs')

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
		self.ncol = 1
		self.ax_dict = {}
		self.obj = {}
		# self.fig = None
		# self.ax1 = None
		# self.ax2 = None
		# self.ax = (self.ax1, self.ax2)
		# self.plt = plt

	def plot(self):


		# self.fig, self.ax = plt.subplots(nrows=self.nrow, ncols=self.ncol)
		# self.add_ax(self.fig, self.ax1, self.ax2)
		
		# ax_list = [ax1, ax2]
		# ax_key = ['ax1', 'ax2']
		# for ax, key in zip(ax_list, ax_key):
		plt.style.use(self.style)

		fig, (ax1, ax2) = plt.subplots(nrows=self.nrow, ncols=self.ncol)
		self.obj['ax1'] = ax1
		self.obj['ax2'] = ax2
		for key in self.obj: 
			ax = self.obj[key]
			for elem in self.ax_dict[key]: # ax_dict[key] = [self.graph[0].lines['money'], self.graph[0].lines['money/2']]
				self.data_x = elem[0]   # elem = [self.df['seconds'], self.df['money'], 'money', 'Money = f(t)', 'Time (s)' , 'Money ($)']
				self.data_y = elem[1]
				self.label = elem[2]
				self.title = elem[3]
				self.xlabel = elem[4]
				self.ylabel = elem[5]
				print('ax=',key,' label=',self.label, ' title=',self.title, ' x=',self.xlabel, ' y=', self.ylabel)
				self.add_line(ax, self.data_x, self.data_y, self.label)
			self.set_up(ax)
		
		plt.tight_layout()
		plt.show()

	def add_line(self, ax, x, y, name): # [self.data_x, self.data_y]
		ax.plot(x, y, label=name)

	def set_up(self, ax):
		ax.legend()
		ax.set_title(self.title)
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



# import pandas as pd
# from matplotlib import pyplot as plt

# plt.style.use('seaborn')

# data = pd.read_csv('data.csv')
# ages = data['Age']
# dev_salaries = data['All_Devs']
# py_salaries = data['Python']
# js_salaries = data['JavaScript']


