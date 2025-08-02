def singleton_approach1():
    class Dummy:
        _self = None

        def __new__(cls):
            """This constructor will return the same instance of the class every time an object is created."""
            if cls._self is not None:
                return cls._self
            cls._self = super().__new__(cls)
            return cls._self
        
        def __init__(self):
            self.name = 'Somdeb Datta'
        
        def greet(self):
            return f'Hello my name is {self.name}'
    
    obj = Dummy()
    print(obj)
    print(obj.greet())
    obj2 = Dummy()
    print(obj2)
    print(obj2.greet())

def singleton_approach2():

    class Dummy:
        _self = None

        def __new__(cls):
            """This constructor will not allow a 2nd instantiation of the class"""
            if cls._self is not None:
                return 'Kya re singleton hai yeh'
            cls._self = super().__new__(cls)
            return cls._self
        
        def __init__(self):
            self.name = 'Somdeb Datta'
        
        def greet(self):
            return f'Hello my name is {self.name}'

    obj = Dummy()
    print(obj)
    print(obj.greet())
    obj2 = Dummy()
    print(obj2)
    print(obj2.greet())


def normal_class():
    class Dummy:
        def __init__(self):
            self.name = 'Somdeb Datta'
        
        def greet(self):
            return f'Hello my name is {self.name}'
    

    obj = Dummy()
    print(obj)
    print(obj.greet())
    obj2 = Dummy()
    print(obj2)
    print(obj2.greet())

if __name__ == '__main__':
    singleton_approach1()
    # singleton_approach2()
    # normal_class()

