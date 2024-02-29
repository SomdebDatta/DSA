arr = [0, -1, 10, 19, -5, 90]
print(f"OG arr - {arr}")


def merge(lb, ub):
    import pdb

    pdb.set_trace()
    print(f"Inside merge func - lb - {lb} ub - {ub}")
    sorted_arr = list()
    mid = (lb + ub) // 2
    print(f"mid - {mid}")
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
    # for i in range(lb, ub):
    #     arr[i]


def mergeSort(lb, ub):
    if lb >= ub:
        return
    if lb < ub:
        mid = (lb + ub) // 2
        # print(f"lb - {lb} mid - {mid} ub - {ub} ")
        mergeSort(lb, mid)
        mergeSort(mid + 1, ub)
        merge(lb, ub)


mergeSort(0, len(arr))
print(arr)
