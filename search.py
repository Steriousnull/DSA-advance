array = [1,2,3,4,5]
x = 12
for i in range(0, len(array)):
    if array[i] == x:
        print(i)
        break
else:
    print("element not presernt")