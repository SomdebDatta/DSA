import logging
import time

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def timer(func):
    """
    This decorator is a timer used to observe the time taken to execute a function
    """

    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        logger.info(f"Time taken to execute {func.__name__} - {time.time() - start}s")
        return res

    return wrapper


@timer
def tester():
    for i in range(5000000):
        pass


class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
        self.__gender = 'M'
    
    @property
    def salary(self):
        """Getter for salary"""
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value
    
    @property
    def name(self):
        """Getter for name"""
        return self._name


if __name__ == "__main__":
    # tester()
    emp = Employee('Somdeb', 50)
    print(emp.name)
    print(emp.salary)
    emp.salary = 50000
    print(emp.salary)
    print(emp._Employee__gender) # This is how you access a private member of the class using name mangling