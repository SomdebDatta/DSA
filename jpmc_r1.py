"""
Question:
Create a mock data table with 50 rows x 10 cols.
The cols are - 4 ints, 3 str, 3 bools
There should be a primary key separately.
"""

from typing import List
import random

def get_rows(index) -> List:
    """
    index: primary key
    """
    words = 'My name is Somdeb Datta. I\'m a backend developer at Dell Technologies.'.split(' ')
    res = [index]
    ints = random.choices(population=[random.randrange(0, 1000) for _ in range(10)], k=4)
    res.extend(ints)
    strs = random.choices(population=words, k=4)
    res.extend(strs)
    bools = [random.choice([True, False]) for _ in range(3)]
    res.extend(bools)
    print(res)
    return res

mock1 = [get_rows(index) for index in range(50)]

print(mock1)