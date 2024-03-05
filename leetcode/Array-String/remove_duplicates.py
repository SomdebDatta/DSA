# Remove duplicates from sorted array
def removeDuplicates(arr):
    removed_arr = list()
    curr = arr[0]
    removed_arr.append(curr)
    for i in range(1, len(arr)):
        if arr[i] == curr:
            continue
        else:
            removed_arr.append(arr[i])
            curr = arr[i]
    return removed_arr


arr = [1, 1, 2, 3, 4, 4, 5, 5, 5, 6, 7, 7]
print(removeDuplicates(arr))
