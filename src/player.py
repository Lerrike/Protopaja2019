#Data storage class. Has update and getter methods.
class Player():
	def __init__(self, number):
		self.number = number #Player number, "name"
		self.heart = 0
		self.heartList = []
		self.breath = 0
		self.breathList = []
		self.xPos = 0
		self.yPos = 0
		
	def update_all(self, new_xPos, new_yPos, new_breath, new_heart):
		self.xPos = new_xPos
		self.yPos = new_yPos
		self.breath = new_breath
		self.heart = new_heart
		self.update_breathList(new_breath)
		self.update_heartList(new_heart)
		
	def return_number(self):
		return self.number
		
	def change_heart(self, new_heart):
		self.heart = new_heart
	
	def return_heart(self):
		return self.heart
		
	def update_heartList(self, new_heart):
		self.heartList.insert(0, new_heart)
		if len(self.heartList) > 250:
			self.heartList.pop()
		
	def return_heartList(self):
		return self.heartList
		
	def change_breath(self, new_breath):
		self.breath = new_breath
	
	def return_breath(self):
		return self.breath
		
	def update_breathList(self, new_breath):
		self.breathList.insert(0, new_breath)
		if len(self.breathList) > 250:
			self.breathList.pop()
		
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