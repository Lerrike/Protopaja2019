class Player():
	def __init__(self, number):
		self.number = number #Player number, "name"
		self.hearth = 0
		self.hearthList = []
		self.breath = 0
		self.breathList = []
		self.xPos = 0
		self.yPos = 0
		
	def update_all(self, new_hearth, new_breath, new_xPos, new_yPos):
		pass
		
	def return_number(self):
		return self.number
		
	def change_hearth(self, new_hearth):
		self.hearth = new_hearth
	
	def return_hearth(self):
		return self.hearth
		
	def update_hearthList(self, new_hearth):
		pass
		
	def return_hearthList(self):
		return self.hearthList
		
	def change_breath(self, new_breath):
		self.breath = new_breath
	
	def return_breath(self):
		return self.breath
		
	def update_breathList(self, new_breath):
		pass
		
	def return_breathList(self):
		return self.breathList
		
	def change_xPos(self, new_xPos):
		self.xPos = new_xPos
		
	def return_xPos(self):
		return self.xPos
		
	def change_yPos(self, new_yPos):
		self.yPos = new_yPos
		
	def return_yPos(self):
		return self.yPos