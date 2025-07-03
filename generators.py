""" "
1. Implement yield
2. Why is it needed?
"""
import psutil
import os
from typing import Generator


from decorators import timer


class Generators:
    def __init__(self, n):
        self.n = n
        self.nums = [i for i in range(1, n + 1)]

    def yield_till_n(self) -> Generator:
        """
        Yields all numbers from 1 to n
        """
        for num in self.nums:
            yield num

    def return_till_n(self):
        return self.nums


gen = Generators(5000000)


@timer
def use_yield():
    for val in gen.yield_till_n():
        # print(val)
        pass


@timer
def use_return():
    for val in gen.return_till_n():
        # print(val)
        pass

process = psutil.Process(os.getpid())

# Before processing
mem_before_yield = process.memory_info().rss # in bytes
use_yield()
mem_after_yield = process.memory_info().rss
print(f'Memory used by yield - {mem_before_yield - mem_before_yield} bytes')

mem_before_return = process.memory_info().rss
use_return()
mem_after_return = process.memory_info().rss
print(f'Memory used by return - {mem_after_return - mem_before_return} bytes')
