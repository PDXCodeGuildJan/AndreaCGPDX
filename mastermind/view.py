class Display:
	"""docstring for Display"""
	def __init__(self):
		
		self.input_template = ""

	def show_display(self):
		pass
	def draw_menu(self):
		pass
	def draw_board_template(self):
		pass
	
	def draw_masters_ballz(self, alist_of_balls):
		"""The drawing of the master balls: we return a string with the master's hand."""
		present_em = ""
		

		present_em = str(alist_of_balls[0]) + " " + str(alist_of_balls[1]) + " " + str(alist_of_balls[2]) + " " + str(alist_of_balls[3])

		return present_em
		

	def draw_win(self):
		pass 
	
	def draw_loser(self):
		pass
	def get_play_or_quit(self):
		pass
	def get_user_guess(self):
		pass

def main():
	pass


if __name__ == '__main__':
	main()