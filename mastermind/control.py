from view import Display 
from model import Guess 
from model import ModelStuff 

class Game:
	""""""
	def __init__(self):
		self.a_model = ModelStuff()
		self.the_display = Display()

##############################################################################
#	Please excuse the use of temporary print statements to simulate program
#	flow because it violates the MVC. Eventually all view elements will
#	be assemballed into a single string to be displayed all at once (see 
#	display).
#
#############################################################################  
	
	def start_round(self):
		"""Runs a round"""
		self.a_model.juggle_the_masters_ballz()
		
		print(self.the_display.draw_welcome())

		print("The master's Guess: ", self.the_display.draw_masters_ballz(self.a_model.masters_ballz))
		

		 
		# create a new guess object by using the input from the display.
		# calling a method from display object
		styrofoam_cup = self.the_display.get_user_guess()
		styrofoam_cup = self.the_display.validate_guess_format_template(styrofoam_cup)

		print("Turn number:", self.a_model.turn)
		x = Guess(styrofoam_cup)

		"""the above code acomplishes passing a valid formated list on balls 
		into a guess object """

		#Prints prove that we succesfully transfered the users input into model.
		print(x.this_guess)

		print(self.the_display.draw_win())

		print(self.the_display.draw_loser())





		"""decide to loop back for valid input
		 string based on validate_guess_format_template(all_guess[ : ], turn): loop back to start_round():"""
		""" Decide to loop back for valid input based on 
		 validate_guess_format_template (). Decide if round won or ongoing 
		 call draw_b_template(all guesses[], turn) """


def main():

	quit_or_not = "not"

	while quit_or_not != 'I suck.':
		a_game = Game()
		a_game.start_round()
		quit_or_not = input(">>>")
	



if __name__ == '__main__':
	main()