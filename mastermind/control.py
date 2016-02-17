from view import Display 
from model import ModelStuff 

class Game:
	"""docstring for Game"""
	def __init__(self):

		def welcome(self):
			pass
		def start_round(self):
			pass

		"""decide to loop back for valid input
		 string based on validate_guess_format_template(all_guess[ : ], turn): loop back to start_round():"""

		""" Decide to loop back for valid input based on 
		 validate_guess_format_template (). Decide if round won or ongoing 
		 call draw_b_template(all guesses[], turn) """



def main():

	the_display = Display()
	a_model = ModelStuff()
	print(the_display.draw_masters_ballz(a_model.masters_ballz))
	

if __name__ == '__main__':
	main()