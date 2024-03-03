"""
Python always uses pass by reference. The behaviour differs because of the datatypes
being mutable / immutable.
(int, string, bool, tuple, etc) are immutable -> so they behave as if they were passed by value.
(lists, dictionaries, etc) are mutable -> so they behave as if they were passed by reference.
But BTS everything was passed by reference and in the case of immmutable objects,
python just created a new object everytime you changed the value i.e. edited the string or manipualted the integer.
"""

empty_arr = []
single_elem_arr = [0]
arr = [13, 46, 24, 52, 20, 9]
sorted_arr_asc = [1, 2, 3, 4]
sorted_arr_desc = [4, 3, 2, 1]


def recInsertionSort(inp_arr, i, n):
    # print(i, id(i))
    # print(inp_arr, id(inp_arr))
    if i == n:
        return
    j = i
    while j > 0 and inp_arr[j] < inp_arr[j - 1]:
        inp_arr[j - 1], inp_arr[j] = inp_arr[j], inp_arr[j - 1]
        j -= 1
    recInsertionSort(inp_arr, i + 1, n)


print(arr)
recInsertionSort(arr, 0, len(arr))
print(arr)

print(empty_arr)
recInsertionSort(empty_arr, 0, len(empty_arr))
print(empty_arr)

print(single_elem_arr)
recInsertionSort(single_elem_arr, 0, len(single_elem_arr))
print(single_elem_arr)

print(sorted_arr_asc)
recInsertionSort(arr, 0, len(sorted_arr_asc))
print(sorted_arr_asc)

print(sorted_arr_desc)
recInsertionSort(sorted_arr_desc, 0, len(sorted_arr_desc))
print(sorted_arr_desc)
