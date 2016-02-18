"""create a generic Die class that allows the user to pass a list of values, that serve as the die's sides"""
from random import randint 

class Die: 
	def __init__(self, possiblevalues):
		self.current_value =  None 
		self.possible_values = possible_values

	def roll(self):

		index = randint(0, len(possible_values) -1)
		self.current_value = self.possible_values[index]

	def __str__(self): 
		return str(self.current_value)