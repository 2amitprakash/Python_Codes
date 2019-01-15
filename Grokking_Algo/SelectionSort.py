def findSmallestIndx(arr):
	Index = 0 # for smallest as default
	for i in range(1, len(arr)):
		if arr[i] < arr[Index]:
			Index = i
	return Index
#End of function findSmallest
def selectionSort(arr):
	newArr = []
	for i in range(len(arr)):
		index = findSmallestIndx(arr)
		newArr.append(arr.pop(index))
	return newArr
#End of Function

my_list = [1, 3, -1, 4, 0]
print ("Original Arr: ", my_list)
print ("Sorted Arr: ", selectionSort(my_list))