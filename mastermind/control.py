from view import Display 
from model import Guess 
from model import ModelStuff 

class Game:
	""""""
	def __init__(self):
		self.a_model = ModelStuff()
		self.the_display = Display()

	def start_round(self):
		"""Runs a round"""
		self.a_model.juggle_the_masters_ballz()
		print(self.the_display.draw_masters_ballz(self.a_model.masters_ballz))
		###########################################################################
		# calling a method from display object 
		#create a new guess object by using the input from the display.
		styrofoam_cup = self.the_display.get_user_guess()
		styrofoam_cup = self.the_display.validate_guess_format_template(styrofoam_cup)

		print(self.a_model.turn)
		#a_model.all_guesses[a_model.turn] = 
		x = Guess(styrofoam_cup)

		"""the above code acomplishes passing a valid formated list on balls into a guess object """

		print(x.this_guess)#a_model.all_guesses[a_model.turn])
###############################################################################
		print(self.the_display.draw_win())
		






		"""decide to loop back for valid input
		 string based on validate_guess_format_template(all_guess[ : ], turn): loop back to start_round():"""

		""" Decide to loop back for valid input based on 
		 validate_guess_format_template (). Decide if round won or ongoing 
		 call draw_b_template(all guesses[], turn) """


def main():

	a_game = Game()
	a_game.start_round()



if __name__ == '__main__':
	main()