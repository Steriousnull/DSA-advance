# merge sort
# split everthing using recusion
#space complexity is 0(n)
#time complexity is 0(nlog(n))

def Mergesort(array):
    if len(array)>1:
        middle = len(array)//2
        left = array[0:middle]
        right = array[middle:]

        Mergesort(left)
        Mergesort(right)

        lp = 0 #left pointer
        rp = 0 #right pointer
        fp = 0 #[,]

        while (lp<len(left)and rp<len(right)):
            if left[lp]<right[rp]:
                array[fp] = left[lp]
                lp+=1
            else:
                array[fp] = right[rp]
                rp+=1

            fp+=1

        while lp<len(left):
            array[fp]=left[lp]
            fp+=1
            lp+=1

        while rp<len(right):
            array[fp]=right[rp]
            fp+=1
            rp+=1

array = [3,2,4,1,6,9,5,8,1,1]
print(array)
Mergesort(array)
print(array)


"""In the context of your Mergesort function, lp stands for "left pointer". It is used to traverse the left subarray during the merge step of the merge sort algorithm.

Here’s how lp works in the merge process:

    After the array is split into two halves (left and right), both halves are sorted recursively.
    During the merge step, two pointers (lp for the left subarray and rp for the right subarray) are used to compare elements from both halves.
    The lp pointer starts at 0 (the beginning of the left subarray) and increments as elements from the left subarray are added to the sorted result.

Example:

Let’s break down the merge step for array = [3, 2]:
Initial Split:

    left = [3], right = [2]

Merge Step:

    lp = 0 points to the first element of left (value 3).
    rp = 0 points to the first element of right (value 2).
    Compare left[lp] (value 3) with right[rp] (value 2):
        Since 2 < 3, 2 is added to the sorted array.
        Increment rp to 1 (move the right pointer forward).
    The right array is now exhausted, so add the remaining element from left:
        Add 3 to the sorted array.
        Increment lp to 1 (move the left pointer forward).

Final Result:

The sorted array becomes [2, 3].

In summary, lp is a pointer to track the position in the left subarray, helping to merge it with the right subarray in sorted order. Similarly, rp is the pointer for the right subarray, and fp tracks the position in the original array where elements are being placed.

"""