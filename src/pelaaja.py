class Pelaaja():
	def __init__(number):
		self.number = number #Player number, "name"
		self.hearth = 0
		self.hearthList = []
		self.breath = 0
		self.breathList = []
		self.xPos = 0
		self.yPos = 0
		
	def update_all(new_hearth, new_breath, new_xPos, new_yPos):
		pass
		
	def return_number():
		return self.number
		
	def change_hearth(new_hearth):
		self.hearth = new_hearth
	
	def return_hearth():
		return self.hearth
		
	def update_hearthList(new_hearth):
		pass
		
	def return_hearthList():
		return self.hearthList
		
	def change_breath(new_breath):
		self.breath = new_breath
	
	def return_breath():
		return self.breath
		
	def update_breathList(new_breath):
		pass
		
	def return_breathList():
		return self.breathList
		
	def change_xPos(new_xPos):
		self.xPos = new_xPos
		
	def return_xPos():
		return self.xPos
		
	def change_yPos(new_yPos):
		self.yPos = new_yPos
		
	def return_yPos():
		return self.yPos