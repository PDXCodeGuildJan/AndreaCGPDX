
# find smallest number in list 
# swap smallest number with first number in list 
# update the 1st num of the unsorted list to be the next number in the unsorted list    
# repeat until there are no more numbers 



# unslorted list 
usl=()


def selction_sort(usl):
	#finding smallest number in list 
	smn=min(usl)
	usl.insert(0, smn)

