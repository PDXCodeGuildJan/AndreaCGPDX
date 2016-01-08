from random import randint

def die():
	roll = randint(1, 6)
	print(roll)


def custom_die(num1, num2):
	print(randint(num1, num2))


def main():
	# ask the user how many dice to roll 

	total_rolls = input("how many dice roll do you want to roll?")
 	total_rolls = int(total_rolls)
 # find out how big the die is 

 	max_num = int(input( "how many sides?"))

	#roll that dice
	for lizard in range(0, total_rolls):
	custom_die(1, max_num)
	







