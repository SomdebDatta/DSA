empty_arr = []
single_elem_arr = [0]
arr = [13, 46, 24, 52, 20, 9]
sorted_arr_asc = [1, 2, 3, 4]
sorted_arr_desc = [4, 3, 2, 1]


def recInsertionSort(inp_arr):
    i = 1
    j = i - 1
    current = inp_arr[i]

    def recursion(i, j, current):
        # import pdb

        # pdb.set_trace()
        if i == len(inp_arr):
            return
        if j < 0:
            i += 1
            j = i - 1
            recursion(i, j, current)
        if inp_arr[j] > current and j != len(inp_arr) - 1:
            print(i, j)
            inp_arr[j + 1] = inp_arr[j]
            j -= 1
            recursion(i, j, current)
        inp_arr[j + 1] = current
        i += 1
        j = i - 1
        current = inp_arr[i]
        recursion(i, j, current)

    recursion(i, j, current)
    print(inp_arr)


print(recInsertionSort(arr))
