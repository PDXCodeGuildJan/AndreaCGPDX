"""Angry Dice game with Objects"""

__author__ = "Andrea L. Flack"

from random import randint 

def main(): 
	game = Angry_Dice()
	game.loop()

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
			 

	def test_diehold():
			ang_game = Angry_Dice()
			print (ang_game.die_1.is_holding)
			ang_game.die_1.value = 4
			print (ang_game.die_2.is_holding)
			ang_game.die_hold()
			print (ang_game.die_1.is_holding)
			print (ang_game.die_2.is_holding)
			ang_game.validate_hold()

			print (ang_game.die_1.is_holding)
			print (ang_game.die_2.is_holding)




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

	def start(self):
	
		print ("Hello Homie! What's shaking? Ya... o .. ya? Well"\
			"\n maybe you should keep that... to yourself! mmmmkay."\
			"\n So Welcome to ANGRY DICE!"\
			"\n Do you wanna know how to play?"\
			"\n Well I will tell you anyhow." 
			"\n It is a solo game played with dice. There are 3 rounds."\
			"\n The object of the game is to roll dice in order from 1 to "\
			"\n 6 as quickly as you can! "\
			"\n Round one: The goal is to get a 1 & 2."\
			"\n If you only roll one of the pair you need,"\
			"\n you may hold it and roll the other dice until you reach your goal"\
			"\n number. Once you have the pair you need you may move on to the next"\
			"\n round. "\
			"\n Round two: is similar. The goal is to get 3 & 4."\
			"\n If you roll two 3's aka ANGRY DICE you must go back to start in"\
			"\n Round 1. You may also hold numbers. "\
			"\n Round three: The goal is to roll a 5 & 6. You may not hold the"\
			"\n 6 and if you get two 3's a.k.a Angry Dice the game will kick you"\
			"\n back to start.")

	def roll(self):
		if self.die_1.is_holding == False:
			self.die_1.roll()
		if self.die_2.is_holding == False:
			self.die_2.roll()
		print(self.die_1)
		print(self.die_2)


		

	def die_hold(self):
		"""Holds the die that matches the goal vaule"""

		V = input("Would you like to hold die 1? (y)es or anything else to skip. ")
		if V.lower() == "y":
			self.die_1.is_holding = True

		V = input ("Would you like to hold die 2? (y)es or anything else to skip. ") 
		if V.lower() == "y":
			self.die_2.is_holding = True 

	def validate_hold(self):
		"""checks to see if hold is valid and unlocks if not valid"""
		if self.die_1.is_holding  and self.die_1.value not in self.round_goals[self.current_round] and self.die_1.value != 6:
			self.die_1.is_holding = False
			print("Do you think this is a valid hold? Well you are wrong buddy!!! NO HOLD FOR YOU!")

		if self.die_2.is_holding  and self.die_2.value not in self.round_goals[self.current_round] and self.die_2.value != 6:
			self.die_2.is_holding = False
			print("Do you think this is a valid hold? Well you are wrong buddy!!! NO HOLD FOR YOU!")
		if self.die_1.is_holding and self.die_2.is_holding and self.die_1.value == self.die_2.value: 
			self.die_1.is_holding = False 
			print("Why would you hold two of the same? Dummy! I will fix it geez!") 


		

	def chk_angry(self):
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
				print ("Good Job Weinie! On to next Round"\
						"\n Woot"\
						"\n Woot"\
						"\n Woot"\
						"\n Woot"\
						"\n Woot"\
						)
				self.current_round +=1
			else:
				print("YOU ARE A WEINIE -"\
					"\n i mean A WINNER...WINNER CHICKEN DINNER!!"\
					"\n(we do not provide chiken dinners)")
			return True
		else:
			return False 

			
	def unlock(self):
		self.die_1.is_holding = False
		self.die_2.is_holding =	False

	def loop(self):
		"""loops thru game"""
		self.start()
		while self.current_round < 4:
			self.roll()
			if self.chk_angry():
				self.unlock()
				continue
			if self.evaluate_die():
				self.unlock()
				continue 
			self.die_hold()
			self.validate_hold()

	

if __name__=='__main__':
		main()
		
