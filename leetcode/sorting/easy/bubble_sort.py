"""
Time Complexity: O(N^2)
Space Complexity: O(1)
"""

arr = [13, 46, 24, 52, 20, 9]
arr2 = [1, 2, 3, 4]


def bubbleSort(arr):

    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(arr)

    return arr


print(bubbleSort(arr))
print(bubbleSort(arr2))
