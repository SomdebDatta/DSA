def add(n):
    if n <= 0:
        return 0
    else:
        return n + add(n - 1)


print(add(5))
