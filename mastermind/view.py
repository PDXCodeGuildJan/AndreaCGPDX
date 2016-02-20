class Display:
	"""In the mvc model this display class corresponds to the view."""

	def __init__(self):
		#this will be a reg ex statement that validates the users input according to format requirments. 
		self.input_template = ""

	def show_display(self):
		"""we intend to write a string that will show the entire display at once 
		insted of updating and showing results bit by bit"""
		pass

	def draw_welcome(self):
		"""Displays welcome message and instructions"""
		pass


	def draw_menu(self):
		"""menu will contain - reminder of instructions, balls bin, format reminder, wins and losses."""
		pass

	def draw_board_template(self):
		"""This is a tmeplate for the board itself excluding the munue and user prompt."""
		pass

	
	def draw_masters_ballz(self, alist_of_balls):
		"""The drawing of the master balls: we return a string with the master's hand."""
		present_em = ""
		

		present_em = str(alist_of_balls[0]) + " " + str(alist_of_balls[1]) + " " + str(alist_of_balls[2]) + " " + str(alist_of_balls[3])

		return present_em
		

	def draw_win(self):
		"""When player wins a display message will pop up that indicates win. Initiate prompt to play another round or quit"""

		return "Winner Winner... chicken dinner. (*Disclaimer: We don't provide chicken dinners!*) Enough pluck to try your luck again? or are you a quitter? Then enter 'I suck.' so you can quit. >>>"
		 
	
	def draw_loser(self):
		"""When player has reached the maximun amount og guesses a message will appear to denote losing"""
		pass
	def get_play_or_quit(self):

		pass
	def get_user_guess(self):
		"""This function takes in user input as a str which is a comma 
		seperated list of the displaynames of the balls (4). It will return a string. There
		needs to be a prompt for the correct format of input. """

		user_input = input()
		return user_input 



	def validate_guess_format_template(self, astring):
		"""uses reg ex statement that is called bibidy blop- if user input is incorrectly formated then then program 
		flow returns to display step while alerting the user they fucked up. Takes in a string and returns a list or nothing."""
		formatted_output = []
		#WE MUST GO BACK AND ADD MORE REGEX TO VERIFY USER INPUT!!!!!

		#but to hell with it. Split the list by spaces.
		formatted_output = astring.split()


		return formatted_output



def main():
	pass


if __name__ == '__main__':
	main()