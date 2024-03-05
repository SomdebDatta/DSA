def checkSortedArray(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return True
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


arr_sorted = [1, 2, 3, 4, 5, 6, 7]
arr_unsorted = [1, 3, 0]
print(checkSortedArray(arr_sorted))
print(checkSortedArray(arr_unsorted))
