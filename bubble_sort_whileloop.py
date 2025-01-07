arr = [1, 10, 11, 5, 2]
while True:
    a = True
    for j in range(0, len(arr)-1):
        if arr[j]<arr[j+1]:
            continue
        elif arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            a = False
# next 2 line is just for reference we can remove if we want
    if a == False:
        continue
    elif a == True:
        break
print(arr)
