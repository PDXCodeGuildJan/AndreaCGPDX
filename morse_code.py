__author__= "Andrea and Shanna"

from morse import morse 
import re


def main():


	write_code("poop", "dodo.txt")

	read_code("test_code.txt")


def read_code(morse_msg_filename):

	open_file = open(morse_msg_filename)

	morse_msg = open_file.read()

	open_file.close()

	decoded_string == " "

	list_of_words = re.split("       ", morse_msg)
	list_of_letters =re.split("   ", list_of_words)

	print (list_of_words)
	print (list_of_letters)
		


def write_code(es, morse):
	encoded_string==""
	for cha in es.upper():
		if cha in morse:
			code= morse[cha]
			encoded_string += code + "   "
		elif cha == " ":
			encoded_string += "       "

		
	open_file= open("morse", "w")
	open_file.write(encoded_string)	
	output_fule.close()
		


if __name__=='__main__':
	main()
