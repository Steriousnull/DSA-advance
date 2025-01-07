arr = [4, 5, 2, 3, 1]

for pos in range(len(arr)-1):
    minindex = pos
    for i in range(pos+1, len(arr)):
        if arr[i]<arr[minindex]:
            minindex = i
    
    arr[minindex],arr[pos] = arr[pos],arr[minindex]
print(arr)

