arr = [13, 46, 24, 52, 20, 9]

i, j = 0, 0


def recBubbleSort(i, j):
    # print(f"i-{i} and j-{j} and arr2-{arr2}")
    if i == len(arr):
        # print(f"i has become equal to len..early return")
        return
    if j == len(arr) - i - 1:
        # print(f"Starting next i loop without swapping")
        j = 0
        i += 1
        recBubbleSort(i, j)
        return
    if arr[j] < arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
    j += 1
    recBubbleSort(i, j)


recBubbleSort(i, j)
print(arr)
# print(recBubbleSort(i, j))
