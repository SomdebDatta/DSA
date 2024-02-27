"""
Selection Sort:
    1. In each iteration, we will select the minimum element from the range of the unsorted array using an inner loop.
    2. After that, we will swap the minimum element with the first element of the selected range(in step 1). 
    3. Finally, after each iteration, we will find that the array is sorted up to the first index of the range. 

    Time Complexity: O(N^2)
    Space Complexity: 0(1)
"""

arr = [13, 46, 24, 52, 20, 9]
arr2 = [1, 2, 3, 4]


def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


print(selectionSort(arr2))
