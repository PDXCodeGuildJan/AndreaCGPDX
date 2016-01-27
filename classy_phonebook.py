
"""A Phonebook program implemented with classes."""
__author__ = "Andrea Flack"

class Contact: 
	"""defines contact object to store info about ppl"""

	def __init__(self, f_name, l-name):
		#assign passed arguments to their corrasponding properties
		self.first_name = f_name
		self.last_name = l_name

		self.phone_num = ""
		self.addresses = {}
		self.email = ""

	def update_address(self, addy_key, street="",
										 unit="",
										 city="", 
										 state="",
										 zip="", 
										 country=""): 
		"""Update the addy at the addy_key with the info passes,"""

		pass

def format_phone_num(self, phone_num):
	"""format the phonenumber of the contact all pretty like"""

	pass

def print_contact(self):
	"""print out the contacts info, all pretty like"""
	pass

class Address:
	"""defines the addy object to be used with contacts"""

	def __init__(self):
		self. street =""
		self.unit = ""
		self.city = ""
		self.state = ""
		self.zip = ""
		self.country = ""

	def __str__(self):
		"""print out the addy, formated all pretty like"""

		formated_str = self.street
		formated_str += "\n" + self.unit  
		formated_str += "\n" + self.city + " " + self.state
		formated_str += " " + self.zip_code
		formated_str += "\n" + self.country




		













