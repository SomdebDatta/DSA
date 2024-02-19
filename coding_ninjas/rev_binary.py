def reverseBits(n):
    # Write your code here.
    pass
    binary = format(n, "b")
    length = len(binary)

    rev_binary = reverse_binary(binary)
    return binary_to_decimal(rev_binary)


def reverse_binary(n):
    rev_binary = list(n)[::-1]

    for _ in range(32 - len(rev_binary)):
        rev_binary.append("0")
    return "".join(rev_binary)


def binary_to_decimal(n):
    decimal = 0
    for i in range(1, 33):
        decimal += int(n[i - 1]) * (2 ** (32 - i))
    return decimal


print(reverseBits(123))
