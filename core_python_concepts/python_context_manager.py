def context_manager_example():
    class Dummy:
        def __enter__(self):
            print("Entering context")
            return self
        
        def __init__(self, a, b):
            print("Initializing Dummy")
            self.a = a
            self.b = b

        def add(self):
            print("Adding values")
            return self.a + self.b
        
        def __exit__(self, exc_type, exc_value, traceback):
            print("Exiting context")
            if exc_type is not None:
                print(f"An exception occurred: {exc_value}")
            return True

    
    with Dummy(10, 20) as dummy_obj:
        print("Inside with block")
        result = dummy_obj.add()
        print(f"Result of addition: {result}")

if __name__ == '__main__':
    context_manager_example()
