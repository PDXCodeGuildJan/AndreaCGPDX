from view import Display 
from model import Guess 
from model import ModelStuff 

class Game:
	""""""
	def __init__(self):


		def start_round(self):
			"""begins a round"""
			pass

		"""decide to loop back for valid input
		 string based on validate_guess_format_template(all_guess[ : ], turn): loop back to start_round():"""

		""" Decide to loop back for valid input based on 
		 validate_guess_format_template (). Decide if round won or ongoing 
		 call draw_b_template(all guesses[], turn) """

class Round:
	""""""

def main():
	

	the_display = Display()
	a_model = ModelStuff()
	print(the_display.draw_masters_ballz(a_model.masters_ballz))
	# calling a method from display object 
	#create a new guess object by using the input from the display.
	styrofoam_cup = the_display.get_user_guess()
	styrofoam_cup = the_display.validate_guess_format_template(styrofoam_cup)
	
	print(a_model.turn)
	#a_model.all_guesses[a_model.turn] = 
	x = Guess(styrofoam_cup)
	
	print(x)#a_model.all_guesses[a_model.turn])

	

if __name__ == '__main__':
	main()