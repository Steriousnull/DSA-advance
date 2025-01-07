#space complexity = ?
#time complexity = ?

import random 

def quicksort(array):
    if len(array)<=1:
        return array
    
    pivot = random.choice(array)

    left = [i for i in array if i < pivot]
    right = [i for i in array if i > pivot]
    middle = [i for i in array if i == pivot]
    return quicksort(left) + middle + quicksort(right)

#elonged
"""    left = []
    for i in array:
        if i<pivot:
            left.append(i)

    right = []
    for i in array:
        if i<pivot:
            left.append(i)

    middle = []
    for i in array:
        if i==pivot:
            left.append(i)"""

    

array = [3,2,5,7,9,1,6]
print("before sorting : ",array)

print("after sorting : ",quicksort(array))