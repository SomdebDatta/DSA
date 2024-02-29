"""
Merge sort uses divide and conquer approach.
Remember 2 way merge sort, wherein, there are 2 input arrays, and elements are compared b/n the 2 arrays one by one
and assembled into a single array.
Similarly, in merge sort algorithm used below, the unsorted input array is broken into individual elements.
Each element treated as a separate array and compare with the neighbouring element (now an array).
These comparisons are then assembled into a single array.
"""

arr = [4, 2, 1, 6, 7]
print(f"OG arr - {arr}")


def merge(lb, ub):
    sorted_arr = list()
    mid = (lb + ub) // 2
    i, j = lb, mid + 1
    while i <= lb and j <= ub:
        if arr[i] <= arr[j]:
            sorted_arr.append(arr[i])
            i += 1
        else:
            sorted_arr.append(arr[j])
            j += 1
    while i <= mid:
        sorted_arr.append(arr[i])
        i += 1
    while j <= ub:
        sorted_arr.append(arr[j])
        j += 1
    print(f"sorted array - {sorted_arr}")
    arr[lb : ub + 1] = sorted_arr


def mergeSort(lb, ub):
    if lb >= ub:
        return
    if lb < ub:
        mid = (lb + ub) // 2
        mergeSort(lb, mid)
        mergeSort(mid + 1, ub)
        merge(lb, ub)


mergeSort(0, len(arr) - 1)
print(arr)
