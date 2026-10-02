def selection_sort(arr):
    for i in range(len(arr)):
        minmIndex = i
        for y in range(i + 1, len(arr)):
            if arr[minmIndex] > arr[y]:
                minmIndex = y
        arr[minmIndex], arr[i] = arr[i], arr[minmIndex]
    return arr
