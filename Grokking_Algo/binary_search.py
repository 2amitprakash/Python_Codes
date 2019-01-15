def binary_search(s_list, item):
	low = 0
	high = len(s_list)-1

	count = 0
	while low <= high:
		count = count + 1
		mid = (low + high)//2
		guess = s_list[int(mid)]
		if guess == item:
			print ("No. of steps: ", count)
			return mid
		if guess > item:
			high = mid - 1
		else:
			low = mid + 1
	#End While
	print ("No. of steps: ", count)
	return None
#End of Function

my_list = list(range(5000001))

print (binary_search(my_list, 5000000))
print (binary_search(my_list, 1))
print (binary_search(my_list, -1))
