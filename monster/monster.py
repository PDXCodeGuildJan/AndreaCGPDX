from creature import Creature 


class Monster(Creature):

	AGGRO= "aggressive"
	DEFENSE= "defensive"


	def __init__(self):
		#imports characteristics of creature to monster 
		super(Monster, self).__init__()

		self.personality = Monster.AGGRO
