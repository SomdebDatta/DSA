"""
Time complexity: 
Space complexity:
"""

empty_arr = []
single_elem_arr = [0]
arr = [13, 46, 24, 52, 20, 9]
sorted_arr_asc = [1, 2, 3, 4]
sorted_arr_desc = [4, 3, 2, 1]


def insertionSort(arr):

    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr


print(insertionSort(empty_arr))
print(insertionSort(single_elem_arr))
print(insertionSort(arr))
print(insertionSort(sorted_arr_asc))
print(insertionSort(sorted_arr_desc))
