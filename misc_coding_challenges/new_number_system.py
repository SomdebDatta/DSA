my_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
}

number = "ac"
my_list = list(number)
n = len(number)
int_number = 0
ct = 0
for i in range(n - 1, -1, -1):
    int_number += my_dict[my_list[i]] * 20**ct
    ct += 1
print(int_number)
