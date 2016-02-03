"""Implements a very simple phonebook using a Dictionary"""

__author__ = "Andrea L. Flack"

import re
# Initialize our dictionary, which will store our phone number 
phonebook = {}

def main():
	"""the main driver function of our Phonebook"""
# load existing data in to phonebook
	load_phonebook()
	print("phonebook after load", phonebook)
        

	print("Welcome to the Phonebook.")

	option = ""

	while option != "E":

		option = input("you can:\n\t(A)dd or \n\t(D)elete \n\t(S)earch with name\n\t(N)umber by Search\n\t(E)xit\n which would you like to do? ")

		if option.upper() == "A":
			name = input ("what is the new contact name? ")
			number= input("what is " + name + "'s number? ")
			add_contact(name, number)

		elif option.upper() == "D":
			name = input(" what contact are you removing? ")
			delete_contact(name)
		elif option.upper() == "E":
			print("Good-Bye")
			exit()
		elif option.upper() == "P":
			print_phonebook()
		elif option.upper() == "S":
			name = input("what contact do you want? ")
			search(name)
		elif option.upper() == "N":
			num = input("What is the number?" )
			search_by_number(num)
		else:
			print("I'm sorry, I did not understand.")


def add_contact(name, phonenumber):
	"""Does an addition to the phonesbook with the given contact info"""
	#remove white space with this 
	regex = "\s+\Z"
	thing_you_replace_with = "" 
	scrubbed_name = re.sub(regex, thing_you_replace_with, name)
	print(scrubbed_name)

	regex = "[0-9]+"
	nums = re.findall(regex, phonenumber)
	new_num = ""
	for every_num in nums:
		new_num += every_num
	
	formated_num = "(" + new_num[0:3] + ")" + new_num[3:6] + "_" + new_num[6:]
	print (formated_num)	
	

	phonebook[scrubbed_name] = phonenumber
	print("Your new Homie", scrubbed_name, "was added with number", phonenumber, "\n")
	print("")

	#save and update pb
	save_phone_book()

def delete_contact(name):
	if name in phonebook:
		del phonebook[name]
		print("The punk", name,"was removed from Phonebook." "\n")
	else:
		print(name, "contact does not exist", "\n")

		save_phone_book()

def search(name):
	if name in phonebook:
		number= phonebook[name]
		print( name, "'s number is", number, "\n")


def search_by_number(search_number):
	result= ""
	for name, number in phonebook.items():
		if search_number == number:
			result = name

	if result == "":
		print("Sorry, no contact found.")
			
	else: 
			
		print(name, "'s number is ", number, "\n")

def print_phonebook():
	print("Contacts:")
	print("___________")
	for name in phonebook:
		print(name, ":\t", phonebook[name], "\n")

def save_phone_book():
	open_file = open("phonebook.txt", "w")
	open_file.write(str(phonebook))
	open_file.close()

def load_phonebook():
	global phonebook 

	load_file = open("phonebook.txt", "a")
	load_file.close()

	load_file =  open("phonebook.txt", "r")
	phonebook_data = load_file.read()
	load_file.close()

	#convert from string back to dictionary
	if phonebook_data: 
		phonebook= eval(phonebook_data)
		print ("phonebook in load function", phonebook)




if __name__=='__main__':
	main()

