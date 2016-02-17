from random import randint

class Ballz:
	"""docstring for Ballz"""
	def __init__(self, color_str = "black"):
		self.balls_representation = {"blue":"blu", "yellow":"yel", "red":"red", "green":"gre", "white":"wht", "black":"blk"}
		self.color = self.balls_representation[color_str]
	def __str__(self):
		return self.color




	def juggle_the_ball(self):

		rand1 = randint(0,5)
		balls_keys = list(self.balls_representation.keys())
		self.color = self.balls_representation[balls_keys[rand1]]



class ModelStuff:
	"""docstring for ModelStuff"""
	def __init__(self):
		self.wins_n_losses = 0
		self.turn = 0
		self.masters_ballz = [Ballz(),Ballz(),Ballz(),Ballz()]
		self.welcome_n_instructions = "Welcome? Finish me!"
		self.all_guesses = []

	def validate_guess(self, alist_of_ballz):
		pass

	def juggle_the_masters_ballz(self):

		self.masters_ballz[0].juggle_the_ball()
		self.masters_ballz[1].juggle_the_ball()
		self.masters_ballz[2].juggle_the_ball()
		self.masters_ballz[3].juggle_the_ball()

class PegBin:
	"""docstring for PegBin"""
	def __init__(self):
		pegs = []

	def eval_color(self):
		pass

	def eval_position(self):
		pass

	def sort_pegs(self):
		pass

class Guess:
	"""docstring for Guess"""
	def __init__(self):
		self.this_guess = []
		self.a_peg_bin = PegBin()
		self.guess_number = 0

	def validate_guess(self, masters_ballz):
		pass

def main():
	some_ball = Ballz()
	a_model = ModelStuff()
	some_peg_bin = PegBin()
	some_guess = Guess()
	print(a_model.masters_ballz[0].color)
	a_model.juggle_the_masters_ballz()
	print(a_model.masters_ballz[0].color)



if __name__ == '__main__':
	main()