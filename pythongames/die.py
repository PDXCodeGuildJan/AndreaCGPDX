from random import randint

def die():
	roll = randint(1, 6)
	print(roll)

# num1 and 2 are my high and lo and roll is what number is rolled 
#randint is a function 
#else is catch all
def custom_die(num1, num2):
	roll= randint(num1, num2)
	if roll == num1:
		print(roll, "Critical fail!")
	elif roll == num2:
		print(roll, "Critical hit!")
	else: 
		print(roll)



def main():
	print("Welcome to Die Machine. Enter q to exit")
	entree =""
	# ask the user how many dice to roll 
	while entree != "q":

		entree = input("how many dice roll do you want to roll?")
		if entree =="q":
			exit()

		total_rolls = int(entree)
		# find out how big the die is 

		entree = input( "how many sides?")
		if entree =="q":
			exit()
		max_num = int(entree)
		#roll that dice
		for something in range(0, total_rolls):
			custom_die(1, max_num)

main()
	







