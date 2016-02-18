
__author__= "Andrea Flack"

def main(): 
	
   link = LinkedList()
   link.add(4)
   link.add(2)
   link.add(86)
   link.add(4)
   link.add(7)
   print("Current list:", link)
   link.remove(4)
   print("List after first 4 is removed:", link)

   link.remove(4)
   print("List after second 4 is removed:", link)

   print("Success! Attempt to remove a third 4 yielded no crashes!")
   link.remove(4)
   
   # Output of above code:
   # -------------------------
   # Current list: 4 2 86 4 7 
   # List after first 4 is removed: 2 86 4 7 
   # List after second 4 is removed: 2 86 7 
   # Attempt to remove a third 4 yielded no crashes


class Node: 

	def __init__(self, value):
	 
		self.value = value
		self.next_node = None

	

class list: 

	def __str__(self):
		 string_list = ""
		 list_of_node = self.head

		 while cur_node.next_node:
		 	string_list += str(list_of_node.value) + ","

		 	cur_node = cur_node.next_node

		 #make a temp empty string 
		 #find start of list 
		 # 
		 # looping the list and look at eh value 
		 #append value of each node to temp string 

		self.head = None

def add(self, value):
	new_node = Node(value)

	cur_node = head

	while cur_node.next_node: 
		cur_node = cur_node.next_node

	cur_node.next_node = new_node

def search(self):
	pass

	#i do not remember any of the linked list stuff. 
	# i have no idea on how to go about this 
	# i suck 
	# and i do not even remember if i finished this or if it worked
	# i copied all this under here from the google and now i am just going
	# to futz around with it bc why not 
	# nope nope nope all wrong
def delete(self, value):
    current = self.head
    previous = None
    found = False
    while current and found is False:
        if current.get_value() == data:
            found = True
        else:
            previous = current
            current = current.get_next()
    if current is None:
        raise ValueError("Data not in list")
    if previous is None:
        self.head = current.get_next()
    else:
        previous.set_next(current.get_next())


