import random

def quicksort(list):
    if len(list) < 2:
        return list
    else:
        pi = random.randint(0,len(list)-1)
        #pi = 0
        print ("The list is {l} and random index is {i}".format(l=list,i=pi))
        pivot = list.pop(pi)
        less = [i for i in list if i <= pivot]
        more = [i for i in list if i > pivot]
        return quicksort(less) + [pivot] + quicksort(more)
#End of function
l=[2,3,6,7,4,6,9,11,-1,5]
print ("The sorted list is - ",quicksort(l))
