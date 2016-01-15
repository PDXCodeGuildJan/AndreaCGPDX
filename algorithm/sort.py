def main():
# find unsorted list 
	usl=[8,4,6,3,5,2,1]

	print("Unsorted:", usl)
	sorted_list = bubble_sort(usl)
	print("Sorted:", sorted_list)

def selection_sort(usl):
	
	# find unsorted list 
	index = 0

	numInlist = len(usl)

	
	
	# repeat until there are no more numbers
	while index < numInlist:
		#so the variable should be in the loop it will be used in 
		#always start looking at the start of the usnorted part of list
		#that is why we put index there 
		nownumIndex = index

		lowIndex = nownumIndex
		# find smallest number in list 

		#looping thru unsorted part of list and index indicates begining of unsorted part
		while nownumIndex < len(usl):
		
			#if the the nmber we are looking at now is smaller then the lowest number in place 0 in the index then...
			if usl[nownumIndex] < usl[lowIndex]:
				#take lowest # in unsorted list makes it the smallest number 
				lowIndex=nownumIndex
			# now we are looking at the next index 
			nownumIndex += 1

		# swap smallest number with first number in list 
		
		temp= usl[index]
		usl[index]=usl[lowIndex]
		usl[lowIndex] =temp
	
		# update the 1st num of the unsorted list to be the next number in the unsorted list    
		index += 1


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
				temp=unsl[now]
				unsl[now]= unsl[next]
				unsl[next]= temp

			xindex += 1 
		unsrtlength -= 1
	return unsl


# find first vaule in unslist 
	# compare vaule found and next value in the unsl
	# if 1st is larger then swap vaules 
	# move to next index
	# if the next index is last in the unsorted section of the list  start at 1st step.  
# if the 1st vaule in the unsl is the last vaule in the unsorted list them stop. 





			

main()

