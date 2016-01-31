"""Angry Dice game with Objects"""

__author__ = "Andrea L. Flack"

def main():  

class die:
	"""tracks the dice vaules during game"""

			possible_value = {

		1:

	"""+-------+              
	   |       |
	   |   o   |               
	   |       |              
	   +-------+ """,               

	   2:

	"""+-------+ 
	   | o     |
	   |	   |
	   |     o |
	   +-------+ """,

	   3:

	"""+-------+
	   | \   / |
	   | ^   ^ |
	   | ----- |
	   +-------+""",
	   4:


	"""+-------+ 
	   | o   o |
	   |	   |
	   | o   o |
	   +-------+ """, 

	   5:


	"""+-------+ 
	   | o   o |
	   |   o   |
	   | o   o |
	   +-------+ """, 

	   6:


	"""+-------+ 
	   | o   o |
	   | o   o |
	   | o   o |
	   +-------+ """ }
	   

		def __init__(self):
				self.value = 1
				self.is_holding = False 

		def roll(self):
				"""Rolls dice to come up with random numbers on a die """
				#two options:
				#roll or hold 

				self.value = randint (1, 6)

				
		def __str__ (self):



class angry_dice:

	def __init__(self):
			#die 1 : die 
			#die 2 : die
			# current.round:int 
			#round goal 

def create_dice():
	"""Creates dice for the game"""


	pass

def die_hold(valid, invalid):
	"""Holds the die that matches the goal vaule"""
	pass

def evaluate_die(angry, full_match, reset):
	"""Decides which outcome matches the roll vaules """
	pass

def weiner(winning, rounds):
	"""Decides if the win moves to next round or wins the game"""
	pass

def start():
"""	welcomes player and tells them what the rules are and how to play and exit"""

pass

