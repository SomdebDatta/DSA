arr = [5, 1, 3, 7, 0]


def sortAsc(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


print(sortAsc(arr))
