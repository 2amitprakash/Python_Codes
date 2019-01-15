def f_max(lst):
    if len(lst) == 2:
        return lst[0] if lst[0] >= lst[1] else lst[1]
    sub_max = f_max(lst[1:])
    return lst[0] if lst[0] >= sub_max else sub_max
#End of Function

l = [2, 14, 6, 8, 1]

print ("Max in the list: ", f_max(l))
