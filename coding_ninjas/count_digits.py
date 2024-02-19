def countDigits(n: int) -> int:
    # Write your code here
    # return len(str(n))
    ct = 0
    while n > 0:
        ct += 1
        n = n // 10
    return ct


print(countDigits(121))
