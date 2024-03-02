empty_arr = []
single_elem_arr = [0]
arr = [13, 46, 24, 52, 20, 9]
sorted_arr_asc = [1, 2, 3, 4]
sorted_arr_desc = [4, 3, 2, 1]


def recInsertionSort(inp_arr):

    for i in range(1, len(inp_arr)):
        current = inp_arr[i]
        j = i - 1

        def recursion(j):
            # import pdb

            # pdb.set_trace()
            if j < 0 or inp_arr[j] < current:
                return j
            if inp_arr[j] > current:
                inp_arr[j + 1] = inp_arr[j]
            j -= 1
            recursion(j)

        j = recursion(j) or j
        inp_arr[j + 1] = current

    return inp_arr


print(recInsertionSort(arr))
