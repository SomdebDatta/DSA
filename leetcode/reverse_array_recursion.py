arr = [1, 2, 3, 4, 5]


def revArray(arr):

    start, end = 0, len(arr) - 1
    for i in range(end // 2):
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


def revArrayRec(arr):
    start, end = 0, len(arr) - 1

    def function(start, end):
        if start == end:
            return

        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    function(start, end)
    return arr


print(revArrayRec(arr))
