"""Angry Dice game with Objects"""

__author__ = "Andrea L. Flack"

from random import randint 

def main(): 
	pass 

class Die:
	"""tracks the dice vaules during game"""
	def __init__(self):
			self.value = 1
			self.is_holding = False 
			self.possible_value = {

		1:"""
+-------+              
|       |
|   o   |               
|       |              
+-------+ """,               

	   2:"""
+-------+ 
| o     |
|       |
|     o |
+-------+ """,

	   3:"""
+-------+
| \   / |
| ^   ^ |
| ----- |
+-------+""",

	   4:"""
+-------+ 
| o   o |
|       |
| o   o |
+-------+ """, 

	   5:"""
+-------+ 
| o   o |
|   o   |
| o   o |
+-------+ """, 

	   6:"""
+-------+ 
| o   o |
| o   o |
| o   o |
+-------+ """ }
	   

		

	def roll(self):
		"""Rolls dice to come up with random numbers on a die """
		#two options:
		#roll or hold 
		self.value = randint (1, 6)


	def __str__ (self):
		return self.possible_value[self.value]
		 



class Angry_Dice:

	def __init__(self):
		self.die_1 = Die()
		self.die_2 = Die()
		self.current_round = 1 
		self.round_goals = {
			1: [1, 2],
			2: [3, 4],
			3: [5, 6]
			}
		
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
		To begin enter "A" to exit enter "E" To hold a die 1 press "H" To hold die 2 press "H2" """
		pass

	def die_hold(self, current_round, round_goals):
		"""Holds the die that matches the goal vaule"""

		V = input("Would you like to hold a die?")
		if V == "H"
			self.holding = True
		if V =="H2"
			self.holding = True 

		

	def chk_angry(self, current_round):
		"""checks to see if roll is angry"""
		if self.die_1.value == 3 and self.die_2.value == 3:
			print ("We are Angry!")
			self.current_round = 1 
			return True
		else: 
			return False 
			


	def evaluate_die(self):
		"""Decides which outcome matches the roll vaules"""
		if self.die_1.value in self.round_goals[self.current_round] and self.die_2.value in self.round_goals[self.current_round] and self.die_1.value != self.die_2.value:
	
			if self.current_round < 3:  
				print ("Good Job Weinie! On to next Round")
				self.current_round +=1
			else:
				print("YOU ARE A WEINIE - i mean A WINNER...WINNER CHICKEN DINNER!!(we do not provide chiken dinners)")
	
			
			



	

if __name__=='__main__':
	main()


