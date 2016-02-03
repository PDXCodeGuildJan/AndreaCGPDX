#search fucntions, binary

from sort import bubble_sort


def main():
	unsorted_list = ["e", "z", "l", "o", "b", "f"]
	target_vaule = "b"


	#call the search function, catch what it returns 
	sorted_list, target_index = binary_search(unsorted_list, target_vaule)

	#print out our soulution 
	print("I found", target_vaule, "it's at", target_index)

	#implements the bi search
def binary_search(the_list, target_vaule):


	#first sor the list 

	sorted_list = bubble_sort(the_list)
	
	#search for the target vaule 

	#find len of current segment, 
	length= len(sorted_list)

	# initialize start and end vari
	start = 0
	end = length - 1

	#if len>= 1, looking in target
	while length >= 1:
		#find the middle of the list  
		mid = start + (length // 2)
		start = 0
		end = length - 1

		#determine if middle value is greater or less then, or equal 
		#if equal we found it return middle		
		if sorted_list[mid] == target_vaule:
			return (sorted_list, mid)

			 #if greater than, reduce segment to left half from middle, repeat loop
		elif sorted_list[mid]> target_vaule:
			length = len(sorted_list[:mid])
			end = mid
			#if less than reduce sefment to the rifht from the middle, repeat loop
		elif sorted_list[mid] < target_vaule:
			lenth = len(sorted_list[mid + 1:end])
			start = mid + 1  
		mid = start + (length // 2)
	#if we cant find th eindex return -1
	return (sort_list, -1)


if __name__=="__main__":
	main()