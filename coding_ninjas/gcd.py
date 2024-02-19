def gcd(x, y):
    # print(x, y)
    if x == 0:
        print(y)
    if y == 0:
        print(x)
    else:

        if x > y:
            gcd(y, x % y)
        else:
            gcd(x, y % x)


gcd(20, 5)
