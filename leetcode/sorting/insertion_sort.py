"""
Time complexity: 
Space complexity:
"""

arr = [13, 46, 24, 52, 20, 9]
arr2 = [1, 2, 3, 4]


def insertionSort(arr):
    for i in range(len(arr) - 1):
        pos = i + 1
        for j in range(0, i):
            if arr[j] > arr[pos]:
                arr[j], arr[pos] = arr[pos], arr[j]

    return arr


print(insertionSort(arr))
print(insertionSort(arr2))
