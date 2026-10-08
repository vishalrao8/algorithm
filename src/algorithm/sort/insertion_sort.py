# time = O(N^2), space = O(1)
def insertion_sort(arr: list[int]) -> list[int]:
    if len(arr) < 2:
        return arr
    for i in range(1, len(arr)):
        pivot = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > pivot:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = pivot
    return arr
