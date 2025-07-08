"""
Question:
Create a mock data table with 50 rows x 10 cols.
The cols are - 3 ints, 3 str, 3 bools
There should be a primary key separately.
"""

from typing import List, Generator
import random

def get_rows(index) -> Generator[int, str, bool]:
    """
    index: primary key
    """
    words = 'My name is Somdeb Datta. I\'m a backend developer at Dell Technologies.'.split(' ')
    res = [index]
    ints = random.choices(population=[random.randrange(0, 1000) for _ in range(10)], k=3)
    res.extend(ints)
    strs = random.choices(population=words, k=4)
    res.extend(strs)
    bools = [random.choice([True, False]) for _ in range(3)]
    res.extend(bools)
    yield res

mock1 = [row for index in range(50) for row in get_rows(index)]

print(mock1)
