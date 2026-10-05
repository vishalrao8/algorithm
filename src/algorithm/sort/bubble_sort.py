# time = O(N^2), space = O(1)

def bubble_sort(arr):
    for start in range(len(arr)):
        for x in range(len(arr) - 1, start, -1):
            if arr[x - 1] > arr[x]:
                arr[x], arr[x - 1] = arr[x - 1], arr[x]
    return arr
