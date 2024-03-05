def secondLargest(arr):
    maxi, maxii = min(arr[0], arr[1]), max(arr[0], arr[1])
    mini, minii = maxii, maxi

    for i in range(2, len(arr)):
        if arr[i] > maxi:
            if arr[i] > maxii:
                maxi = maxii
                maxii = arr[i]
            else:
                maxi = arr[i]
        if arr[i] < mini:
            if arr[i] < minii:
                mini = minii
                minii = arr[i]
            else:
                mini = arr[i]

    print(mini, maxi)


arr = [4, 2, 1, 6, 7]
arr2 = [4, 5, 3, 6, 7]
secondLargest(arr2)
