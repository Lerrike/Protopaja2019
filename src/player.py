class Player():
	def __init__(self, number):
		self.number = number #Player number, "name"
		self.hearth = 0
		self.hearthList = [123,145,154,154,165,123,88,87,86,89,89,87,65,54,77,77,88,89,77,104,104,114,134,134]
		self.breath = 0
		self.breathList = [55,55,55,45,45,34,23,23,24,34,34,24,22,22,25,25,26,27,36]
		self.xPos = 10
		self.yPos = 22
		
	def update_all(self, new_hearth, new_breath, new_xPos, new_yPos):
		pass
		
	def return_number(self):
		return self.number
		
	def change_hearth(self, new_hearth):
		self.hearth = new_hearth
	
	def return_hearth(self):
		return self.hearth
		
	def update_hearthList(self, new_hearth):
		self.hearthList.insert(0, new_hearth)
		
	def return_hearthList(self):
		return self.hearthList
		
	def change_breath(self, new_breath):
		self.breath = new_breath
	
	def return_breath(self):
		return self.breath
		
	def update_breathList(self, new_breath):
		self.breathList.insert(0, new_breath)
		
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