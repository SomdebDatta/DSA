class Dummy:
    name = 'Somdeb Datta'
    
    def __init__(self, salary):
        print(f'Creating a class {__class__.__name__}')
        self.salary = salary
    
    @staticmethod
    def greet():
        print('hello')
    
    @classmethod
    def class_greet(cls):
        print(cls.name)


def instantiate_obj(cls, *args, **kwargs):
    cls(*args, **kwargs)


obj1 = Dummy(5)
Dummy.greet()