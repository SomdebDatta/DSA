def basic_operations():
    my_list = [1, 2, 3, 4]
    my_iter = iter(my_list)
    
    # Using __next__ magic function
    while my_iter:
        print(my_iter.__next__())

    # 2nd approach
    while my_iter:
        print(next(my_iter))

    # 3rd approach
    for val in my_iter:
        print(val)


def create_iterator():
    """Custom Iterator"""
    class TopTen:

        def __init__(self):
            self.num = 1

        def __iter__(self):
            return self
    
        def __next__(self):

            if self.num > 10:
                raise StopIteration

            val = self.num
            self.num += 1
            return val
        
    obj = TopTen()
    print(obj)
    my_iter = iter(obj)
    print(my_iter)
    for val in my_iter:
        print(val)

if __name__ == '__main__':
    basic_operations()
    # create_iterator()