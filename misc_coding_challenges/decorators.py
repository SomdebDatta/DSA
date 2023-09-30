import time


class decorator_class(object):
    def __init__(self, x_func):
        self.x_func = x_func

    def __call__(self, *args, **kwargs):
        self.x_func(*args, **kwargs)
        print(f"Function {self.x_func.__name__} ran successfully.")


def decorator(x_func):
    def wrapper(*args, **kwargs):
        x_func(*args, **kwargs)
        print(f"Function {x_func.__name__} ran successfully.")

    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(f"Function {func.__name__} ran successfully.")
        print(
            f"Time taken to run {func.__name__} is {round((time.time() - start),4)}secs."
        )

    return wrapper


@timer
def tp_print():
    print("This is timepass print")


@timer
def test_timer(sleep_secs):
    time.sleep(sleep_secs)


@timer
def print_val(x: int):
    print(f"This function prints the value passed squared.")
    print(f"Value passed is {x}. Square of {x} is {x**2}")


tp_print()
print_val(10)
test_timer(5)
