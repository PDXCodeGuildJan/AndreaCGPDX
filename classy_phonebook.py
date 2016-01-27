
"""A Phonebook program implemented with classes."""
__author__ = "Andrea Flack"

import re
def main():

	#test contact in address classes  with jim 
	jim = Contact("Jim", "Everyone")
	jim.phone_num = "1234567891"
	jim.email = "jim@gmail.com"
	jim.update_address("Home", city="Portland")
	jim.update_address("Work", "1234 Awesome Ln", "Apt8", "ShittyCIty", "OR", "81818", "Crayolastan")
	print (jim)


class Contact: 
	"""defines contact object to store info about ppl"""

	def __init__(self, f_name, l_name):
		#assign passed arguments to their corrasponding properties
		self.first_name = f_name
		self.last_name = l_name

		self.phone_num = ""
		self.addresses = {}
		self.email = ""

	def update_address(self, addy_key, street=None,
										 unit=None,
										 city=None, 
										 state=None,
										 zip_code=None, 
										 country=None): 
		"""Update the addy at the addy_key with the info passes,"""

		#check to see if you already have an address for that key s
		if addy_key in self.addresses:
			temp_address = self.addresses[addy_key]
		else:

		#make a new address object 
			temp_address = Address()
		#set the new addy street to thwatever was passed 
		if street:
			temp_address.street = street 

		if unit:
			temp_address.unit = unit

		if city:
			temp_address.city = city 

		if state:
			temp_address.state = state

		if zip_code:
			temp_address.zip_code = zip_code

		if country:
			temp_address.country = country 

		#Assign the address to the given assy key for the contact 
		self.addresses[addy_key] = temp_address



	def format_phone_num(self, phone_num):
		"""format the phonenumber of the contact all pretty like"""

		regex = "[0-9]+"
		nums = re.findall(regex, phone_num)

		#formats into string 
		new_num = ""

		for every_num in nums:
			new_num += every_num

		#introduced the correct formatting to the string of nums 
		
		formated_num = "(" + new_num[0:3] + ")" + new_num[3:6] + "_" + new_num[6:]
		print (formated_num)	
		
		# save formated num to contact 
		self.phone_num + formated_num 

	def __str__(self):
		"""print out the contacts info, all pretty like"""

		#initalize formated string 
		formated_str = "{0} {1}".format(self.first_name, self.last_name)

		#if there is a phone num
		if self.phone_num:
			#format the phone number 
			self.formated_phone_num = (self.phone_num)
			#add formated number to str
			formated_str +="\nPhone: {0}".format(self.phone_num)

			#if ther is an email
		if self.email:
			formated_str += "\nEmail: {0}".format(self.email)

		#if there is an addy
		if self.addresses:
			#loop through all addys and pring them 
			formated_str += "\nAddresses:"
			formated_str += "\n--------------------------------------------------------------"
			for key, address in self.addresses.items():
				formated_str += "\n{0}:".format(key)
				formated_str += "\n{0}".format(address)
				formated_str += "\n--------"

		return formated_str



class Address:
	"""defines the addy object to be used with contacts"""

	def __init__(self):
		self. street =""
		self.unit = ""
		self.city = ""
		self.state = ""
		self.zip_code = ""
		self.country = ""

	def __str__(self):
		"""print out the addy, formated all pretty like"""

		formated_str = ""

		if self.unit != "":

			formated_str = self.street
			formated_str += "\n" + self.unit  
			formated_str += "\n" + self.city + " " + self.state
			formated_str += " " + self.zip_code
			formated_str += "\n" + self.country

		return formated_str



if __name__== '__main__':
	main()
		













