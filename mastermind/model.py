from random import randint

class Ballz:
	"""represents a single ball"""
	def __init__(self, color_str = "black"):
		"""the defult color for the ball is black"""
		self.balls_representation = {"blue":"blu", "yellow":"yel", "red":"red", "green":"gre", "white":"wht", "black":"blk"}
		self.color = self.balls_representation[color_str]
	def __str__(self):
		return self.color




	def juggle_the_ball(self):
		"""this function randomizes the ball's color"""

		rand1 = randint(0,5)
		balls_keys = list(self.balls_representation.keys())
		self.color = self.balls_representation[balls_keys[rand1]]



class ModelStuff:
	"""docstring for ModelStuff- this is a misc. bin for this mvc module."""
	def __init__(self):
		self.wins_n_losses = 0
		self.turn = 0
		self.masters_ballz = [Ballz(),Ballz(),Ballz(),Ballz()]
		self.welcome_n_instructions = "Welcome? Finish me!"
		self.all_guesses = []

	def elvaluate_guess(self, alist_of_ballz):
		"""This method evaluates the guess for correctness or incorrectness against the masters_ballz"""
		pass

	def juggle_the_masters_ballz(self):
		"""hard codes juggling each ball in masters_ballz indivdually. The function could be improved 
		by looping thru for the length of masters_ballz."""

		self.masters_ballz[0].juggle_the_ball()
		self.masters_ballz[1].juggle_the_ball()
		self.masters_ballz[2].juggle_the_ball()
		self.masters_ballz[3].juggle_the_ball()

class PegBin:
	"""peg bin is a very important data object that allows the controler t preform the tricky parts 
	of our game logic"""
	def __init__(self):
		pegs = []

	def eval_color(self):
		"""This determines how many ball colors the player has correct."""
		pass

	def eval_position(self):
		"""This determines how many ball positions the player has correct."""
		pass

	def sort_pegs(self):
		"""This sorts the pegs in a way that does not give the position of the masters_ballz"""
		pass

class Guess:
	"""bundels the users correctly formated ball guess along with the peg bin scoring of said guess"""
	def __init__(self):
		self.this_guess = []
		self.a_peg_bin = PegBin()
		self.guess_number = 0

	

def main():
	"""Testing shit"""
	some_ball = Ballz()
	a_model = ModelStuff()
	some_peg_bin = PegBin()
	some_guess = Guess()
	print(a_model.masters_ballz[0].color)
	a_model.juggle_the_masters_ballz()
	print(a_model.masters_ballz[0].color)



if __name__ == '__main__':
	main()