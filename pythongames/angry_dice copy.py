"""Angry Dice Game: Solo game played with 2 dice. The 
	goal of the game is to roll form 1 to 6 in order quickly. 
	Once you attain the goal pair for that round you move on to 
	the next round of three. If two 3/ Angry faces are rolled it 
	kicks you back to the beging.
 """

__author__ = "Andrea L FLack"

 from random import randint

def main():
	
	pass

def create_dice():
	"""Creates dice for the game"""


	pass

def die_hold(valid, invalid):
	"""Determines if the die the player wishes to hold is a valid 
		entree or not. If it is valid it will hold the die that matches
		the goal vaule. If not the game will tell you to pick a diffrent
		die or roll agian"""
	pass

def evaluate_die(angry, full_match, reset):
	"""Decides which outcome matches the roll vaules. 
		if the roll has no matches: roll again.  
		if the roll is angry x2: reset 
		if the roll has 2 round matches then preceed to next round. 
		Tell them the result. 
	 """
	pass

def weiner(winning, rounds):
	"""Decides if the win moves them to to next round or wins the game"""
	pass

def start():
	"""	Welcomes player and tells them what the rules are and how to 
	play and exit--- Hello Homie! What's shaking? Ya... o .. ya? Well
	maybe you should keep that... to yourself! mmmmkay. 
	So Welcome to ANGRY DICE! 
	Do you wanna know how to play? 
	Well I will tell you anyhow. 
	It is a solo game played with "dice". There are 3 rounds. 
	The object of the game is to roll dice in order from 1 to 
	6 as quickly as you can! 
	Round one: The goal is to get a 1 & 2.  
	If you only roll one of the pair you need,
	you may hold it and roll the other dice until you reach your goal
	number. Once you have the pair you need you may move on to the next
	round. 
	Round two: is similar. The goal is to get 3 & 4. 
	If you roll two 3's aka ANGRY DICE you must go back to start in 
	Round 1. You may also hold numbers. 
	Round three: The goal is to roll a 5 & 6. You may not hold the 
	6 and if you get two 3's a.k.a Angry Dice the game will kick you
	back to start. 
	To begin enter A to exit enter E"""

	pass


class Die:
	"""tracks the dice vaules during game"""
	def __init__(self):

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
	   +-------+ """ 
	   }

	   def __init__(self):

		   	self.value = 1 
			self.is_holding = False
	

	def roll(self):
		"""Rolls dice to come up with random numbers on a 
		die """

		#two options 
		# roll
		#hold


		self.value = randint(1, 6)

		pass
	def __str__ (self):
		pass


die_1 = Die()
die_2 = Die()
current_round = 0 





if __name__=='__main__':
	main()