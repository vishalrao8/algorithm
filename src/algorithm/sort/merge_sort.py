# Time = O(nlogn), space = O(n)
def merge_sort(arr: list[int]) -> list[int]:
    def helper(start: int, end: int) -> list[int]:
        if start >= end:
            return arr[start:end+1]
        
        mid = start + ((end - start) // 2)
        leftList = helper(start, mid)
        rightList = helper(mid + 1, end)

        aux: list[int] = []
        i = 0
        j = 0
        while i < len(leftList) and j < len(rightList):
            if leftList[i] < rightList[j]:
                aux.append(leftList[i])
                i += 1
            else:
                aux.append(rightList[j])
                j += 1

        while i < len(leftList):
            aux.append(leftList[i])
            i += 1
        while j < len(rightList):
            aux.append(rightList[j])
            j += 1

        return aux

    arr = helper(0, len(arr) - 1)

    return arr


def merge_sort_in_place(arr: list[int]) -> list[int]:
    def helper(start: int, end: int):
        if start >= end:
            return 
        
        mid = start + ((end - start) // 2)
        helper(start, mid)
        helper(mid + 1, end)

        aux: list[int] = []
        i = start
        j = mid + 1
        while i <= mid and j <= end:
            if arr[i] < arr[j]:
                aux.append(arr[i])
                i += 1
            else:
                aux.append(arr[j])
                j += 1

        while i <= mid :
            aux.append(arr[i])
            i += 1
        while j <= end:
            aux.append(arr[j])
            j += 1

        arr[start: end+1] = aux

    helper(0, len(arr) - 1)
    return arr