arr=[7, 1, 4, 5, 3, 2]
for i in range(1, len(arr)):
    cur = arr[i]
    j = i-1
    while j>=0 and cur<arr[j]:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=cur

print(arr)

#time complexity = o(1)
#space complexity = o(n^2)
