import random


# time = O(nlogn), space = O(1)
def quick_sort(arr):

    def helper(start, end):
        if start >= end:
            return
        pivotIndx = random.randint(start, end)
        arr[start], arr[pivotIndx] = arr[pivotIndx], arr[start]
        pivot = arr[start]
        smallestIndx = start
        for bigger in range(start + 1, end + 1):
            if pivot > arr[bigger]:
                smallestIndx += 1
                arr[smallestIndx], arr[bigger] = arr[bigger], arr[smallestIndx]
        arr[smallestIndx], arr[start] = arr[start], arr[smallestIndx]

        helper(start, smallestIndx - 1)
        helper(smallestIndx + 1, end)

    helper(0, len(arr) - 1)
    return arr
