# steps = 4
# badindex = 6
# step, i, j = 0, 0, 1
# while step<steps:


import math


def max_reachable_index(N, B):
    max_index = 0
    for i in range(N):
        if i != B:
            max_index += math.pow(2, N - i - 1)
    return int(max_index)


N = 4
B = 6
print(max_reachable_index(N, B))
