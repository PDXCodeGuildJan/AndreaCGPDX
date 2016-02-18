from creature import Creature 

class Hero(Creature):


	def __init__(self):
		#imports characteristics of creature to monster 
		super(Hero, self).__init__()

		self.level = 1