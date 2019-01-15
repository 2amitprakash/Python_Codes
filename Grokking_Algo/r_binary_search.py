def r_binary_search(s_list, item):
    def recurse(low, high):
        mid = (low + high)//2
        guess = s_list[int(mid)]
        if low > high:
            return None
        elif guess == item:
            return mid
        elif guess > item:
            return recurse(low, mid - 1 )
        else:
            return recurse(mid + 1, high)
    return recurse(0,len(s_list)-1)
#End of Function

my_list = list(range(5000001))
print (r_binary_search(my_list, 5000000))
print (r_binary_search(my_list, 5))
print (r_binary_search(my_list, -1))
