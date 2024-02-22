count = 0


def recursionCount(count):
    if count == 5:
        return count
    count += 1
    return recursionCount(count)


print(recursionCount(count))
