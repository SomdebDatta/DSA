po2 = lambda x: x > 0 and not (x & (x - 1))
print(po2(10 & 7))
