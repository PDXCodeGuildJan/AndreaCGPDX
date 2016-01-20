
__author__= "Andrea L. Flack"
def main():
	# take a random list and use merge_sort to sort it
	unsorted = [4, 7, 14, 2, 94, 38, 2]
	sorted = merge_sort(unsorted)
	print (sorted)

def merge_sort(list_a):  
#Implements the merge sort algorithm, recursively, in python.
	# if the length of the list is smaller or = 2 1 then return that list
	if len(list_a) <= 1:
		return list_a 
		#otherwise the length of list //2 = the mid 
	else:
		mid = len(list_a) // 2

		#assigning variables for the seperate lists 
		#and noting the indexs that will be in the list with slicing 
		# the empty side denotes the assumption that it goes to end of index 
		left = merge_sort(list_a[:mid])
		right = merge_sort(list_a[mid:])

		#return the merged list 

		return merge(left, right)

#merge _sort
#	Splits list into 2 halves
#	first_sorted = sort first half using merge_sort 
#	Second_sorted = sort 2nd half using merge_sort
#	merge the 2 halves back together into merged list 
#	return merged sorted list 


def merge(left, right): 
	#given 2 list, merge them together into a 3rd list, which is sorted
	#nameing varible for list index and temp list to store in 
	li=0
	ri=0
	tl=[]

	#loops until all items in list are evaluated and returned 
	while len(left) > li and len(right) > ri:

		if left[li] < right[ri]:
			tl.append(left[li])
			li += 1
		else :
			tl.append(right[ri])
			ri += 1
	if len(left) >= li:
		tl.extend(left[li:])
	if len(right) >= ri:
		tl.extend(right[ri:])

	return tl

if __name__=='__main__':
	main()