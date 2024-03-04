def largest(arr):
    maxi = arr[0]
    for elem in arr:
        maxi = max(elem, maxi)
    return maxi


def recursiveLargest(arr):
    n = len(arr)
    maxi = [arr[0]]
    i = 0

    def recursion(arr, maxi, i, n):
        maxi[0] = max(arr[i], maxi[0])
        i += 1
        if i == n:
            return
        recursion(arr, maxi, i, n)

    recursion(arr, maxi, i, n)
    return maxi[0]


arr = [1, 2, 3, 4, 5]
print(largest(arr))
print(recursiveLargest(arr))
