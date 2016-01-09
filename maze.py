def main():

	print("Welcome to the Verbally Abusive Maze!"
		"Now find your way out Dummy!"
		" Oh and press B to exit fool!")
	#ask them where they want to go 

	entree=input("The door locked behind you and it smells almost as bad as you!"
		" you have two directions to choose from"
		"Hurry! Which way will you go? west or east")

	if entree=="west":
		lions()
	elif entree=="east":
		snakeroom() 
	else:
		ass()


def lions():
	print("You dummy! You entered a room full of Lions."
			" You are Dead unless you go back.")


def snakeroom ():
	print("Good job dork! You have entered the Snake room.")
		
	entree=input(" See all those little holes in wall?"
		" Yes you do dummy! So in 20"
		"seconds the room will fill with snakes!"
		" Yes, they want to eat you! You may go down or south."
		"Hurry! Pick a direction")
	if entree=="down":
		win()
	elif entree=="south":
		dragon()
	else:
		ass()

def win():
	print("You Win Dummy...I mean Good Job Homie! Stay Golden!")

def dragon():
	print("Ha Ha Ha! We all can't be the brightest crayon in the box!"
		" You just walked into the Dragon room. You DIE")

def ass():
	print("Did I say that was an option? You die dummy!")
