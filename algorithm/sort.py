def main():
# find unsorted list 
	usl=[8,4,6,3,5,2,1]

	print("Unsorted:", usl)
	sorted_list = bubble_sort(usl)
	print("Sorted:", sorted_list)

def swap(usl, index_a, index_b):
	usl[index_a], usl [index_b]= usl[index_b], usl[index_a]
	
	# find unsorted list 
	


	return usl
# take unsorteded list

def bubble_sort(unsl):
	
	length= len(unsl)


	unsrtlength= length
	while unsrtlength > 1:

		xindex= 0

		while xindex < length - 1:
			now=xindex
			next=xindex +1 
		
			if unsl[now]> unsl[next]:
				swap(unsl, now, next)

			xindex += 1 
		unsrtlength -= 1
	return unsl


# find first vaule in unslist 
	# compare vaule found and next value in the unsl
	# if 1st is larger then swap vaules 
	# move to next index
	# if the next index is last in the unsorted section of the list  start at 1st step.  
# if the 1st vaule in the unsl is the last vaule in the unsorted list them stop. 

def insert_sort(usl):
# make a tempcar for the index of the thing 
# we're currently sort

	for start_index, vaule in enumerate (usl):

		lost_index= start_index
		lost_value =vaule

		while (lost_vaule < usl[lost_index -1]
			and lost_index > 0):
			usl = selection_sort(usl, lost_index, lost_index-1)



			#decrement the lost_index
			lost_index -= 1 


	return usl

# write this for any 

if __name__=="__main__":		

	main()

