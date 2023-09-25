# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A, K, L):
    # Implement your solution here
    n = len(A)
    max_sum1, max_sum2 = 0, 0
    occupied_pos = 0
    max_list = list()
    if K + L > n:
        return -1
    for i in range(0, n - K + 1):
        # print(A[i : i + K])
        if sum(A[i : i + K]) > max_sum1:
            max_sum1 = sum(A[i : i + K])
            occupied_pos = i
    # print(max_sum1, occupied_pos)
    i = 0
    while i < n - L + 1:
        if i == (occupied_pos - L + 1) or occupied_pos == 0:
            i = occupied_pos + K
        # print(i, A[i : i + L])
        max_sum2 = max(max_sum2, sum(A[i : i + L]))
        i += 1
    # print(max_sum2)
    max_list.append(max_sum1 + max_sum2)

    max_sum1, max_sum2 = 0, 0
    for i in range(0, n - L + 1):
        if sum(A[i : i + L]) > max_sum1:
            max_sum1 = sum(A[i : i + L])
            occupied_pos = i
    # print(max_sum1, occupied_pos)
    i = 0
    while i < n - K + 1:
        if i == (occupied_pos - K + 1) or occupied_pos == 0:
            i = occupied_pos + L
        max_sum2 = max(max_sum2, sum(A[i : i + K]))
        i += 1
    # print(max_sum2)
    max_list.append(max_sum1 + max_sum2)
    # print(max_list)
    return max(max_list)


A = [6, 1, 4, 6, 3, 2, 7, 4]
A = [6, 1, 8, 8, 12, 2, 7, 6]
A = [5, 7, 2, 8]
K = 2
L = 2
print(solution(A, K, L))
