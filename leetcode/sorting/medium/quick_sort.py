empty_arr = []
single_elem_arr = [0]
arr = [13, 46, 24, 52, 20, 9]
sorted_arr_asc = [1, 2, 3, 4]
sorted_arr_desc = [4, 3, 2, 1]


def partition(inp_arr, low, high):
    pivot = inp_arr[low]
    i, j = low, high

    while i < j:
        while inp_arr[i] <= pivot and i < high:
            i += 1
        while inp_arr[j] > pivot and j > low:
            j -= 1
        if i < j:
            inp_arr[i], inp_arr[j] = inp_arr[j], inp_arr[i]

    inp_arr[low], inp_arr[j] = inp_arr[j], inp_arr[low]
    return j


def quickSort(inp_arr, low, high):
    if low < high:
        p_index = partition(inp_arr, low, high)
        quickSort(inp_arr, low, p_index - 1)
        quickSort(inp_arr, p_index + 1, high)


print(arr)
quickSort(arr, 0, len(arr) - 1)
print(arr)

print(empty_arr)
quickSort(empty_arr, 0, len(empty_arr) - 1)
print(empty_arr)

print(single_elem_arr)
quickSort(single_elem_arr, 0, len(single_elem_arr) - 1)
print(single_elem_arr)

print(sorted_arr_asc)
quickSort(arr, 0, len(sorted_arr_asc) - 1)
print(sorted_arr_asc)

print(sorted_arr_desc)
quickSort(sorted_arr_desc, 0, len(sorted_arr_desc) - 1)
print(sorted_arr_desc)
